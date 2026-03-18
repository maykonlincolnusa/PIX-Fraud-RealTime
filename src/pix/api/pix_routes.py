from __future__ import annotations

import asyncio

from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import Response

from src.pix.mock.generator import generate_pix_transactions
from src.pix.schemas import (
    PixFraudDecision,
    PixPublishRequest,
    PixTransaction,
    PixTransactionIn,
)
from src.pix.security.sels_immutable_log import sels_logger
from src.pix.services.metrics import pix_metrics
from src.pix.services.processing_service import pix_processing_service
from src.pix.services.repository import pix_repository
from src.pix.streaming.producer import pix_kafka_producer
from src.sovereign.module import SovereignPixModule

router = APIRouter(prefix="/pix", tags=["pix"])
sovereign_module = SovereignPixModule()


@router.get("/public/status")
def pix_status() -> dict:
    return {
        "module": "PIX-Fraud-RealTime",
        "streaming": "active",
        "sels_chain_valid": sels_logger.verify_chain(),
    }


@router.post("/score", response_model=PixFraudDecision)
async def score_single_pix(transaction: PixTransactionIn) -> PixFraudDecision:
    tx = transaction.normalized()
    return await pix_processing_service.process(tx)


@router.post("/score/batch", response_model=list[PixFraudDecision])
async def score_batch_pix(transactions: list[PixTransactionIn]) -> list[PixFraudDecision]:
    decisions = []
    for incoming in transactions:
        decision = await pix_processing_service.process(incoming.normalized())
        decisions.append(decision)
    return decisions


@router.get("/transactions/recent", response_model=list[PixTransaction])
def list_recent_pix(limit: int = 200) -> list[PixTransaction]:
    return pix_repository.list_recent_transactions(limit=limit)


@router.get("/metrics")
def pix_runtime_metrics() -> dict:
    return pix_metrics.snapshot().model_dump(mode="json")


@router.get("/metrics/prometheus")
def pix_prometheus_metrics() -> Response:
    payload, content_type = pix_metrics.prometheus_payload()
    return Response(content=payload, media_type=content_type)


@router.post("/mock/publish")
async def publish_mock_stream(
    payload: PixPublishRequest,
    background_tasks: BackgroundTasks,
) -> dict:
    background_tasks.add_task(
        _publish_mock_stream_task,
        payload.transactions_per_second,
        payload.duration_seconds,
        payload.fraud_ratio,
    )
    return {
        "status": "accepted",
        "transactions_per_second": payload.transactions_per_second,
        "duration_seconds": payload.duration_seconds,
    }


@router.post("/mock/local")
async def score_mock_locally(payload: PixPublishRequest) -> dict:
    total = payload.transactions_per_second * payload.duration_seconds
    transactions = generate_pix_transactions(
        total_transactions=total,
        fraud_ratio=payload.fraud_ratio,
        seed=21,
    )
    for tx in transactions:
        await pix_processing_service.process(tx)
    return {"status": "ok", "processed": total}


@router.get("/decisions/{transaction_id}", response_model=PixFraudDecision)
def get_decision(transaction_id: str) -> PixFraudDecision:
    from uuid import UUID

    try:
        parsed = UUID(transaction_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="invalid transaction id") from exc

    decision = pix_repository.get_decision(parsed)
    if not decision:
        raise HTTPException(status_code=404, detail="decision not found")
    return decision


@router.get("/sels/verify")
def verify_sels_chain() -> dict:
    return {"valid": sels_logger.verify_chain()}


@router.get("/sovereign/health")
def sovereign_health() -> dict:
    return sovereign_module.health()


async def _publish_mock_stream_task(tps: int, duration: int, fraud_ratio: float) -> None:
    total = tps * duration
    transactions = generate_pix_transactions(
        total_transactions=total,
        fraud_ratio=fraud_ratio,
        seed=99,
    )

    await pix_kafka_producer.start()
    interval = 1.0 / tps

    for tx in transactions:
        await pix_kafka_producer.publish(tx)
        await asyncio.sleep(interval)

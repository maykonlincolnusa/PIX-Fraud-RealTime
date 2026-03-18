from __future__ import annotations

from src.pix.schemas import PixFraudDecision, PixTransaction
from src.pix.security.sels_immutable_log import sels_logger
from src.pix.services.alerting import alert_dispatcher
from src.pix.services.metrics import pix_metrics
from src.pix.services.repository import pix_repository
from src.pix.services.scoring_service import pix_scoring_service
from src.pix.services.sovereign_adapter import sovereign_adapter
from src.pix.ws.broadcaster import pix_broadcaster


class PixProcessingService:
    async def process(self, tx: PixTransaction) -> PixFraudDecision:
        pix_repository.save_transaction(tx)
        decision = pix_scoring_service.score(tx)
        pix_repository.save_decision(decision)

        pix_metrics.record(amount=tx.amount, is_fraud=decision.is_fraud, latency_ms=decision.latency_ms)
        sels_logger.append(
            "pix_scoring_decision",
            {
                "transaction_id": str(tx.transaction_id),
                "score": decision.score,
                "is_fraud": decision.is_fraud,
                "latency_ms": decision.latency_ms,
            },
        )

        await pix_broadcaster.publish(tx, decision)

        if decision.is_fraud:
            await alert_dispatcher.dispatch(tx, decision)
            pix_metrics.record_alert()
            await sovereign_adapter.publish_decision(tx, decision)

        return decision


pix_processing_service = PixProcessingService()

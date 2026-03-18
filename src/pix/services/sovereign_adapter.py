from __future__ import annotations

from typing import Any

import httpx

from src.core.settings import settings
from src.pix.schemas import PixFraudDecision, PixTransaction


class SovereignAdapter:
    """Integra o modulo PIX com Sovereign AI Security Platform."""

    async def publish_decision(self, tx: PixTransaction, decision: PixFraudDecision) -> None:
        if not settings.SOVEREIGN_PLATFORM_WEBHOOK:
            return

        payload: dict[str, Any] = {
            "domain": "pix-fraud-realtime",
            "version": "1.0",
            "transaction": {
                "transaction_id": str(tx.transaction_id),
                "end_to_end_id": tx.end_to_end_id,
                "payer_id": _mask_identifier(tx.payer_id),
                "payee_id": _mask_identifier(tx.payee_id),
                "amount": tx.amount,
                "timestamp": tx.timestamp.isoformat(),
                "channel": tx.channel,
            },
            "decision": {
                "score": decision.score,
                "is_fraud": decision.is_fraud,
                "reasons": decision.reasons,
                "latency_ms": decision.latency_ms,
            },
            "compliance": {
                "lgpd": "pseudonymized",
                "data_residency": "BR",
            },
        }

        headers = {}
        if settings.SOVEREIGN_PLATFORM_TOKEN:
            headers["Authorization"] = f"Bearer {settings.SOVEREIGN_PLATFORM_TOKEN}"

        async with httpx.AsyncClient(timeout=5.0) as client:
            await client.post(settings.SOVEREIGN_PLATFORM_WEBHOOK, json=payload, headers=headers)


def _mask_identifier(identifier: str) -> str:
    if len(identifier) <= 4:
        return "****"
    return f"{identifier[:2]}***{identifier[-2:]}"


sovereign_adapter = SovereignAdapter()

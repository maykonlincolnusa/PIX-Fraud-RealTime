from __future__ import annotations

from typing import Any

import httpx

from src.core.settings import settings
from src.pix.schemas import PixFraudDecision, PixTransaction


class AlertDispatcher:
    async def dispatch(self, tx: PixTransaction, decision: PixFraudDecision) -> None:
        if not decision.is_fraud:
            return

        message = self._build_message(tx, decision)

        async with httpx.AsyncClient(timeout=5.0) as client:
            await self._send_telegram(client, message)
            await self._send_whatsapp(client, message)

    async def _send_telegram(self, client: httpx.AsyncClient, message: str) -> None:
        if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
            return

        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload: dict[str, Any] = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown",
        }
        await client.post(url, json=payload)

    async def _send_whatsapp(self, client: httpx.AsyncClient, message: str) -> None:
        if not settings.WHATSAPP_API_URL or not settings.WHATSAPP_TOKEN:
            return

        headers = {
            "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
            "Content-Type": "application/json",
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": settings.WHATSAPP_TO,
            "type": "text",
            "text": {"body": message},
        }
        await client.post(settings.WHATSAPP_API_URL, headers=headers, json=payload)

    def _build_message(self, tx: PixTransaction, decision: PixFraudDecision) -> str:
        return (
            "*ALERTA FRAUDE PIX*\n"
            f"E2E: `{tx.end_to_end_id}`\n"
            f"Valor: R$ {tx.amount:,.2f}\n"
            f"Pagador: {tx.payer_id}\n"
            f"Recebedor: {tx.payee_id}\n"
            f"Risco: {decision.score:.2%}\n"
            f"Motivos: {', '.join(decision.reasons[:5])}"
        )


alert_dispatcher = AlertDispatcher()

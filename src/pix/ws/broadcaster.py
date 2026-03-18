from __future__ import annotations

import asyncio
from typing import Any, Dict, Set

from fastapi import WebSocket

from src.pix.schemas import PixFraudDecision, PixTransaction


class PixBroadcaster:
    def __init__(self) -> None:
        self._connections: Set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections.add(websocket)

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self._lock:
            self._connections.discard(websocket)

    async def publish(self, tx: PixTransaction, decision: PixFraudDecision) -> None:
        async with self._lock:
            connections = list(self._connections)

        if not connections:
            return

        payload: Dict[str, Any] = {
            "transaction_id": str(tx.transaction_id),
            "end_to_end_id": tx.end_to_end_id,
            "amount": tx.amount,
            "city": tx.city,
            "state": tx.state,
            "score": decision.score,
            "is_fraud": decision.is_fraud,
            "reasons": decision.reasons,
            "latency_ms": decision.latency_ms,
            "timestamp": tx.timestamp.isoformat(),
        }

        for websocket in connections:
            try:
                await websocket.send_json(payload)
            except Exception:
                await self.disconnect(websocket)


pix_broadcaster = PixBroadcaster()

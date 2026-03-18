from __future__ import annotations

import json

from src.core.settings import settings
from src.pix.schemas import PixTransaction
from src.pix.streaming.kafka import PIX_TOPIC, kafka_enabled

try:
    from aiokafka import AIOKafkaProducer
except Exception:  # pragma: no cover
    AIOKafkaProducer = None


class PixKafkaProducer:
    def __init__(self) -> None:
        self._producer = None

    async def start(self) -> None:
        if not kafka_enabled() or AIOKafkaProducer is None:
            return
        if self._producer is not None:
            return

        self._producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
        try:
            await self._producer.start()
        except Exception:
            self._producer = None

    async def stop(self) -> None:
        if self._producer is None:
            return
        await self._producer.stop()
        self._producer = None

    async def publish(self, tx: PixTransaction) -> None:
        if self._producer is None:
            return

        payload = tx.model_dump(mode="json")
        await self._producer.send_and_wait(PIX_TOPIC, json.dumps(payload).encode("utf-8"))


pix_kafka_producer = PixKafkaProducer()

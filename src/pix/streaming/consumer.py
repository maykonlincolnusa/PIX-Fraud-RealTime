from __future__ import annotations

import asyncio
import json
from contextlib import suppress

from src.core.settings import settings
from src.pix.schemas import PixTransaction
from src.pix.services.processing_service import pix_processing_service
from src.pix.streaming.kafka import PIX_TOPIC, kafka_enabled

try:
    from aiokafka import AIOKafkaConsumer
except Exception:  # pragma: no cover
    AIOKafkaConsumer = None


class KafkaConsumerRuntime:
    def __init__(self) -> None:
        self._consumer = None
        self._task: asyncio.Task | None = None
        self._running = False

    async def start(self) -> None:
        if self._running:
            return

        if not kafka_enabled() or AIOKafkaConsumer is None:
            self._running = True
            return

        self._consumer = AIOKafkaConsumer(
            PIX_TOPIC,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            group_id=settings.KAFKA_GROUP_ID,
            auto_offset_reset="latest",
            enable_auto_commit=True,
        )
        try:
            await self._consumer.start()
        except Exception:
            self._consumer = None
            self._running = True
            return
        self._running = True
        self._task = asyncio.create_task(self._loop())

    async def stop(self) -> None:
        self._running = False

        if self._task:
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task
            self._task = None

        if self._consumer is not None:
            await self._consumer.stop()
            self._consumer = None

    async def _loop(self) -> None:
        if self._consumer is None:
            return

        while self._running:
            try:
                result = await self._consumer.getmany(timeout_ms=500, max_records=100)
            except Exception:
                await asyncio.sleep(0.5)
                continue

            for _topic_partition, messages in result.items():
                for message in messages:
                    try:
                        payload = json.loads(message.value.decode("utf-8"))
                        tx = PixTransaction(**payload)
                        await pix_processing_service.process(tx)
                    except Exception:
                        # Em producao, enviar para DLQ.
                        continue


kafka_consumer_runtime = KafkaConsumerRuntime()

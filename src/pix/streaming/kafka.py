from __future__ import annotations

from src.core.settings import settings

PIX_TOPIC = settings.KAFKA_PIX_TOPIC
PIX_ALERTS_TOPIC = settings.KAFKA_ALERT_TOPIC


def kafka_enabled() -> bool:
    return bool(settings.KAFKA_BOOTSTRAP_SERVERS)

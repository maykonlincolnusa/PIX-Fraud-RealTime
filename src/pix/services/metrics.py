from __future__ import annotations

from datetime import datetime

try:
    from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, Histogram, generate_latest
except Exception:  # pragma: no cover
    CONTENT_TYPE_LATEST = "text/plain; version=0.0.4"

    class _NoopMetric:
        def inc(self, *_args, **_kwargs) -> None:
            return None

        def set(self, *_args, **_kwargs) -> None:
            return None

        def observe(self, *_args, **_kwargs) -> None:
            return None

    def Counter(*_args, **_kwargs):  # type: ignore[misc]
        return _NoopMetric()

    def Gauge(*_args, **_kwargs):  # type: ignore[misc]
        return _NoopMetric()

    def Histogram(*_args, **_kwargs):  # type: ignore[misc]
        return _NoopMetric()

    def generate_latest() -> bytes:
        return b""

from src.pix.schemas import PixStreamStats

PIX_PROCESSED = Counter("pix_processed_total", "Total de transacoes PIX processadas")
PIX_FRAUD = Counter("pix_fraud_total", "Total de transacoes marcadas como fraude")
PIX_ALERTS = Counter("pix_alerts_total", "Total de alertas enviados")
PIX_LATENCY = Histogram(
    "pix_scoring_latency_ms",
    "Latencia de scoring PIX em ms",
    buckets=(5, 10, 20, 50, 100, 200, 500, 1000),
)
PIX_FRAUD_RATE = Gauge("pix_fraud_rate", "Taxa de fraude PIX em tempo real")
PIX_VOLUME = Gauge("pix_volume_last_minute", "Volume total PIX no ultimo minuto")


class PixMetrics:
    def __init__(self) -> None:
        self._processed = 0
        self._fraud = 0
        self._latency_sum = 0.0
        self._volume_minute = 0.0
        self._last_updated = datetime.utcnow()

    def record(self, amount: float, is_fraud: bool, latency_ms: float) -> None:
        self._processed += 1
        self._fraud += int(is_fraud)
        self._latency_sum += latency_ms
        self._volume_minute += amount
        self._last_updated = datetime.utcnow()

        PIX_PROCESSED.inc()
        PIX_LATENCY.observe(latency_ms)
        PIX_VOLUME.set(self._volume_minute)

        if is_fraud:
            PIX_FRAUD.inc()

        PIX_FRAUD_RATE.set(self._fraud / max(self._processed, 1))

    def record_alert(self) -> None:
        PIX_ALERTS.inc()

    def snapshot(self) -> PixStreamStats:
        avg_latency = self._latency_sum / max(self._processed, 1)
        return PixStreamStats(
            processed_transactions=self._processed,
            fraud_detected=self._fraud,
            fraud_rate=self._fraud / max(self._processed, 1),
            average_latency_ms=avg_latency,
            last_updated=self._last_updated,
        )

    def prometheus_payload(self) -> tuple[bytes, str]:
        return generate_latest(), CONTENT_TYPE_LATEST


pix_metrics = PixMetrics()

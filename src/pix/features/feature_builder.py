from __future__ import annotations

from datetime import datetime
from typing import Dict, Iterable, List

from src.pix.schemas import PixTransaction

CITY_RISK = {
    "Sao Paulo": 0.3,
    "Rio de Janeiro": 0.35,
    "Belo Horizonte": 0.28,
    "Curitiba": 0.2,
    "Salvador": 0.32,
    "Recife": 0.33,
    "Fortaleza": 0.31,
}


def build_feature_sequence(
    tx: PixTransaction,
    history: Iterable[PixTransaction],
    seq_len: int = 12,
) -> tuple[list[list[float]], dict[str, float]]:
    ordered_history = sorted(history, key=lambda item: item.timestamp)
    vectors: List[List[float]] = []

    for hist_tx in ordered_history[-(seq_len - 1) :]:
        vectors.append(_vectorize(hist_tx, ordered_history))

    vectors.append(_vectorize(tx, ordered_history + [tx]))

    if len(vectors) < seq_len:
        missing = seq_len - len(vectors)
        vectors = [[0.0] * 12 for _ in range(missing)] + vectors

    latest = _to_named_features(vectors[-1])
    return vectors[-seq_len:], latest


def _vectorize(tx: PixTransaction, window: list[PixTransaction]) -> List[float]:
    same_payer = [item for item in window if item.payer_id == tx.payer_id]
    same_payer_sorted = sorted(same_payer, key=lambda item: item.timestamp)

    one_hour_ago = tx.timestamp.timestamp() - 3600
    one_day_ago = tx.timestamp.timestamp() - 86400
    count_1h = sum(1 for item in same_payer if item.timestamp.timestamp() >= one_hour_ago)
    count_24h = sum(1 for item in same_payer if item.timestamp.timestamp() >= one_day_ago)
    sum_24h = sum(item.amount for item in same_payer if item.timestamp.timestamp() >= one_day_ago)

    prev = same_payer_sorted[-2] if len(same_payer_sorted) >= 2 else None
    minutes_since_last = (
        max((tx.timestamp - prev.timestamp).total_seconds() / 60.0, 0.0)
        if prev
        else 720.0
    )

    seen_payee = any(item.payee_id == tx.payee_id for item in same_payer_sorted[:-1])
    payee_first_seen_hours = 0.0 if seen_payee else 168.0

    hour = tx.timestamp.hour
    is_night = 1.0 if hour >= 22 or hour <= 5 else 0.0

    velocity_ratio = float(count_1h) / float(max(count_24h, 1))

    vector = [
        _log1p(tx.amount),
        is_night,
        1.0 if tx.is_new_beneficiary else 0.0,
        min(minutes_since_last, 720.0) / 720.0,
        min(float(count_1h), 40.0) / 40.0,
        min(float(count_24h), 200.0) / 200.0,
        min(sum_24h, 300000.0) / 300000.0,
        payee_first_seen_hours / 168.0,
        CITY_RISK.get(tx.city, 0.25),
        1.0 - tx.device_trust_score,
        min(float(tx.failed_auth_count_24h), 10.0) / 10.0,
        min(velocity_ratio, 1.0),
    ]
    return vector


def _to_named_features(vector: list[float]) -> Dict[str, float]:
    names = [
        "log_amount",
        "is_night",
        "is_new_beneficiary",
        "minutes_since_last_norm",
        "payer_count_1h_norm",
        "payer_count_24h_norm",
        "payer_sum_24h_norm",
        "payee_first_seen_norm",
        "city_risk",
        "device_risk",
        "failed_auth_norm",
        "velocity_ratio",
    ]
    return dict(zip(names, vector, strict=True))


def _log1p(value: float) -> float:
    import math

    return math.log1p(max(value, 0.0)) / 12.0

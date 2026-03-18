from __future__ import annotations

import time
from datetime import datetime

from src.pix.feature_store.timescale_store import pix_feature_store
from src.pix.ml.aids_lstm import aids_lstm_scorer
from src.pix.schemas import PixFraudDecision, PixTransaction


class PixScoringService:
    def score(self, tx: PixTransaction) -> PixFraudDecision:
        start = time.perf_counter()
        feature_vector = pix_feature_store.build_realtime_features(tx)
        lstm_score = aids_lstm_scorer.score(feature_vector.sequence)
        rules_score, reasons = _rules_score(tx, feature_vector.latest_features)

        final_score = min(1.0, (0.62 * lstm_score) + (0.38 * rules_score))
        is_fraud = final_score >= 0.78

        latency_ms = (time.perf_counter() - start) * 1000.0

        return PixFraudDecision(
            transaction_id=tx.transaction_id,
            end_to_end_id=tx.end_to_end_id,
            score=final_score,
            lstm_score=lstm_score,
            rules_score=rules_score,
            is_fraud=is_fraud,
            latency_ms=latency_ms,
            reasons=reasons,
            created_at=datetime.utcnow(),
        )


pix_scoring_service = PixScoringService()


def _rules_score(tx: PixTransaction, features: dict[str, float]) -> tuple[float, list[str]]:
    score = 0.0
    reasons: list[str] = []

    if tx.amount >= 50000:
        score += 0.36
        reasons.append("valor_muito_alto")
    elif tx.amount >= 15000:
        score += 0.2
        reasons.append("valor_alto")

    hour = tx.timestamp.hour
    if hour >= 22 or hour <= 5:
        score += 0.18
        reasons.append("horario_noturno")

    if tx.is_new_beneficiary:
        score += 0.16
        reasons.append("beneficiario_novo")

    if tx.device_trust_score <= 0.45:
        score += 0.17
        reasons.append("dispositivo_baixa_confianca")

    if tx.failed_auth_count_24h >= 3:
        score += 0.14
        reasons.append("multiplas_falhas_autenticacao")

    velocity = features.get("velocity_ratio", 0.0)
    if velocity >= 0.6:
        score += 0.12
        reasons.append("alta_velocidade_transacional")

    if features.get("is_night", 0.0) and features.get("is_new_beneficiary", 0.0):
        score += 0.08
        reasons.append("combinacao_critica_noturno_beneficiario")

    return min(score, 1.0), reasons

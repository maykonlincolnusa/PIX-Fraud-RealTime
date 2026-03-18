from __future__ import annotations

from src.pix.features.feature_builder import build_feature_sequence
from src.pix.schemas import PixFeatureVector, PixTransaction
from src.pix.services.repository import pix_repository


class PixFeatureStore:
    def build_realtime_features(self, tx: PixTransaction, seq_len: int = 12) -> PixFeatureVector:
        history = pix_repository.recent_payer_history(
            payer_id=tx.payer_id,
            at_time=tx.timestamp,
            lookback_hours=24,
            limit=200,
        )
        sequence, latest = build_feature_sequence(tx, history, seq_len=seq_len)
        return PixFeatureVector(
            transaction_id=tx.transaction_id,
            sequence=sequence,
            latest_features=latest,
        )


pix_feature_store = PixFeatureStore()

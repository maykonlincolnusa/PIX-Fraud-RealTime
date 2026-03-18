from __future__ import annotations

from datetime import datetime, timedelta
from typing import List
from uuid import UUID

from sqlalchemy import desc, select

from src.db.db import session_scope
from src.db.models import PixFraudDecisionDB, PixTransactionDB
from src.pix.schemas import PixFraudDecision, PixTransaction


class PixRepository:
    def save_transaction(self, tx: PixTransaction) -> None:
        with session_scope() as session:
            row = session.get(PixTransactionDB, str(tx.transaction_id))
            if row is None:
                row = PixTransactionDB(transaction_id=str(tx.transaction_id))
                session.add(row)

            row.end_to_end_id = tx.end_to_end_id
            row.payer_id = tx.payer_id
            row.payee_id = tx.payee_id
            row.payer_bank = tx.payer_bank
            row.payee_bank = tx.payee_bank
            row.amount = tx.amount
            row.city = tx.city
            row.state = tx.state
            row.timestamp = tx.timestamp
            row.pix_key_type = tx.pix_key_type
            row.channel = tx.channel
            row.device_id = tx.device_id
            row.device_trust_score = tx.device_trust_score
            row.is_new_beneficiary = tx.is_new_beneficiary
            row.failed_auth_count_24h = tx.failed_auth_count_24h
            row.metadata_json = tx.metadata

    def save_decision(self, decision: PixFraudDecision) -> None:
        with session_scope() as session:
            row = session.get(PixFraudDecisionDB, str(decision.transaction_id))
            if row is None:
                row = PixFraudDecisionDB(transaction_id=str(decision.transaction_id))
                session.add(row)

            row.end_to_end_id = decision.end_to_end_id
            row.score = decision.score
            row.lstm_score = decision.lstm_score
            row.rules_score = decision.rules_score
            row.is_fraud = decision.is_fraud
            row.latency_ms = decision.latency_ms
            row.reasons = decision.reasons
            row.created_at = decision.created_at

    def list_recent_transactions(self, limit: int = 300) -> List[PixTransaction]:
        with session_scope() as session:
            rows = (
                session.execute(
                    select(PixTransactionDB).order_by(desc(PixTransactionDB.timestamp)).limit(limit)
                )
                .scalars()
                .all()
            )
            return [self._to_transaction(item) for item in rows]

    def recent_payer_history(
        self,
        payer_id: str,
        at_time: datetime,
        lookback_hours: int = 24,
        limit: int = 200,
    ) -> List[PixTransaction]:
        since = at_time - timedelta(hours=lookback_hours)
        with session_scope() as session:
            rows = (
                session.execute(
                    select(PixTransactionDB)
                    .where(PixTransactionDB.payer_id == payer_id)
                    .where(PixTransactionDB.timestamp >= since)
                    .order_by(desc(PixTransactionDB.timestamp))
                    .limit(limit)
                )
                .scalars()
                .all()
            )
            return [self._to_transaction(item) for item in rows]

    def get_decision(self, transaction_id: UUID) -> PixFraudDecision | None:
        with session_scope() as session:
            row = session.get(PixFraudDecisionDB, str(transaction_id))
            if row is None:
                return None
            return PixFraudDecision(
                transaction_id=UUID(row.transaction_id),
                end_to_end_id=row.end_to_end_id,
                score=row.score,
                lstm_score=row.lstm_score,
                rules_score=row.rules_score,
                is_fraud=row.is_fraud,
                latency_ms=row.latency_ms,
                reasons=row.reasons or [],
                created_at=row.created_at,
            )

    def _to_transaction(self, row: PixTransactionDB) -> PixTransaction:
        return PixTransaction(
            transaction_id=UUID(row.transaction_id),
            end_to_end_id=row.end_to_end_id,
            payer_id=row.payer_id,
            payee_id=row.payee_id,
            payer_bank=row.payer_bank,
            payee_bank=row.payee_bank,
            amount=row.amount,
            city=row.city,
            state=row.state,
            timestamp=row.timestamp,
            pix_key_type=row.pix_key_type,
            channel=row.channel,
            device_id=row.device_id,
            device_trust_score=row.device_trust_score,
            is_new_beneficiary=row.is_new_beneficiary,
            failed_auth_count_24h=row.failed_auth_count_24h,
            metadata=row.metadata_json or {},
        )


pix_repository = PixRepository()

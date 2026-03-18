from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TransactionDB(Base):
    __tablename__ = "transactions"

    transaction_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    entity_id: Mapped[str] = mapped_column(String(128), index=True)
    counterparty_id: Mapped[Optional[str]] = mapped_column(String(128), index=True)
    amount: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(3))
    channel: Mapped[Optional[str]] = mapped_column(String(32))
    device_id: Mapped[Optional[str]] = mapped_column(String(128))
    country: Mapped[Optional[str]] = mapped_column(String(3))
    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True)
    features: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)
    risk_score: Mapped[float] = mapped_column(Float, default=0.0)
    risk_reasons: Mapped[List[str]] = mapped_column(JSON, default=list)


class AlertDB(Base):
    __tablename__ = "alerts"

    alert_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    transaction_id: Mapped[str] = mapped_column(String(36), index=True)
    entity_id: Mapped[str] = mapped_column(String(128), index=True)
    score: Mapped[float] = mapped_column(Float)
    reason: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="open")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class EntityDB(Base):
    __tablename__ = "entities"

    entity_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    risk_score: Mapped[float] = mapped_column(Float, default=0.0)
    last_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class InvestigationDB(Base):
    __tablename__ = "investigations"

    case_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    alert_id: Mapped[str] = mapped_column(String(36), index=True)
    entity_id: Mapped[str] = mapped_column(String(128), index=True)
    status: Mapped[str] = mapped_column(String(20), default="open")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class PixTransactionDB(Base):
    __tablename__ = "pix_transactions"

    transaction_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    end_to_end_id: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    payer_id: Mapped[str] = mapped_column(String(128), index=True)
    payee_id: Mapped[str] = mapped_column(String(128), index=True)
    payer_bank: Mapped[str] = mapped_column(String(10))
    payee_bank: Mapped[str] = mapped_column(String(10))
    amount: Mapped[float] = mapped_column(Float, index=True)
    city: Mapped[str] = mapped_column(String(128))
    state: Mapped[str] = mapped_column(String(8))
    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True)
    pix_key_type: Mapped[str] = mapped_column(String(32))
    channel: Mapped[str] = mapped_column(String(32))
    device_id: Mapped[str] = mapped_column(String(128), index=True)
    device_trust_score: Mapped[float] = mapped_column(Float, default=0.9)
    is_new_beneficiary: Mapped[bool] = mapped_column(Boolean, default=False)
    failed_auth_count_24h: Mapped[int] = mapped_column(Integer, default=0)
    metadata_json: Mapped[Dict[str, Any]] = mapped_column("metadata", JSON, default=dict)


class PixFraudDecisionDB(Base):
    __tablename__ = "pix_fraud_decisions"

    transaction_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    end_to_end_id: Mapped[str] = mapped_column(String(40), index=True)
    score: Mapped[float] = mapped_column(Float, index=True)
    lstm_score: Mapped[float] = mapped_column(Float)
    rules_score: Mapped[float] = mapped_column(Float)
    is_fraud: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    latency_ms: Mapped[float] = mapped_column(Float, default=0.0)
    reasons: Mapped[List[str]] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)


class SelsEventDB(Base):
    __tablename__ = "sels_events"

    event_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    event_type: Mapped[str] = mapped_column(String(64), index=True)
    payload_hash: Mapped[str] = mapped_column(String(128))
    prev_hash: Mapped[str] = mapped_column(String(128))
    chain_hash: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class PixTransactionIn(BaseModel):
    transaction_id: Optional[UUID] = Field(default=None)
    end_to_end_id: Optional[str] = Field(default=None)
    payer_id: str = Field(..., description="Hash/ID da conta pagadora")
    payee_id: str = Field(..., description="Hash/ID da conta recebedora")
    payer_bank: str = "001"
    payee_bank: str = "237"
    amount: float = Field(..., gt=0)
    city: str = "Sao Paulo"
    state: str = "SP"
    timestamp: Optional[datetime] = None
    pix_key_type: str = "cpf"
    channel: str = "mobile"
    device_id: str = "device_default"
    device_trust_score: float = Field(default=0.9, ge=0.0, le=1.0)
    is_new_beneficiary: bool = False
    failed_auth_count_24h: int = Field(default=0, ge=0)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def normalized(self) -> "PixTransaction":
        tx_id = self.transaction_id or uuid4()
        tx_time = self.timestamp or datetime.utcnow()
        end_to_end_id = self.end_to_end_id or f"E{tx_id.hex[:31].upper()}"
        return PixTransaction(
            transaction_id=tx_id,
            end_to_end_id=end_to_end_id,
            payer_id=self.payer_id,
            payee_id=self.payee_id,
            payer_bank=self.payer_bank,
            payee_bank=self.payee_bank,
            amount=self.amount,
            city=self.city,
            state=self.state,
            timestamp=tx_time,
            pix_key_type=self.pix_key_type,
            channel=self.channel,
            device_id=self.device_id,
            device_trust_score=self.device_trust_score,
            is_new_beneficiary=self.is_new_beneficiary,
            failed_auth_count_24h=self.failed_auth_count_24h,
            metadata=self.metadata,
        )


class PixTransaction(BaseModel):
    transaction_id: UUID
    end_to_end_id: str
    payer_id: str
    payee_id: str
    payer_bank: str
    payee_bank: str
    amount: float
    city: str
    state: str
    timestamp: datetime
    pix_key_type: str
    channel: str
    device_id: str
    device_trust_score: float
    is_new_beneficiary: bool
    failed_auth_count_24h: int
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PixFeatureVector(BaseModel):
    transaction_id: UUID
    sequence: List[List[float]]
    latest_features: Dict[str, float]


class PixFraudDecision(BaseModel):
    transaction_id: UUID
    end_to_end_id: str
    score: float = Field(..., ge=0.0, le=1.0)
    lstm_score: float = Field(..., ge=0.0, le=1.0)
    rules_score: float = Field(..., ge=0.0, le=1.0)
    is_fraud: bool
    latency_ms: float = Field(..., ge=0.0)
    reasons: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PixMockRequest(BaseModel):
    total_transactions: int = Field(default=100, ge=1, le=5000)
    fraud_ratio: float = Field(default=0.08, ge=0.0, le=1.0)
    seed: int = Field(default=42)


class PixPublishRequest(BaseModel):
    transactions_per_second: int = Field(default=10, ge=1, le=250)
    duration_seconds: int = Field(default=30, ge=1, le=3600)
    fraud_ratio: float = Field(default=0.1, ge=0.0, le=1.0)


class PixStreamStats(BaseModel):
    processed_transactions: int
    fraud_detected: int
    fraud_rate: float
    average_latency_ms: float
    last_updated: datetime

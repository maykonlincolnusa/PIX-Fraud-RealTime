from __future__ import annotations

from fastapi import APIRouter

from src.pix.mock.generator import generate_pix_transactions
from src.pix.schemas import PixMockRequest, PixTransaction

router = APIRouter(prefix="/mock", tags=["pix-mock"])


@router.post("/generate", response_model=list[PixTransaction])
def generate_mock_pix(payload: PixMockRequest) -> list[PixTransaction]:
    return generate_pix_transactions(
        total_transactions=payload.total_transactions,
        fraud_ratio=payload.fraud_ratio,
        seed=payload.seed,
    )

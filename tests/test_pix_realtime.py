import os
from pathlib import Path

os.environ["DATABASE_URL"] = "sqlite:///./data/test_pix_realtime.db"

from fastapi.testclient import TestClient

from src.Backend.app import app
from src.core.settings import settings
from src.db.session import init_db

DB_PATH = Path("data/test_pix_realtime.db")


def setup_module() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()


def test_pix_score_endpoint_under_1s() -> None:
    payload = {
        "payer_id": "payer_9001",
        "payee_id": "payee_7777",
        "amount": 18500,
        "city": "Sao Paulo",
        "state": "SP",
        "is_new_beneficiary": True,
        "device_trust_score": 0.32,
        "failed_auth_count_24h": 4,
    }

    headers = {"x-api-key": settings.PIX_API_KEY, "x-service-id": "ops-console"}

    with TestClient(app) as client:
        response = client.post("/api/v1/pix/score", json=payload, headers=headers)
        assert response.status_code == 200

        decision = response.json()
        assert 0.0 <= decision["score"] <= 1.0
        assert decision["latency_ms"] < 1000


def test_pix_zero_trust_block_without_headers() -> None:
    payload = {
        "payer_id": "payer_1",
        "payee_id": "payee_1",
        "amount": 500,
    }

    with TestClient(app) as client:
        response = client.post("/api/v1/pix/score", json=payload)
        assert response.status_code == 401

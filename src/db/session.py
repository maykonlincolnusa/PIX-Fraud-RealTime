from __future__ import annotations

from pathlib import Path
from typing import Dict

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.core.settings import settings


def _connect_args(database_url: str) -> Dict[str, object]:
    if database_url.startswith("sqlite"):
        return {"check_same_thread": False}
    return {}


def _ensure_sqlite_path(database_url: str) -> None:
    if not database_url.startswith("sqlite"):
        return
    if database_url.startswith("sqlite:///"):
        raw_path = database_url.replace("sqlite:///", "")
        path = Path(raw_path)
        if not path.is_absolute():
            path = Path.cwd() / path
        path.parent.mkdir(parents=True, exist_ok=True)


_ensure_sqlite_path(settings.DATABASE_URL)

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args=_connect_args(settings.DATABASE_URL),
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def init_db() -> None:
    from src.db.models import Base  # noqa: WPS433

    Base.metadata.create_all(bind=engine)
    init_timescale()


def init_timescale() -> None:
    if not settings.DATABASE_URL.startswith("postgresql"):
        return

    statements = [
        "CREATE EXTENSION IF NOT EXISTS timescaledb;",
        "SELECT create_hypertable('pix_transactions', 'timestamp', if_not_exists => TRUE);",
        "CREATE INDEX IF NOT EXISTS idx_pix_transactions_payer_time ON pix_transactions (payer_id, timestamp DESC);",
        "CREATE INDEX IF NOT EXISTS idx_pix_decisions_created ON pix_fraud_decisions (created_at DESC);",
    ]

    with engine.begin() as conn:
        for statement in statements:
            try:
                conn.execute(text(statement))
            except Exception:
                # Timescale nao deve impedir inicializacao da API em ambiente dev.
                continue

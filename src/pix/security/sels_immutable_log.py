from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict
from uuid import uuid4

from src.core.settings import settings
from src.db.db import session_scope
from src.db.models import SelsEventDB


@dataclass
class SelsRecord:
    event_id: str
    timestamp: str
    event_type: str
    payload_hash: str
    prev_hash: str
    chain_hash: str


class SelsImmutableLogger:
    """Secure Event Ledger System (SELS) com hash encadeado imutavel."""

    def __init__(self, log_path: str = "data/sels_ledger.jsonl") -> None:
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event_type: str, payload: Dict[str, Any]) -> SelsRecord:
        event_id = str(uuid4())
        timestamp = datetime.utcnow().isoformat()
        payload_hash = hashlib.sha256(
            json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
        ).hexdigest()
        prev_hash = self._last_hash()
        chain_hash = self._chain_hash(event_id, timestamp, event_type, payload_hash, prev_hash)

        record = SelsRecord(
            event_id=event_id,
            timestamp=timestamp,
            event_type=event_type,
            payload_hash=payload_hash,
            prev_hash=prev_hash,
            chain_hash=chain_hash,
        )

        with self.log_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(record.__dict__, ensure_ascii=False) + "\n")

        with session_scope() as session:
            session.add(
                SelsEventDB(
                    event_id=event_id,
                    event_type=event_type,
                    payload_hash=payload_hash,
                    prev_hash=prev_hash,
                    chain_hash=chain_hash,
                    created_at=datetime.utcnow(),
                )
            )

        return record

    def verify_chain(self) -> bool:
        if not self.log_path.exists():
            return True

        previous = "GENESIS"
        for line in self.log_path.read_text(encoding="utf-8").splitlines():
            raw = json.loads(line)
            expected = self._chain_hash(
                raw["event_id"],
                raw["timestamp"],
                raw["event_type"],
                raw["payload_hash"],
                previous,
            )
            if raw["prev_hash"] != previous or raw["chain_hash"] != expected:
                return False
            previous = raw["chain_hash"]

        return True

    def _last_hash(self) -> str:
        if not self.log_path.exists():
            return "GENESIS"
        lines = self.log_path.read_text(encoding="utf-8").splitlines()
        if not lines:
            return "GENESIS"
        return json.loads(lines[-1])["chain_hash"]

    def _chain_hash(
        self,
        event_id: str,
        timestamp: str,
        event_type: str,
        payload_hash: str,
        prev_hash: str,
    ) -> str:
        raw = f"{event_id}|{timestamp}|{event_type}|{payload_hash}|{prev_hash}|{settings.SELS_SALT}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()


sels_logger = SelsImmutableLogger()

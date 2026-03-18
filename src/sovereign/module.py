from __future__ import annotations

from dataclasses import dataclass

from src.pix.services.repository import pix_repository


@dataclass
class SovereignPixModule:
    module_name: str = "pix-fraud-realtime"
    version: str = "1.0.0"

    def health(self) -> dict:
        return {
            "module": self.module_name,
            "version": self.version,
            "status": "ready",
        }

    def recent_transactions(self, limit: int = 100) -> list[dict]:
        transactions = pix_repository.list_recent_transactions(limit=limit)
        return [tx.model_dump(mode="json") for tx in transactions]

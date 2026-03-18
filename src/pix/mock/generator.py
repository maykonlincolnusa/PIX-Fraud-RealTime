"""Gerador de transacoes PIX sinteticas com padroes de fraude brasileiros."""

from __future__ import annotations

import random
from datetime import datetime, timedelta
from typing import List
from uuid import uuid4

from src.pix.schemas import PixTransaction

BANKS = ["001", "033", "104", "237", "260", "341", "748"]
CITIES = [
    ("Sao Paulo", "SP"),
    ("Rio de Janeiro", "RJ"),
    ("Belo Horizonte", "MG"),
    ("Curitiba", "PR"),
    ("Salvador", "BA"),
    ("Recife", "PE"),
    ("Fortaleza", "CE"),
]
CHANNELS = ["mobile", "internet_banking", "api", "qr_code"]
PIX_KEYS = ["cpf", "email", "phone", "evp"]


def generate_pix_transactions(
    total_transactions: int = 100,
    fraud_ratio: float = 0.08,
    seed: int = 42,
) -> List[PixTransaction]:
    rnd = random.Random(seed)
    fraud_count = int(total_transactions * fraud_ratio)
    base_time = datetime.utcnow()
    txs: List[PixTransaction] = []

    for idx in range(total_transactions):
        is_fraud = idx < fraud_count
        txs.append(_build_transaction(rnd, base_time, idx, is_fraud))

    rnd.shuffle(txs)
    return txs


def _build_transaction(rnd: random.Random, base_time: datetime, idx: int, is_fraud: bool) -> PixTransaction:
    city, state = rnd.choice(CITIES)
    payer_id = f"payer_{rnd.randint(1, 500):04d}"
    payee_id = f"payee_{rnd.randint(1, 1200):04d}"
    timestamp = base_time - timedelta(seconds=rnd.randint(0, 7200))
    amount = round(rnd.lognormvariate(4.3, 0.8), 2)
    device_trust = rnd.uniform(0.5, 1.0)
    failed_auths = rnd.randint(0, 2)
    is_new_beneficiary = rnd.random() < 0.12
    pattern = "normal"

    if is_fraud:
        pattern = rnd.choice(
            [
                "high_value_night_new_beneficiary",
                "velocity_attack",
                "account_takeover",
                "mule_chain",
            ]
        )
        if pattern == "high_value_night_new_beneficiary":
            amount = round(rnd.uniform(15000, 120000), 2)
            timestamp = _force_night_time(base_time, rnd)
            is_new_beneficiary = True
            device_trust = rnd.uniform(0.2, 0.55)
            failed_auths = rnd.randint(1, 5)
        elif pattern == "velocity_attack":
            amount = round(rnd.uniform(2000, 15000), 2)
            timestamp = base_time - timedelta(seconds=rnd.randint(0, 120))
            is_new_beneficiary = rnd.random() < 0.8
            device_trust = rnd.uniform(0.3, 0.65)
            failed_auths = rnd.randint(2, 6)
        elif pattern == "account_takeover":
            amount = round(rnd.uniform(5000, 50000), 2)
            timestamp = _force_night_time(base_time, rnd)
            is_new_beneficiary = True
            device_trust = rnd.uniform(0.1, 0.45)
            failed_auths = rnd.randint(3, 7)
        else:  # mule_chain
            amount = round(rnd.uniform(7000, 35000), 2)
            timestamp = base_time - timedelta(seconds=rnd.randint(0, 300))
            is_new_beneficiary = True
            device_trust = rnd.uniform(0.2, 0.6)
            failed_auths = rnd.randint(1, 5)

    tx_id = uuid4()
    return PixTransaction(
        transaction_id=tx_id,
        end_to_end_id=f"E{tx_id.hex[:31].upper()}",
        payer_id=payer_id,
        payee_id=payee_id,
        payer_bank=rnd.choice(BANKS),
        payee_bank=rnd.choice(BANKS),
        amount=amount,
        city=city,
        state=state,
        timestamp=timestamp,
        pix_key_type=rnd.choice(PIX_KEYS),
        channel=rnd.choice(CHANNELS),
        device_id=f"dev_{payer_id}_{rnd.randint(1, 15)}",
        device_trust_score=round(device_trust, 3),
        is_new_beneficiary=is_new_beneficiary,
        failed_auth_count_24h=failed_auths,
        metadata={"synthetic_pattern": pattern, "synthetic_fraud": is_fraud, "stream_index": idx},
    )


def _force_night_time(base_time: datetime, rnd: random.Random) -> datetime:
    day = base_time.date()
    night_hour = rnd.choice([0, 1, 2, 3, 4, 5, 23])
    minute = rnd.randint(0, 59)
    second = rnd.randint(0, 59)
    candidate = datetime(day.year, day.month, day.day, night_hour, minute, second)
    if candidate > base_time:
        return candidate - timedelta(days=1)
    return candidate

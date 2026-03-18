from __future__ import annotations

import argparse
import asyncio

from src.pix.mock.generator import generate_pix_transactions
from src.pix.streaming.producer import pix_kafka_producer


async def run_simulation(tps: int, duration: int, fraud_ratio: float) -> None:
    total = tps * duration
    transactions = generate_pix_transactions(total_transactions=total, fraud_ratio=fraud_ratio, seed=123)

    await pix_kafka_producer.start()
    interval = 1.0 / tps

    for tx in transactions:
        await pix_kafka_producer.publish(tx)
        await asyncio.sleep(interval)

    await pix_kafka_producer.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PIX simulator producer")
    parser.add_argument("--tps", type=int, default=20)
    parser.add_argument("--duration", type=int, default=60)
    parser.add_argument("--fraud-ratio", type=float, default=0.1)
    args = parser.parse_args()

    asyncio.run(run_simulation(args.tps, args.duration, args.fraud_ratio))

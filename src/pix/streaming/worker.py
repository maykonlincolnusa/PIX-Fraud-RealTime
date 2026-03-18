from __future__ import annotations

import asyncio

from src.pix.streaming.consumer import kafka_consumer_runtime


async def main() -> None:
    await kafka_consumer_runtime.start()
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

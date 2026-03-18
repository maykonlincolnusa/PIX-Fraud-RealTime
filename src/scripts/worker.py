import asyncio

from src.pix.streaming.consumer import kafka_consumer_runtime


async def main() -> None:
    print("pix worker started")
    await kafka_consumer_runtime.start()
    try:
        while True:
            await asyncio.sleep(2)
    finally:
        await kafka_consumer_runtime.stop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("pix worker stopped")

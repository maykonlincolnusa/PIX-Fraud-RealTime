from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles

from src.Backend.api.alerts_api import router as alerts_router
from src.Backend.api.graph_api import router as graph_router
from src.Backend.api.investigation_service import router as investigations_router
from src.Backend.api.transactions_api import router as transactions_router
from src.Backend.routes_entities import router as entities_router
from src.Backend.websocket.realtime_stram import broadcaster
from src.core.settings import settings
from src.db.session import init_db
from src.pix.api.pix_routes import router as pix_router
from src.pix.mock.api import router as pix_mock_router
from src.pix.security.zero_trust import ZeroTrustMiddleware
from src.pix.services.metrics import pix_metrics
from src.pix.streaming.consumer import kafka_consumer_runtime
from src.pix.streaming.producer import pix_kafka_producer
from src.pix.ws.broadcaster import pix_broadcaster

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)
app.add_middleware(ZeroTrustMiddleware)

app.include_router(alerts_router, prefix=settings.API_PREFIX)
app.include_router(entities_router, prefix=settings.API_PREFIX)
app.include_router(graph_router, prefix=settings.API_PREFIX)
app.include_router(investigations_router, prefix=settings.API_PREFIX)
app.include_router(transactions_router, prefix=settings.API_PREFIX)
app.include_router(pix_router, prefix=settings.API_PREFIX)
app.include_router(pix_mock_router, prefix=f"{settings.API_PREFIX}/pix")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "version": settings.VERSION}


@app.on_event("startup")
async def startup() -> None:
    init_db()
    await pix_kafka_producer.start()
    await kafka_consumer_runtime.start()


@app.on_event("shutdown")
async def shutdown() -> None:
    await kafka_consumer_runtime.stop()
    await pix_kafka_producer.stop()


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.websocket("/ws/alerts")
async def alerts_ws(websocket: WebSocket) -> None:
    await broadcaster.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await broadcaster.disconnect(websocket)


@app.websocket("/ws/pix")
async def pix_ws(websocket: WebSocket) -> None:
    await pix_broadcaster.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await pix_broadcaster.disconnect(websocket)


@app.get("/metrics")
def metrics() -> Response:
    payload, content_type = pix_metrics.prometheus_payload()
    return Response(content=payload, media_type=content_type)

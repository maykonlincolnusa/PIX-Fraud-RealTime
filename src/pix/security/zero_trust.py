from __future__ import annotations

import hashlib
import hmac
from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from src.core.settings import settings


class ZeroTrustMiddleware(BaseHTTPMiddleware):
    """Zero-Trust basico: API key + service-id + assinatura opcional HMAC."""

    async def dispatch(self, request: Request, call_next: Callable):
        if not _is_protected_path(request.url.path):
            return await call_next(request)

        api_key = request.headers.get("x-api-key")
        service_id = request.headers.get("x-service-id")
        signature = request.headers.get("x-signature")

        if not api_key or api_key != settings.PIX_API_KEY:
            return JSONResponse({"detail": "invalid api key"}, status_code=401)

        if service_id not in settings.allowed_services():
            return JSONResponse({"detail": "service not allowed"}, status_code=403)

        if settings.ZERO_TRUST_REQUIRE_SIGNATURE:
            raw_body = await request.body()
            expected = _sign_body(raw_body, settings.ZERO_TRUST_HMAC_SECRET)
            if not signature or not hmac.compare_digest(signature, expected):
                return JSONResponse({"detail": "invalid signature"}, status_code=401)

        return await call_next(request)


def _is_protected_path(path: str) -> bool:
    return path.startswith("/api/v1/pix") and not path.startswith("/api/v1/pix/public")


def _sign_body(raw_body: bytes, secret: str) -> str:
    return hmac.new(secret.encode("utf-8"), raw_body, hashlib.sha256).hexdigest()

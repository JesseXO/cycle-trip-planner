from __future__ import annotations

import json
from typing import Any


SENSITIVE_KEYS = {
    "authorization",
    "x-api-key",
    "api_key",
    "apikey",
    "anthropic_api_key",
    "gemini_api_key",
}
REDACTED = "***REDACTED***"


def try_parse_json(raw: bytes) -> Any:
    if not raw:
        return None
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return None


def redact(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: REDACTED if str(k).lower() in SENSITIVE_KEYS else redact(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [redact(x) for x in obj]
    return obj

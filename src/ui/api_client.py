from __future__ import annotations

import requests

from src.ui.constants import CHAT_PATH, HEALTH_CHECK_TIMEOUT_S, HEALTH_PATH, REQUEST_TIMEOUT_S


def health(backend_url: str) -> dict | None:
    try:
        r = requests.get(f"{backend_url}{HEALTH_PATH}", timeout=HEALTH_CHECK_TIMEOUT_S)
    except Exception:
        return None
    return r.json() if r.status_code == 200 else None


def build_preferences(
    nationality: str,
    month: str,
    daily_km: int,
    lodging: str,
    hostel_every: int,
) -> dict:
    return {
        "nationality": nationality.strip() or None,
        "month": month or None,
        "daily_km": int(daily_km),
        "lodging_preference": lodging,
        "hostel_every_n_nights": int(hostel_every) if hostel_every else None,
    }


def send_message(
    backend_url: str,
    conversation_id: str | None,
    message: str,
    preferences: dict,
) -> dict:
    payload = {
        "conversation_id": conversation_id,
        "message": message,
        "preferences": preferences,
    }
    r = requests.post(f"{backend_url}{CHAT_PATH}", json=payload, timeout=REQUEST_TIMEOUT_S)
    r.raise_for_status()
    return r.json()

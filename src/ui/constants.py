from __future__ import annotations

import os


BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
CHAT_PATH = "/api/v1/chat"
HEALTH_PATH = "/health"
REQUEST_TIMEOUT_S = 300
HEALTH_CHECK_TIMEOUT_S = 3

MONTH_OPTIONS = ["", "March", "April", "May", "June", "July", "August", "September", "October"]
LODGING_OPTIONS = ["mixed", "camping", "hostel", "hotel"]

DAILY_KM_MIN = 40
DAILY_KM_MAX = 200
DAILY_KM_DEFAULT = 100
DAILY_KM_STEP = 10

HOSTEL_CADENCE_MIN = 0
HOSTEL_CADENCE_MAX = 14
HOSTEL_CADENCE_DEFAULT = 4

from __future__ import annotations

import os


BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
CHAT_PATH = "/api/v1/chat"
HEALTH_PATH = "/health"
REQUEST_TIMEOUT_S = 300

MONTH_OPTIONS = ["", "March", "April", "May", "June", "July", "August", "September", "October"]
LODGING_OPTIONS = ["mixed", "camping", "hostel", "hotel"]

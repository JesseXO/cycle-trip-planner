from __future__ import annotations

from src.api.models import TripPreferences
from src.tools.names import ToolName
from src.tools.registry import ToolRegistry


def fetch_route(preferences: TripPreferences, registry: ToolRegistry):
    return registry.dispatch(
        ToolName.GET_ROUTE,
        {
            "origin": preferences.origin,
            "destination": preferences.destination,
            "mode": "cycling",
        },
    )

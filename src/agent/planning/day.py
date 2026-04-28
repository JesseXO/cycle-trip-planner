from __future__ import annotations

from src.agent.planning.lodging import format_sleep_choice, lodging_kind_for_night
from src.agent.planning.segments import Segment
from src.api.models import DayPlan, TripPreferences
from src.config.settings import Settings
from src.tools.names import ToolName
from src.tools.registry import ToolRegistry


def build_day_plan(
    *,
    index: int,
    segment: Segment,
    preferences: TripPreferences,
    registry: ToolRegistry,
    settings: Settings,
) -> DayPlan:
    elevation = _fetch_elevation(segment, registry)
    weather = _fetch_weather(segment, preferences, registry)
    sleep = _fetch_sleep(index, segment, preferences, registry)
    highlights = _fetch_highlights(segment, registry, settings)

    return DayPlan(
        day=index,
        start=segment.start,
        end=segment.end,
        distance_km=segment.distance_km,
        elevation_gain_m=elevation.elevation_gain_m,
        difficulty=elevation.difficulty,
        weather_summary=f"{weather.summary} (avg {weather.avg_low_c}–{weather.avg_high_c}°C)",
        sleep=sleep,
        highlights=highlights,
    )


def _fetch_elevation(segment: Segment, registry: ToolRegistry):
    return registry.dispatch(
        ToolName.GET_ELEVATION_PROFILE,
        {
            "origin": segment.start,
            "destination": segment.end,
            "distance_km": segment.distance_km,
        },
    )


def _fetch_weather(segment: Segment, preferences: TripPreferences, registry: ToolRegistry):
    return registry.dispatch(
        ToolName.GET_WEATHER,
        {"location": segment.end, "month": preferences.month},
    )


def _fetch_sleep(
    index: int,
    segment: Segment,
    preferences: TripPreferences,
    registry: ToolRegistry,
) -> str:
    kind = lodging_kind_for_night(preferences, index)
    accommodation = registry.dispatch(
        ToolName.FIND_ACCOMMODATION,
        {"near": segment.end, "kind": kind},
    )
    return format_sleep_choice(accommodation)


def _fetch_highlights(segment: Segment, registry: ToolRegistry, settings: Settings) -> list[str]:
    limit = int(settings.plan_poi_per_day)
    pois = registry.dispatch(
        ToolName.GET_POINTS_OF_INTEREST,
        {"near": segment.end, "category": "any", "limit": limit},
    )
    return [p.name for p in getattr(pois, "items", [])][:limit]

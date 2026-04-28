from __future__ import annotations

from typing import Any, Literal

from src.api.models import TripPreferences


LodgingKind = Literal["camping", "hostel", "hotel", "any"]


def lodging_kind_for_night(preferences: TripPreferences, day: int) -> LodgingKind:
    if preferences.hostel_every_n_nights and day % preferences.hostel_every_n_nights == 0:
        return "hostel"
    if preferences.lodging_preference == "mixed":
        return "any"
    return preferences.lodging_preference


def format_sleep_choice(accommodation: Any) -> str:
    options = getattr(accommodation, "options", None) or []
    if not options:
        return "No accommodation options found."
    pick = options[0]
    return f"{pick.kind.title()}: {pick.name} (~€{pick.approx_price_eur})"

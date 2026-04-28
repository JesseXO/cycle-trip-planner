from __future__ import annotations

from typing import Literal

from src.api.models import TripPreferences


def lodging_kind_for_night(
    preferences: TripPreferences,
    day: int,
) -> Literal["camping", "hostel", "hotel", "any"]:
    if preferences.hostel_every_n_nights and day % preferences.hostel_every_n_nights == 0:
        return "hostel"
    if preferences.lodging_preference == "mixed":
        return "any"
    return preferences.lodging_preference

from __future__ import annotations

import hashlib
from typing import Literal

from pydantic import BaseModel, Field

from src.config.runtime import get_settings


class AccommodationOption(BaseModel):
    kind: Literal["camping", "hostel", "hotel"]
    name: str
    approx_price_eur: int
    distance_from_target_km: float


class FindAccommodationInput(BaseModel):
    near: str = Field(min_length=2, description="City or waypoint name")
    kind: Literal["camping", "hostel", "hotel", "any"] = "any"


class FindAccommodationOutput(BaseModel):
    near: str
    options: list[AccommodationOption]


def find_accommodation(inp: FindAccommodationInput) -> FindAccommodationOutput:
    s = get_settings()
    base = int(hashlib.sha256(inp.near.encode("utf-8")).hexdigest()[:8], 16) % s.mock_accommodation_seed_mod

    def opt(kind: str, idx: int, price: int) -> AccommodationOption:
        dist = round(((base + idx * s.mock_accommodation_dist_step) % s.mock_accommodation_dist_mod) / s.mock_accommodation_dist_scale, 1)
        return AccommodationOption(
            kind=kind, name=f"{inp.near} {kind.title()} {idx}", approx_price_eur=price, distance_from_target_km=dist
        )

    all_opts = [
        opt("camping", 1, s.mock_price_camping_base + (base % max(1, s.mock_price_camping_span))),
        opt("camping", 2, s.mock_price_camping_base + (base % max(1, s.mock_price_camping_span)) + 4),
        opt("hostel", 1, s.mock_price_hostel_base + (base % max(1, s.mock_price_hostel_span))),
        opt("hostel", 2, s.mock_price_hostel_base + (base % max(1, s.mock_price_hostel_span)) + 7),
        opt("hotel", 1, s.mock_price_hotel_base + (base % max(1, s.mock_price_hotel_span))),
        opt("hotel", 2, s.mock_price_hotel_base + (base % max(1, s.mock_price_hotel_span)) + 25),
    ]

    if inp.kind == "any":
        options = all_opts
    else:
        options = [o for o in all_opts if o.kind == inp.kind]

    return FindAccommodationOutput(near=inp.near, options=options)


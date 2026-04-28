from __future__ import annotations

import hashlib
from typing import Literal

from pydantic import BaseModel, Field

from src.config.runtime import get_settings


class GetElevationProfileInput(BaseModel):
    origin: str = Field(min_length=2)
    destination: str = Field(min_length=2)
    distance_km: float = Field(gt=0)


class GetElevationProfileOutput(BaseModel):
    origin: str
    destination: str
    elevation_gain_m: int
    difficulty: Literal["easy", "moderate", "hard"]


def get_elevation_profile(inp: GetElevationProfileInput) -> GetElevationProfileOutput:
    s = get_settings()
    h = int(hashlib.sha256(f"{inp.origin}->{inp.destination}".encode("utf-8")).hexdigest()[:8], 16)
    gain = int((h % s.mock_elev_hash_mod_m) + inp.distance_km * float(s.mock_elev_gain_per_km))
    if gain < s.mock_elev_easy_max_m:
        difficulty = "easy"
    elif gain < s.mock_elev_moderate_max_m:
        difficulty = "moderate"
    else:
        difficulty = "hard"
    return GetElevationProfileOutput(
        origin=inp.origin,
        destination=inp.destination,
        elevation_gain_m=gain,
        difficulty=difficulty,
    )


from __future__ import annotations

from pydantic import BaseModel, Field


class ElevationMockSettings(BaseModel):
    mock_elev_hash_mod_m: int = Field(default=1800, ge=1, le=100000, alias="MOCK_ELEV_HASH_MOD_M")
    mock_elev_gain_per_km: float = Field(default=4.0, ge=0, alias="MOCK_ELEV_GAIN_PER_KM")
    mock_elev_easy_max_m: int = Field(default=900, ge=0, alias="MOCK_ELEV_EASY_MAX_M")
    mock_elev_moderate_max_m: int = Field(default=1800, ge=0, alias="MOCK_ELEV_MODERATE_MAX_M")

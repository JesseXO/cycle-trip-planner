from __future__ import annotations

from pydantic import BaseModel, Field


class VisaMockSettings(BaseModel):
    mock_visa_schengen_countries: list[str] = Field(
        default_factory=lambda: ["netherlands", "denmark", "germany", "belgium", "france", "sweden", "norway"],
        alias="MOCK_VISA_SCHENGEN_COUNTRIES",
    )
    mock_visa_max_days_no_visa: int = Field(default=90, ge=1, le=365, alias="MOCK_VISA_MAX_DAYS_NO_VISA")

from __future__ import annotations

import hashlib
from pydantic import BaseModel, Field

from src.config.runtime import get_settings


class GetWeatherInput(BaseModel):
    location: str = Field(min_length=2)
    month: str = Field(min_length=3, description="Month name like 'June'")


class GetWeatherOutput(BaseModel):
    location: str
    month: str
    avg_high_c: int
    avg_low_c: int
    rainfall_mm: int
    summary: str


def get_weather(inp: GetWeatherInput) -> GetWeatherOutput:
    s = get_settings()
    h = int(hashlib.sha256(f"{inp.location}|{inp.month}".encode("utf-8")).hexdigest()[:8], 16)
    avg_high = s.mock_weather_high_base_c + (h % max(1, s.mock_weather_high_span_c))
    avg_low = avg_high - (s.mock_weather_low_delta_base_c + (h % max(1, s.mock_weather_low_delta_span_c)))
    rain = s.mock_weather_rain_base_mm + (h % max(1, s.mock_weather_rain_span_mm))
    summary = f"Typical {inp.month} weather: mild to warm, with a chance of rain."
    return GetWeatherOutput(
        location=inp.location,
        month=inp.month,
        avg_high_c=avg_high,
        avg_low_c=avg_low,
        rainfall_mm=rain,
        summary=summary,
    )


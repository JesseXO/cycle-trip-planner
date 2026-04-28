from __future__ import annotations

from pydantic import BaseModel, Field


class WeatherMockSettings(BaseModel):
    mock_weather_high_base_c: int = Field(default=16, ge=-50, le=60, alias="MOCK_WEATHER_HIGH_BASE_C")
    mock_weather_high_span_c: int = Field(default=12, ge=0, le=60, alias="MOCK_WEATHER_HIGH_SPAN_C")
    mock_weather_low_delta_base_c: int = Field(default=6, ge=0, le=40, alias="MOCK_WEATHER_LOW_DELTA_BASE_C")
    mock_weather_low_delta_span_c: int = Field(default=3, ge=0, le=40, alias="MOCK_WEATHER_LOW_DELTA_SPAN_C")
    mock_weather_rain_base_mm: int = Field(default=35, ge=0, le=1000, alias="MOCK_WEATHER_RAIN_BASE_MM")
    mock_weather_rain_span_mm: int = Field(default=70, ge=0, le=1000, alias="MOCK_WEATHER_RAIN_SPAN_MM")

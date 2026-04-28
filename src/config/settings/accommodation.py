from __future__ import annotations

from pydantic import BaseModel, Field


class AccommodationMockSettings(BaseModel):
    mock_accommodation_seed_mod: int = Field(default=100, ge=10, le=10000, alias="MOCK_ACCOMMODATION_SEED_MOD")
    mock_accommodation_dist_mod: int = Field(default=40, ge=1, le=1000, alias="MOCK_ACCOMMODATION_DIST_MOD")
    mock_accommodation_dist_scale: float = Field(default=10.0, gt=0, alias="MOCK_ACCOMMODATION_DIST_SCALE")
    mock_accommodation_dist_step: int = Field(default=7, ge=1, le=100, alias="MOCK_ACCOMMODATION_DIST_STEP")

    mock_price_camping_base: int = Field(default=18, ge=0, alias="MOCK_PRICE_CAMPING_BASE")
    mock_price_camping_span: int = Field(default=12, ge=0, alias="MOCK_PRICE_CAMPING_SPAN")
    mock_price_camping_premium: int = Field(default=4, ge=0, alias="MOCK_PRICE_CAMPING_PREMIUM")
    mock_price_hostel_base: int = Field(default=35, ge=0, alias="MOCK_PRICE_HOSTEL_BASE")
    mock_price_hostel_span: int = Field(default=20, ge=0, alias="MOCK_PRICE_HOSTEL_SPAN")
    mock_price_hostel_premium: int = Field(default=7, ge=0, alias="MOCK_PRICE_HOSTEL_PREMIUM")
    mock_price_hotel_base: int = Field(default=85, ge=0, alias="MOCK_PRICE_HOTEL_BASE")
    mock_price_hotel_span: int = Field(default=40, ge=0, alias="MOCK_PRICE_HOTEL_SPAN")
    mock_price_hotel_premium: int = Field(default=25, ge=0, alias="MOCK_PRICE_HOTEL_PREMIUM")

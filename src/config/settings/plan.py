from __future__ import annotations

from pydantic import BaseModel, Field


class PlanSettings(BaseModel):
    plan_poi_per_day: int = Field(default=4, ge=0, le=20, alias="PLAN_POI_PER_DAY")
    plan_food_style: str = Field(default="balanced", alias="PLAN_FOOD_STYLE")

from __future__ import annotations

from pydantic import BaseModel, Field


class BudgetMockSettings(BaseModel):
    mock_budget_lodging_camping: int = Field(default=18, ge=0, alias="MOCK_BUDGET_LODGING_CAMPING")
    mock_budget_lodging_hostel: int = Field(default=40, ge=0, alias="MOCK_BUDGET_LODGING_HOSTEL")
    mock_budget_lodging_hotel: int = Field(default=100, ge=0, alias="MOCK_BUDGET_LODGING_HOTEL")
    mock_budget_lodging_mixed: int = Field(default=45, ge=0, alias="MOCK_BUDGET_LODGING_MIXED")
    mock_budget_food_budget: int = Field(default=18, ge=0, alias="MOCK_BUDGET_FOOD_BUDGET")
    mock_budget_food_balanced: int = Field(default=28, ge=0, alias="MOCK_BUDGET_FOOD_BALANCED")
    mock_budget_food_treats: int = Field(default=40, ge=0, alias="MOCK_BUDGET_FOOD_TREATS")
    mock_budget_variable_per_km: float = Field(default=0.12, ge=0, alias="MOCK_BUDGET_VARIABLE_PER_KM")
    mock_budget_misc_per_day: int = Field(default=8, ge=0, alias="MOCK_BUDGET_MISC_PER_DAY")
    mock_budget_currency: str = Field(default="EUR", alias="MOCK_BUDGET_CURRENCY")

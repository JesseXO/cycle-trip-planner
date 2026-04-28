from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict

from src.config.settings.accommodation import AccommodationMockSettings
from src.config.settings.budget import BudgetMockSettings
from src.config.settings.core import CoreSettings, LLMProviderName
from src.config.settings.elevation import ElevationMockSettings
from src.config.settings.plan import PlanSettings
from src.config.settings.poi import POIMockSettings
from src.config.settings.route import RouteMockSettings
from src.config.settings.visa import VisaMockSettings
from src.config.settings.weather import WeatherMockSettings


class Settings(
    BaseSettings,
    CoreSettings,
    RouteMockSettings,
    AccommodationMockSettings,
    WeatherMockSettings,
    ElevationMockSettings,
    POIMockSettings,
    BudgetMockSettings,
    VisaMockSettings,
    PlanSettings,
):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


__all__ = ["LLMProviderName", "Settings"]

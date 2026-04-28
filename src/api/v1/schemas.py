from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from src.api.models import TripPreferences


class ChatV1Request(BaseModel):
    conversation_id: str | None = None
    message: str = Field(min_length=1)
    preferences: TripPreferences | None = None


class ToolCallView(BaseModel):
    name: str
    input: dict[str, Any]
    output: dict[str, Any] | None = None
    is_error: bool = False


class ChatV1Response(BaseModel):
    conversation_id: str
    reply: str
    tool_calls: list[ToolCallView] = Field(default_factory=list)
    rounds: int = 0
    truncated: bool = False
    error: str | None = None

from fastapi.testclient import TestClient

from src.agent.providers.base import StopReason
from src.agent.providers.mock_provider import MockProvider, MockResponse, text_block
from src.agent.v1 import AgentOrchestrator
from src.api.app import app
from src.api.models import ConversationState, TripPreferences
from src.config.settings import Settings
from src.tools.builtins import build_registry


def test_conversation_continuity_same_id():
    client = TestClient(app)
    r1 = client.post("/api/v1/chat", json={"message": "First message"})
    cid = r1.json()["conversation_id"]

    r2 = client.post("/api/v1/chat", json={"conversation_id": cid, "message": "Second message"})
    assert r2.status_code == 200
    assert r2.json()["conversation_id"] == cid


def test_preference_change_reframes_user_message_for_provider():
    captured: list[list[dict]] = []

    def _capture(messages):
        captured.append([{"role": m["role"], "content": m["content"]} for m in messages])

    provider = MockProvider(
        responses=[
            MockResponse(content=[text_block("ack 1")], stop_reason=StopReason.END_TURN),
            MockResponse(content=[text_block("ack 2")], stop_reason=StopReason.END_TURN),
        ],
        on_call=_capture,
    )
    settings = Settings()
    orchestrator = AgentOrchestrator(settings=settings, provider=provider, registry=build_registry())

    state = ConversationState(conversation_id="test-cid")

    _, state_after_first = orchestrator.handle_turn(
        state=state,
        user_message="Plan it",
        preferences_override=TripPreferences(daily_km=80, lodging_preference="camping"),
    )

    _, state_after_second = orchestrator.handle_turn(
        state=state_after_first,
        user_message="Make it harder",
        preferences_override=TripPreferences(daily_km=140),
    )

    first_user_msg = captured[0][-1]["content"]
    second_user_msg = captured[1][-1]["content"]

    assert "daily_km: 80" in first_user_msg
    assert "lodging_preference: camping" in first_user_msg

    assert "daily_km: 140" in second_user_msg
    assert "lodging_preference: camping" in second_user_msg
    assert "daily_km: 80" not in second_user_msg

    assert state_after_second.preferences.daily_km == 140
    assert state_after_second.preferences.lodging_preference == "camping"


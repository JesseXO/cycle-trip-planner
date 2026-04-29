from src.api.middleware.redaction import REDACTED, redact


def test_redact_masks_known_sensitive_keys():
    payload = {
        "Authorization": "Bearer xxx",
        "ANTHROPIC_API_KEY": "sk-...",
        "X-Api-Key": "abcd",
        "password": "p4ss",
        "secret_token": "s3cret",
        "user": {"refresh_token": "rrr", "name": "Omar"},
        "list_field": [{"access_token": "tok"}, {"safe_field": "ok"}],
    }
    out = redact(payload)
    assert out["Authorization"] == REDACTED
    assert out["ANTHROPIC_API_KEY"] == REDACTED
    assert out["X-Api-Key"] == REDACTED
    assert out["password"] == REDACTED
    assert out["secret_token"] == REDACTED
    assert out["user"]["refresh_token"] == REDACTED
    assert out["user"]["name"] == "Omar"
    assert out["list_field"][0]["access_token"] == REDACTED
    assert out["list_field"][1]["safe_field"] == "ok"


def test_redact_leaves_non_sensitive_payload_unchanged():
    payload = {
        "conversation_id": "abc",
        "message": "Plan a trip",
        "preferences": {"daily_km": 100, "lodging_preference": "camping"},
        "tool_calls": [{"name": "get_route", "is_error": False}],
    }
    assert redact(payload) == payload

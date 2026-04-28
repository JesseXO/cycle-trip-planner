import os

import pytest


def pytest_configure(config):
    os.environ["LLM_PROVIDER"] = "mock"
    os.environ["LLM_MODEL"] = "mock-model"
    os.environ["INCLUDE_STRUCTURED_PLAN"] = "true"


@pytest.fixture(autouse=True)
def _force_mock_provider_env(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    monkeypatch.setenv("LLM_MODEL", "mock-model")
    monkeypatch.setenv("INCLUDE_STRUCTURED_PLAN", "true")
    yield


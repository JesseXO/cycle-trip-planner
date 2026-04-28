from __future__ import annotations

from fastapi import APIRouter, Depends

from src.agent.runtime import Runtime
from src.api.deps import get_runtime
from src.config.version import get_version


router = APIRouter(tags=["meta"])


@router.get("/health")
def health(rt: Runtime = Depends(get_runtime)) -> dict:
    return {
        "status": "ok",
        "api": rt.settings.api_title,
        "version": get_version(),
        "provider": rt.settings.llm_provider.value,
        "model": rt.settings.llm_model,
    }

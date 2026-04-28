from __future__ import annotations

from fastapi import APIRouter, Depends

from src.agent.runtime import Runtime
from src.api.deps import get_runtime
from src.api.schemas import ChatRequest, ChatResponse


router = APIRouter(tags=["v0"])


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, rt: Runtime = Depends(get_runtime)) -> ChatResponse:
    state = rt.store.get_or_create(req.conversation_id)
    reply, updated = rt.orchestrator_v0.handle_turn(
        state=state,
        user_message=req.message,
        preferences_override=req.preferences,
    )
    rt.store.save(updated)
    return ChatResponse(conversation_id=updated.conversation_id, reply=reply)

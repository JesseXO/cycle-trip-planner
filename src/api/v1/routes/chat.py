from __future__ import annotations

from fastapi import APIRouter, Depends

from src.agent.runtime import Runtime
from src.api.v1.dependencies import get_runtime
from src.api.v1.schemas import ChatV1Request, ChatV1Response, ToolCallView


router = APIRouter(tags=["v1"])


@router.post("/chat", response_model=ChatV1Response)
def chat(req: ChatV1Request, rt: Runtime = Depends(get_runtime)) -> ChatV1Response:
    state = rt.store.get_or_create(req.conversation_id)
    result, updated = rt.orchestrator_v1.handle_turn(
        state=state,
        user_message=req.message,
        preferences_override=req.preferences,
    )
    rt.store.save(updated)

    tool_calls = [
        ToolCallView(name=t.name, input=t.input, output=t.output, is_error=t.is_error)
        for t in result.tool_calls
    ]
    return ChatV1Response(
        conversation_id=updated.conversation_id,
        reply=result.reply,
        tool_calls=tool_calls,
        rounds=result.rounds,
        truncated=result.truncated,
        error=result.error,
    )

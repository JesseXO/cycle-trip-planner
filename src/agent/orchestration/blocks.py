from __future__ import annotations

from typing import Any


def block_attr(block: Any, key: str) -> Any:
    if isinstance(block, dict):
        return block.get(key)
    return getattr(block, key, None)


def extract_text(content: list[Any]) -> str:
    parts: list[str] = []
    for block in content:
        if block_attr(block, "type") == "text":
            text = block_attr(block, "text") or ""
            if text:
                parts.append(text)
    return "\n".join(parts).strip()


def extract_tool_uses(content: list[Any]) -> list[Any]:
    return [b for b in content if block_attr(b, "type") == "tool_use"]


def normalize_assistant_content(content: list[Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for b in content:
        btype = block_attr(b, "type")
        if btype == "text":
            out.append({"type": "text", "text": block_attr(b, "text") or ""})
        elif btype == "tool_use":
            out.append(
                {
                    "type": "tool_use",
                    "id": block_attr(b, "id"),
                    "name": block_attr(b, "name"),
                    "input": block_attr(b, "input") or {},
                }
            )
    return out

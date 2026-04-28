from __future__ import annotations

import streamlit as st

from src.ui import tool_calls


def render_history() -> None:
    for turn_idx, msg in enumerate(st.session_state.messages):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant" and turn_idx < len(st.session_state.tool_calls_per_turn):
                entry = st.session_state.tool_calls_per_turn[turn_idx]
                tool_calls.render(entry["tool_calls"], entry["rounds"])


def render_empty_state() -> None:
    if st.session_state.messages:
        return
    with st.container(border=True):
        st.markdown(
            "**Try this:**  \n"
            "_I want to cycle from Amsterdam to Copenhagen, ~100 km/day, prefer camping but a "
            "hostel every 4th night, traveling in June._"
        )


def render_header() -> None:
    st.markdown("# 🚴 Cycling Trip Planner Agent")
    st.caption(
        "Plan a multi-day bike trip via chat. The agent calls real tools — route, elevation, weather, "
        "accommodation, POIs, budget, visa — and adapts when you change your preferences."
    )

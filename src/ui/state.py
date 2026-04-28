from __future__ import annotations

import uuid

import streamlit as st


def init() -> None:
    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "tool_calls_per_turn" not in st.session_state:
        st.session_state.tool_calls_per_turn = []
    if "session_key" not in st.session_state:
        st.session_state.session_key = uuid.uuid4().hex


def reset() -> None:
    st.session_state.conversation_id = None
    st.session_state.messages = []
    st.session_state.tool_calls_per_turn = []
    st.session_state.session_key = uuid.uuid4().hex


def append_user(message: str) -> None:
    st.session_state.messages.append({"role": "user", "content": message})
    st.session_state.tool_calls_per_turn.append({"tool_calls": [], "rounds": 0})


def append_assistant(reply: str, tool_calls: list[dict], rounds: int) -> None:
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.tool_calls_per_turn.append({"tool_calls": tool_calls, "rounds": rounds})

from __future__ import annotations

import streamlit as st


def render(tool_calls: list[dict], rounds: int) -> None:
    if not tool_calls:
        return

    n = len(tool_calls)
    plural_calls = "" if n == 1 else "s"
    plural_rounds = "" if rounds == 1 else "s"
    label = f"🔧 Agent steps — {n} tool call{plural_calls} across {rounds} round{plural_rounds}"

    with st.expander(label, expanded=False):
        for i, call in enumerate(tool_calls, 1):
            err = " ⚠️" if call.get("is_error") else ""
            st.markdown(f"**{i}. `{call['name']}`{err}**")

            cols = st.columns(2)
            with cols[0]:
                st.caption("input")
                st.json(call.get("input") or {}, expanded=False)
            with cols[1]:
                st.caption("output")
                if call.get("output") is None:
                    st.error("tool failed")
                else:
                    st.json(call["output"], expanded=False)

from __future__ import annotations

from dataclasses import dataclass

import streamlit as st

from src.ui import state
from src.ui.api_client import health
from src.ui.constants import (
    BACKEND_URL,
    DAILY_KM_DEFAULT,
    DAILY_KM_MAX,
    DAILY_KM_MIN,
    DAILY_KM_STEP,
    HOSTEL_CADENCE_DEFAULT,
    HOSTEL_CADENCE_MAX,
    HOSTEL_CADENCE_MIN,
    LODGING_OPTIONS,
    MONTH_OPTIONS,
)


@dataclass
class SidebarValues:
    nationality: str
    month: str
    daily_km: int
    lodging: str
    hostel_every: int


CHAT_MODES = ("Chat only", "Chat with filters")


def render() -> SidebarValues:
    prefs = st.session_state.prefs

    with st.sidebar:
        st.markdown("### 🚴 Trip Planner")

        info = health(BACKEND_URL)
        if info:
            st.success(f"Backend online · {info['provider']}/{info['model']}", icon="✅")
        else:
            st.error(f"Backend unreachable at {BACKEND_URL}", icon="🔌")
            st.caption("Start with `./scripts/backend.sh`")

        st.divider()
        st.radio(
            "Mode",
            CHAT_MODES,
            key="chat_mode",
            help="Chat only sends just your message. Chat with filters also sends the saved preferences below.",
        )

        if st.session_state.chat_mode == "Chat with filters":
            st.divider()
            st.markdown("**Filters**")
            prefs["month"] = st.selectbox(
                "Travel month",
                MONTH_OPTIONS,
                index=MONTH_OPTIONS.index(prefs["month"]) if prefs["month"] in MONTH_OPTIONS else 4,
            )
            prefs["daily_km"] = int(
                st.slider(
                    "Daily km target",
                    min_value=DAILY_KM_MIN,
                    max_value=DAILY_KM_MAX,
                    value=int(prefs["daily_km"]),
                    step=DAILY_KM_STEP,
                )
            )
            prefs["lodging"] = st.selectbox(
                "Lodging style",
                LODGING_OPTIONS,
                index=LODGING_OPTIONS.index(prefs["lodging"]) if prefs["lodging"] in LODGING_OPTIONS else 0,
            )
            prefs["hostel_every"] = int(
                st.number_input(
                    "Hostel cadence (every N nights, 0 = off)",
                    min_value=HOSTEL_CADENCE_MIN,
                    max_value=HOSTEL_CADENCE_MAX,
                    value=int(prefs["hostel_every"]),
                    step=1,
                )
            )
            prefs["nationality"] = st.text_input(
                "Nationality (for visa note, optional)", value=prefs["nationality"]
            )

        st.divider()
        st.button("🗑️ New conversation", on_click=state.reset, use_container_width=True)

    return SidebarValues(
        nationality=prefs["nationality"],
        month=prefs["month"],
        daily_km=int(prefs["daily_km"]),
        lodging=prefs["lodging"],
        hostel_every=int(prefs["hostel_every"]),
    )

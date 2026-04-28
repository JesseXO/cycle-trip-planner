from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Segment:
    start: str
    end: str
    distance_km: float


def split_into_daily_segments(
    origin: str,
    destination: str,
    total_distance_km: float,
    daily_km: int,
    *,
    min_days: int,
    distance_decimals: int,
) -> list[Segment]:
    days = max(min_days, round(total_distance_km / max(1, daily_km)))

    base = total_distance_km / days
    segments: list[Segment] = []
    prev = origin
    for i in range(1, days + 1):
        nxt = destination if i == days else f"Day{i}_Stop"
        segments.append(Segment(start=prev, end=nxt, distance_km=round(base, distance_decimals)))
        prev = nxt
    return segments

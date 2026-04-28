from __future__ import annotations

import tomllib
from functools import lru_cache
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


PACKAGE_NAME = "cycling-trip-planner-agent"
FALLBACK_VERSION = "0.0.0"


@lru_cache(maxsize=1)
def get_version() -> str:
    try:
        return version(PACKAGE_NAME)
    except PackageNotFoundError:
        return _read_pyproject_version()


def _read_pyproject_version() -> str:
    pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
    if not pyproject.exists():
        return FALLBACK_VERSION
    try:
        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        return data["project"]["version"]
    except (KeyError, tomllib.TOMLDecodeError):
        return FALLBACK_VERSION

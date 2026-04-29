#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON_MIN="3.11"
VENV_DIR=".venv"

log()  { printf "\033[1;34m[install]\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m[install]\033[0m %s\n" "$*" >&2; }
fail() { printf "\033[1;31m[install]\033[0m %s\n" "$*" >&2; exit 1; }

find_python() {
  for candidate in python3.13 python3.12 python3.11 python3 python; do
    if command -v "$candidate" >/dev/null 2>&1; then
      if "$candidate" -c "import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
        echo "$candidate"
        return 0
      fi
    fi
  done
  return 1
}

PYTHON_BIN="$(find_python || true)"
if [ -z "${PYTHON_BIN:-}" ]; then
  fail "Python ${PYTHON_MIN}+ is required but was not found on PATH."
fi
log "Using $($PYTHON_BIN --version) at $(command -v "$PYTHON_BIN")"

venv_python_ok() {
  [ -x "$VENV_DIR/bin/python" ] && \
    "$VENV_DIR/bin/python" -c "import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null
}

if [ -d "$VENV_DIR" ] && ! venv_python_ok; then
  warn "Existing $VENV_DIR uses an unsupported Python ($("$VENV_DIR/bin/python" --version 2>&1 || echo unknown)); recreating"
  rm -rf "$VENV_DIR"
fi

if [ ! -d "$VENV_DIR" ]; then
  log "Creating virtual environment at $VENV_DIR"
  "$PYTHON_BIN" -m venv "$VENV_DIR"
else
  log "Virtual environment already exists at $VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

log "Upgrading pip"
python -m pip install --upgrade pip >/dev/null

if [ -f "pyproject.toml" ]; then
  log "Installing project + dev extras from pyproject.toml"
  python -m pip install -e ".[dev]"
elif [ -f "requirements.txt" ]; then
  log "Installing requirements.txt"
  python -m pip install -r requirements.txt
else
  fail "No pyproject.toml or requirements.txt found."
fi

if [ ! -f ".env" ]; then
  if [ -f ".env.example" ]; then
    cp .env.example .env
    log "Created .env from .env.example — fill in ANTHROPIC_API_KEY before running"
  else
    warn "No .env.example found; skipping .env bootstrap"
  fi
else
  log ".env already exists; leaving it untouched"
fi

if [ -d ".githooks" ] && [ -d ".git" ]; then
  current_hooks_path="$(git config --get core.hooksPath || true)"
  if [ "$current_hooks_path" != ".githooks" ]; then
    git config core.hooksPath .githooks
    log "Wired git hooks via core.hooksPath=.githooks"
  else
    log "Git hooks already pointed at .githooks"
  fi
fi

log "Done. Run ./scripts/dev.sh to start the FastAPI + Streamlit stack."

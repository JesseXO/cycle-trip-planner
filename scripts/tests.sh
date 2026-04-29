#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
source .venv/bin/activate

if [[ "${1:-}" == "--live" ]]; then
  shift
  export RUN_LIVE_LLM=1
  exec pytest -m live "$@"
fi

exec pytest "$@"

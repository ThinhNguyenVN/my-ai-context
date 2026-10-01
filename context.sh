#!/bin/sh
# Resolve the checkout from this script, regardless of the current directory.
set -eu
TASK_CONTEXT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if ! command -v python3 >/dev/null 2>&1; then
    echo "Cần Python 3.9+ để chạy my-ai-context." >&2
    exit 1
fi
if ! python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)'; then
    echo "Cần Python 3.9+; python3 hiện tại quá cũ." >&2
    exit 1
fi
if [ "$#" -eq 0 ]; then
    set -- status
fi
exec python3 "$TASK_CONTEXT_DIR/bin/context" "$@"

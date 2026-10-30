#!/bin/bash
# Run Brave inside a Firejail sandbox.
#
# Firejail is the whole point of this script: it starts Brave with a
# private home view and the default browser profile restrictions, so a
# compromised page gets the sandbox's filesystem, not yours. That only
# holds while Brave is launched through Firejail, which is why this
# script checks for both binaries first: falling back to a bare `brave`
# when Firejail is missing would silently drop the protection the script
# exists to provide.
set -u

if ! command -v firejail >/dev/null 2>&1; then
    echo "error: firejail is not installed, so Brave would run unsandboxed. Install firejail first." >&2
    exit 1
fi
if ! command -v brave >/dev/null 2>&1; then
    echo "error: brave is not installed (or not on PATH)." >&2
    exit 1
fi

# "$@" forwards any flags the caller passed (for example a URL to open)
# to Brave, inside the sandbox. exec replaces this shell with Firejail so
# signals and the exit code are Brave's own.
exec firejail brave "$@"

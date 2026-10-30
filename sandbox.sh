#!/bin/bash
# I run Brave inside a Firejail sandbox, and I wrote this script because
# a plain brave launch gives a compromised page my real home directory.
# Firejail starts Brave with a private home view and the default browser
# profile restrictions, so the page gets the sandbox filesystem instead.
# That protection only exists on this launch path. If I started Brave any
# other way from here, nothing in the output would warn me it was gone.
#
# I check firejail before I check brave, on purpose. A missing brave is
# just a missing program. A missing firejail is the failure that matters,
# because it is the one I could be tempted to work around by launching
# Brave bare. I do not do that. I stop and say what is missing.
#
# I set -u so a future edit that reads a variable nobody set fails loudly
# here, instead of expanding to an empty string and quietly changing what
# gets launched.
set -u

# I test with command -v because it searches PATH the same way this shell
# will when it launches the names below, so my check matches the launch.
# I hide its output because the path it prints adds nothing next to my own
# error, and I send that error to stderr so it never mixes into output a
# caller captured from stdout.
if ! command -v firejail >/dev/null 2>&1; then
    echo "error: firejail is not installed, so Brave would run unsandboxed. Install firejail first." >&2
    exit 1
fi
if ! command -v brave >/dev/null 2>&1; then
    echo "error: brave is not installed (or not on PATH)." >&2
    exit 1
fi

# I hand "$@" to Brave inside the sandbox, so a URL or flag I pass here
# opens in the sandboxed browser directly. The quotes matter: an argument
# with spaces in it stays one argument. I use exec so this shell gets
# replaced by firejail instead of sitting between firejail and the
# terminal. Signals such as Ctrl-C and the final exit code then belong to
# the browser run itself, and no wrapper shell stays alive after Brave
# closes.
exec firejail brave "$@"

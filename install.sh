#!/usr/bin/env bash
set -euo pipefail

app='text-analyzer'
raw_url="https://raw.githubusercontent.com/seetaayeesh/$app/main"

install_app() {
    if ! command -v python3 >/dev/null ||
       ! python3 -c 'import sys; sys.exit(sys.version_info < (3, 8))'; then
        printf '%s\n' 'Python 3.8 or later is required.' >&2
        exit 1
    fi

    if ! command -v curl >/dev/null; then
        printf '%s\n' 'curl is required.' >&2
        exit 1
    fi

    bin_dir="$HOME/.local/bin"
    mkdir -p -- "$bin_dir"
    staged_file=$(mktemp "$bin_dir/.$app.XXXXXX")
    trap 'rm -f -- "$staged_file"' EXIT

    # Keep the MIT notice with the standalone Python executable.
    {
        printf '%s\n' '#!/usr/bin/env python3'
        curl -fsSL "$raw_url/LICENSE" | sed 's/^/# /'
        printf '\n'
        curl -fsSL "$raw_url/main.py"
    } > "$staged_file"

    python3 -c 'import sys; path = sys.argv[1]; compile(open(path, "rb").read(), path, "exec")' "$staged_file"

    # Replace an existing installation only after the new copy is ready.
    chmod 0755 -- "$staged_file"
    mv -fT -- "$staged_file" "$bin_dir/$app"
    trap - EXIT
    printf 'Installed. Run: %s\n' "$bin_dir/$app"
}

install_app

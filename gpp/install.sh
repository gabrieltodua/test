#!/bin/bash
# ═══════════════════════════════════════════════════════════
#  G++ Language Installer  —  macOS / Linux
#  One-line install:
#    curl -fsSL https://raw.githubusercontent.com/USERNAME/REPO/main/install.sh | bash
# ═══════════════════════════════════════════════════════════

set -e

# ════════════════════════════════════════════════════════════════════
#  ▼▼▼  CHANGE THIS ONE LINE to your GitHub repo raw base URL  ▼▼▼
GITHUB_RAW="https://raw.githubusercontent.com/gabrieltodua/test/main/gpp"
#  ▲▲▲  Example: "https://raw.githubusercontent.com/john/gpp/main"  ▲▲▲
# ════════════════════════════════════════════════════════════════════

RESET='\033[0m'
BOLD='\033[1m'
DIM='\033[2m'
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'

echo ""
echo -e "${CYAN}${BOLD}  ╔══════════════════════════════════════╗"
echo -e "  ║     G++ Language — Installer v2.0   ║"
echo -e "  ╚══════════════════════════════════════╝${RESET}"
echo ""

# ── Permanent install locations ─────────────────────────────────────────────
GPP_HOME="$HOME/.gpp"
GPP_PY="$GPP_HOME/gpp.py"
EXT_DEST="$HOME/.vscode/extensions/gpp-language-1.0.0"

# ── Step 1: Check Python 3 ───────────────────────────────────────────────────
echo -e "  ${DIM}[1/5] Checking Python 3...${RESET}"

if ! command -v python3 &>/dev/null; then
    echo -e "  ${RED}✗  Python 3 is not installed.${RESET}"
    echo -e "     Download from: ${YELLOW}https://www.python.org/downloads/${RESET}"
    exit 1
fi

PY_VER=$(python3 --version 2>&1)
echo -e "  ${GREEN}✓${RESET}  Found ${PY_VER}"

# ── Step 2: Check curl ───────────────────────────────────────────────────────
echo ""
echo -e "  ${DIM}[2/5] Checking curl...${RESET}"

if ! command -v curl &>/dev/null; then
    echo -e "  ${RED}✗  curl is not installed.${RESET}"
    echo -e "     Install via Homebrew: ${YELLOW}brew install curl${RESET}"
    exit 1
fi

echo -e "  ${GREEN}✓${RESET}  curl is available"

# ── Step 3: Download gpp.py to permanent home ────────────────────────────────
echo ""
echo -e "  ${DIM}[3/5] Installing G++ interpreter...${RESET}"

mkdir -p "$GPP_HOME"

if curl -fsSL "$GITHUB_RAW/gpp.py" -o "$GPP_PY"; then
    chmod +x "$GPP_PY"
    echo -e "  ${GREEN}✓${RESET}  Interpreter saved to: ${DIM}$GPP_PY${RESET}"
else
    echo -e "  ${RED}✗  Failed to download gpp.py — check GITHUB_RAW URL or internet.${RESET}"
    exit 1
fi

# ── Step 4: Install the 'gpp' command ────────────────────────────────────────
echo ""
echo -e "  ${DIM}[4/5] Installing 'gpp' command...${RESET}"

LAUNCHER_CONTENT="#!/bin/bash
exec python3 \"$GPP_PY\" \"\$@\""

# Try /usr/local/bin first (may need sudo), fall back to ~/bin
if echo "$LAUNCHER_CONTENT" | sudo tee /usr/local/bin/gpp > /dev/null 2>&1 \
   && sudo chmod +x /usr/local/bin/gpp; then
    echo -e "  ${GREEN}✓${RESET}  Command installed: ${DIM}/usr/local/bin/gpp${RESET}"
    echo -e "     ${DIM}(works system-wide, no PATH changes needed)${RESET}"
else
    mkdir -p "$HOME/bin"
    echo "$LAUNCHER_CONTENT" > "$HOME/bin/gpp"
    chmod +x "$HOME/bin/gpp"
    echo -e "  ${YELLOW}⚠${RESET}  Installed to: ${DIM}$HOME/bin/gpp${RESET}"

    # Auto-add ~/bin to PATH in shell config if not already there
    for RC in "$HOME/.zshrc" "$HOME/.bash_profile" "$HOME/.bashrc"; do
        if [ -f "$RC" ] && ! grep -q 'HOME/bin' "$RC"; then
            echo '' >> "$RC"
            echo '# G++ language' >> "$RC"
            echo 'export PATH="$HOME/bin:$PATH"' >> "$RC"
            echo -e "  ${GREEN}✓${RESET}  Auto-added PATH to ${DIM}$RC${RESET}"
            echo -e "     ${DIM}Restart your terminal (or run: source $RC)${RESET}"
            break
        fi
    done
fi

# ── Step 5: Install VS Code Extension ────────────────────────────────────────
echo ""
echo -e "  ${DIM}[5/5] Installing VS Code extension...${RESET}"

mkdir -p "$EXT_DEST/icons"
mkdir -p "$EXT_DEST/snippets"
mkdir -p "$EXT_DEST/syntaxes"

FAILED=0

dl() {
    local url="$1"
    local dest="$2"
    local label="$3"
    if curl -fsSL "$url" -o "$dest" 2>/dev/null; then
        echo -e "  ${GREEN}✓${RESET}  ${label}"
    else
        echo -e "  ${YELLOW}⚠${RESET}  Could not download: ${label}"
        FAILED=$((FAILED + 1))
    fi
}

dl "$GITHUB_RAW/vscode-gpp/package.json"                 "$EXT_DEST/package.json"                 "package.json"
dl "$GITHUB_RAW/vscode-gpp/language-configuration.json"  "$EXT_DEST/language-configuration.json"  "language-configuration.json"
dl "$GITHUB_RAW/vscode-gpp/icons/gpp_icon.png"           "$EXT_DEST/icons/gpp_icon.png"           "icons/gpp_icon.png"
dl "$GITHUB_RAW/vscode-gpp/snippets/gpp.json"            "$EXT_DEST/snippets/gpp.json"            "snippets/gpp.json"
dl "$GITHUB_RAW/vscode-gpp/syntaxes/gpp.tmLanguage.json" "$EXT_DEST/syntaxes/gpp.tmLanguage.json" "syntaxes/gpp.tmLanguage.json"

if [ "$FAILED" -eq 0 ]; then
    echo -e "  ${GREEN}✓${RESET}  Extension installed — restart VS Code to activate."
else
    echo -e "  ${YELLOW}⚠${RESET}  $FAILED file(s) failed. 'gpp' command still works fine."
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo -e "  ${CYAN}${BOLD}══════════════════════════════════════════${RESET}"
echo -e "  ${GREEN}${BOLD}  G++ is installed and ready!${RESET}"
echo -e "  ${CYAN}${BOLD}══════════════════════════════════════════${RESET}"
echo ""
echo -e "  Run any program from anywhere:"
echo -e "    ${BOLD}gpp ~/projects/main.G++${RESET}"
echo -e "    ${BOLD}gpp /any/path/program.G++${RESET}"
echo ""
echo -e "  ${DIM}Interpreter: $GPP_PY${RESET}"
echo -e "  ${DIM}Uninstall:   rm -rf $GPP_HOME $EXT_DEST && sudo rm -f /usr/local/bin/gpp${RESET}"
echo ""

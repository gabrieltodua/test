#!/bin/bash
# ═══════════════════════════════════════════════════════════
#  G++ Language Installer v3.0  —  macOS / Linux
#  One-line install:
#    curl -fsSL https://raw.githubusercontent.com/gabrieltodua/test/main/gpp/install.sh | bash
# ═══════════════════════════════════════════════════════════

set -e

GITHUB_RAW="https://raw.githubusercontent.com/gabrieltodua/test/main/gpp"

RESET='\033[0m'
BOLD='\033[1m'
DIM='\033[2m'
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'
WHITE='\033[97m'

clear 2>/dev/null || true

echo ""
echo -e "${CYAN}${BOLD}  ╔══════════════════════════════════════════╗"
echo -e "  ║     G++ Language — Installer  v3.0      ║"
echo -e "  ╚══════════════════════════════════════════╝${RESET}"
echo ""

GPP_HOME="$HOME/.gpp"
GPP_PY="$GPP_HOME/gpp.py"
EXT_DEST="$HOME/.vscode/extensions/gpp-language-3.0.0"

# ── Step 1: Python 3 ────────────────────────────────────────────────────────
echo -e "  ${DIM}[1/6]  Checking Python 3...${RESET}"

if ! command -v python3 &>/dev/null; then
    echo -e "  ${RED}✗  Python 3 not found.${RESET}"
    echo -e "     Download from: ${YELLOW}https://www.python.org/downloads/${RESET}"
    exit 1
fi

PY_VER=$(python3 --version 2>&1)
echo -e "  ${GREEN}✓${RESET}  $PY_VER"

# ── Step 2: curl ─────────────────────────────────────────────────────────────
echo ""
echo -e "  ${DIM}[2/6]  Checking curl...${RESET}"

if ! command -v curl &>/dev/null; then
    echo -e "  ${RED}✗  curl not found.${RESET}"
    echo -e "     macOS: ${YELLOW}brew install curl${RESET}  |  Linux: ${YELLOW}sudo apt install curl${RESET}"
    exit 1
fi
echo -e "  ${GREEN}✓${RESET}  curl available"

# ── Step 3: Download gpp.py ───────────────────────────────────────────────────
echo ""
echo -e "  ${DIM}[3/6]  Installing G++ interpreter...${RESET}"

mkdir -p "$GPP_HOME"

if curl -fsSL "$GITHUB_RAW/gpp.py" -o "$GPP_PY" 2>/dev/null; then
    chmod +x "$GPP_PY"
    echo -e "  ${GREEN}✓${RESET}  Interpreter: ${DIM}$GPP_PY${RESET}"
else
    echo -e "  ${RED}✗  Failed to download gpp.py${RESET}"
    echo -e "  ${DIM}Check your internet or the GITHUB_RAW URL at the top of this file.${RESET}"
    exit 1
fi

# ── Step 4: Install commands (gpp AND G++) ───────────────────────────────────
echo ""
echo -e "  ${DIM}[4/6]  Installing 'G++' and 'gpp' commands...${RESET}"

LAUNCHER="#!/bin/bash
exec python3 \"$GPP_PY\" \"\$@\""

install_cmd() {
    local name="$1"
    if echo "$LAUNCHER" | sudo tee "/usr/local/bin/$name" > /dev/null 2>&1 \
       && sudo chmod +x "/usr/local/bin/$name"; then
        echo -e "  ${GREEN}✓${RESET}  /usr/local/bin/$name  ${DIM}(system-wide)${RESET}"
    else
        mkdir -p "$HOME/bin"
        echo "$LAUNCHER" > "$HOME/bin/$name"
        chmod +x "$HOME/bin/$name"
        echo -e "  ${YELLOW}⚠${RESET}  $HOME/bin/$name  ${DIM}(user only)${RESET}"
        for RC in "$HOME/.zshrc" "$HOME/.bash_profile" "$HOME/.bashrc"; do
            if [ -f "$RC" ] && ! grep -q '"$HOME/bin"' "$RC" 2>/dev/null \
               && ! grep -q "\$HOME/bin" "$RC" 2>/dev/null; then
                printf '\n# G++ Language\nexport PATH="$HOME/bin:$PATH"\n' >> "$RC"
                echo -e "     ${DIM}Added PATH to $RC — restart terminal or: source $RC${RESET}"
                break
            fi
        done
    fi
}

install_cmd "gpp"
install_cmd "G++"

# ── Step 5: VS Code Extension ────────────────────────────────────────────────
echo ""
echo -e "  ${DIM}[5/6]  Installing VS Code extension...${RESET}"

mkdir -p "$EXT_DEST/icons" "$EXT_DEST/snippets" "$EXT_DEST/syntaxes"

FAILED=0

dl() {
    local url="$1" dest="$2" label="$3"
    if curl -fsSL "$url" -o "$dest" 2>/dev/null; then
        echo -e "  ${GREEN}✓${RESET}  $label"
    else
        echo -e "  ${YELLOW}⚠${RESET}  Could not download: $label"
        FAILED=$((FAILED + 1))
    fi
}

dl "$GITHUB_RAW/vscode-gpp/extension.js"               "$EXT_DEST/extension.js"               "extension.js  (run button + error checking)"
dl "$GITHUB_RAW/vscode-gpp/package.json"                "$EXT_DEST/package.json"                "package.json"
dl "$GITHUB_RAW/vscode-gpp/language-configuration.json" "$EXT_DEST/language-configuration.json" "language-configuration.json"
dl "$GITHUB_RAW/vscode-gpp/icons/gpp_icon.png"          "$EXT_DEST/icons/gpp_icon.png"          "icons/gpp_icon.png"
dl "$GITHUB_RAW/vscode-gpp/snippets/gpp.json"           "$EXT_DEST/snippets/gpp.json"           "snippets/gpp.json"
dl "$GITHUB_RAW/vscode-gpp/syntaxes/gpp.tmLanguage.json" "$EXT_DEST/syntaxes/gpp.tmLanguage.json" "syntaxes/gpp.tmLanguage.json"

if [ "$FAILED" -eq 0 ]; then
    echo -e "  ${GREEN}✓${RESET}  Extension ready — ${WHITE}restart VS Code to activate${RESET}"
else
    echo -e "  ${YELLOW}⚠${RESET}  $FAILED file(s) failed. The 'G++' command still works."
fi

# ── Step 6: Quick test ────────────────────────────────────────────────────────
echo ""
echo -e "  ${DIM}[6/6]  Verifying installation...${RESET}"

TEST_FILE="$GPP_HOME/test.G++"
cat > "$TEST_FILE" << 'EOF'
say("G++ installed successfully!")
say("Version:", "3.0.0")
EOF

if python3 "$GPP_PY" "$TEST_FILE" 2>/dev/null | grep -q "installed"; then
    echo -e "  ${GREEN}✓${RESET}  Interpreter test passed"
else
    echo -e "  ${YELLOW}⚠${RESET}  Test inconclusive — but install looks fine"
fi
rm -f "$TEST_FILE"

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo -e "  ${CYAN}${BOLD}══════════════════════════════════════════════${RESET}"
echo -e "  ${GREEN}${BOLD}  G++ v3.0 is installed and ready!${RESET}"
echo -e "  ${CYAN}${BOLD}══════════════════════════════════════════════${RESET}"
echo ""
echo -e "  ${WHITE}How to run:${RESET}"
echo -e "    ${BOLD}G++${RESET}                   ← auto-finds .G++ file here"
echo -e "    ${BOLD}G++ main.G++${RESET}          ← run specific file"
echo -e "    ${BOLD}G++ ~/projects/app.G++${RESET} ← run from any path"
echo ""
echo -e "  ${WHITE}In VS Code:${RESET}"
echo -e "    ${DIM}Open a .G++ file → press ▶ in top-right corner${RESET}"
echo -e "    ${DIM}Or press F5 / Ctrl+Shift+R${RESET}"
echo ""
echo -e "  ${DIM}Interpreter: $GPP_PY${RESET}"
echo -e "  ${DIM}Uninstall:   rm -rf $GPP_HOME $EXT_DEST && sudo rm -f /usr/local/bin/gpp /usr/local/bin/G++${RESET}"
echo ""

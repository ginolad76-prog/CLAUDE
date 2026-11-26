#!/usr/bin/env bash
# Pasang semua plugin & skill Claude Code (macOS / Linux / WSL / Git Bash).
# Aman dijalankan berulang: yang sudah terpasang akan dilewati atau di-update.

set -u

SKILLS_DIR="$HOME/.claude/skills"
OK=()
GAGAL=()

info()  { printf '\n\033[1;34m==> %s\033[0m\n' "$1"; }
sukses(){ OK+=("$1");    printf '\033[0;32m   ✓ %s\033[0m\n' "$1"; }
gagal() { GAGAL+=("$1"); printf '\033[0;31m   ✗ %s\033[0m\n' "$1"; }

# --- Cek syarat ---------------------------------------------------------------
for cmd in claude git; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Error: '$cmd' belum terpasang. Pasang dulu, lalu jalankan script ini lagi."
    exit 1
  fi
done
mkdir -p "$SKILLS_DIR"

# --- Plugin (lewat marketplace Claude Code) ----------------------------------
pasang_plugin() { # $1 = repo GitHub, $2 = plugin@marketplace
  info "Plugin: $2"
  claude plugin marketplace add "$1" >/dev/null 2>&1 || true   # sudah ada = tidak apa-apa
  if claude plugin install "$2" ; then sukses "$2"; else gagal "$2"; fi
}

pasang_plugin thedotmack/claude-mem                 claude-mem@thedotmack
pasang_plugin anthropics/skills                     example-skills@anthropic-agent-skills
pasang_plugin nextlevelbuilder/ui-ux-pro-max-skill  ui-ux-pro-max@ui-ux-pro-max-skill
pasang_plugin DietrichGebert/ponytail                ponytail@ponytail
pasang_plugin pbakaus/impeccable                     impeccable@impeccable

# --- Skill (folder di ~/.claude/skills) --------------------------------------
pasang_skill() { # $1 = repo GitHub, $2 = nama folder
  local tujuan="$SKILLS_DIR/$2"
  info "Skill: $2"
  if [ -d "$tujuan/.git" ]; then
    if git -C "$tujuan" pull --ff-only -q; then sukses "$2 (di-update)"; else gagal "$2 (update)"; fi
  elif [ -e "$tujuan" ]; then
    sukses "$2 (sudah ada, dilewati)"
  else
    if git clone -q --depth 1 "https://github.com/$1.git" "$tujuan"; then sukses "$2"; else gagal "$2"; fi
  fi
}

pasang_skill wheresryan22/anatomy      anatomy
pasang_skill BehiSecc/VibeSec-Skill    vibesec

# --- Ringkasan ----------------------------------------------------------------
echo
echo "========================================"
echo " Berhasil: ${#OK[@]}   Gagal: ${#GAGAL[@]}"
for g in "${GAGAL[@]+"${GAGAL[@]}"}"; do echo "   - gagal: $g"; done
echo "========================================"
echo
echo "Langkah berikutnya:"
echo " 1. Tutup lalu buka lagi Claude Code supaya skill & plugin termuat."
echo " 2. (Opsional) Chief of Staff: lihat setup/README.md bagian 'Chief of Staff'."

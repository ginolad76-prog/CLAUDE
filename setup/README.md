# Setup Claude Code di Laptop

Satu script untuk memasang semua plugin & skill yang dipakai.

## Yang dipasang

| Nama | Jenis | Fungsi |
|---|---|---|
| claude-mem | Plugin | Memori antar sesi: Claude ingat pekerjaan sebelumnya |
| example-skills (Anthropic) | Plugin | frontend-design, canvas-design, theme-factory, algorithmic-art, brand-guidelines, dll |
| UI UX Pro Max | Plugin | Database 80 gaya UI, 194 palet warna, 74 pasangan font, banner & slide |
| anatomy | Skill | Ilustrasi isometrik interaktif untuk menjelaskan ide teknis |
| VibeSec | Skill | Panduan keamanan saat membuat web app |

## Syarat

- **Claude Code** sudah terpasang dan sudah login (`claude` bisa dijalankan di terminal)
- **Git**
- **Node.js 20+** (dipakai skill anatomy)
- **Python 3** (dipakai UI UX Pro Max)

Cek cepat: `claude --version && git --version && node --version && python3 --version`
(di Windows pakai `python --version`)

## Cara pakai

**1. Ambil repo ini**

```bash
git clone https://github.com/ginolad76-prog/claude.git
cd claude
```

**2. Jalankan script**

macOS / Linux:
```bash
bash setup/install-skills.sh
```

Windows (PowerShell):
```powershell
powershell -ExecutionPolicy Bypass -File setup\install-skills.ps1
```

**3. Tutup lalu buka lagi Claude Code.** Cek dengan mengetik `/plugin` (daftar plugin) atau tanya "skill apa saja yang kamu punya?".

Script aman dijalankan ulang kapan saja; yang sudah terpasang dilewati, skill dari git akan di-update.

## Plugin & konektor dari akun claude.ai (tidak perlu script)

Ini dipasang lewat akun claude.ai, bukan lewat script, jadi ikut otomatis ke sesi mana pun yang login dengan akun yang sama (dicek 24 Nov 2026 di sesi cloud).

| Nama | Fungsi |
|---|---|
| superpowers (obra/superpowers) | Cara kerja terstruktur: brainstorming, rencana, debugging, TDD, review |
| caveman (akramsystems/caveman) | Mode jawaban super singkat ("caveman mode") |
| claude-code-setup | Rekomendasi otomasi Claude Code untuk sebuah proyek |
| claude-security | Pemindai celah keamanan kode |
| github | Konektor GitHub (issue, PR, repo) |
| instagram | Baca & balas komentar/DM Instagram (butuh token Graph API, lihat `/instagram:configure`) |

Konektor akun: Gmail, Google Drive, Google Sheets, Canva, Claude Docs, Metricool, TikTok for Business, Windsor.ai, vidIQ, Orla, PocketSmith, Perplexity Computer.

Kalau salah satu plugin di atas tidak muncul di laptop: ketik `/plugin`, cari namanya di tab Discover, lalu install. Untuk superpowers bisa juga:
`/plugin marketplace add obra/superpowers-marketplace` lalu `/plugin install superpowers@superpowers-marketplace`.

Repo yang dipakai: hanya `ginolad76-prog/claude` (repo ini).

## Chief of Staff (opsional, manual)

Tidak dimasukkan ke script karena installer-nya menanyakan data pribadi (nama, email, jabatan, zona waktu) dan **menimpa `~/.claude/CLAUDE.md`**. Kalau kamu sudah punya `CLAUDE.md` sendiri, backup dulu.

```bash
git clone https://github.com/mimurchison/claude-chief-of-staff.git
cd claude-chief-of-staff
./install.sh
```

Butuh konektor **Gmail** dan **Google Calendar**. Setelah itu coba `/gm` (briefing pagi) atau `/triage` (sortir inbox). Di Windows, jalankan `install.sh` lewat Git Bash atau WSL.

## Kalau ada yang gagal

- `claude: command not found` → Claude Code belum terpasang atau belum ada di PATH.
- Plugin gagal → coba manual di dalam Claude Code: `/plugin marketplace add <repo>` lalu `/plugin install <nama>`.
- Skill gagal di-clone → cek koneksi internet / akses ke github.com.

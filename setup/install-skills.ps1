# Pasang semua plugin & skill Claude Code (Windows PowerShell).
# Aman dijalankan berulang: yang sudah terpasang akan dilewati atau di-update.

$SkillsDir = Join-Path $HOME ".claude\skills"
$Ok = @(); $Gagal = @()

foreach ($cmd in @("claude", "git")) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Host "Error: '$cmd' belum terpasang. Pasang dulu, lalu jalankan script ini lagi." -ForegroundColor Red
        exit 1
    }
}
New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null

function Pasang-Plugin($Repo, $Plugin) {
    Write-Host "`n==> Plugin: $Plugin" -ForegroundColor Cyan
    claude plugin marketplace add $Repo *> $null
    claude plugin install $Plugin
    if ($LASTEXITCODE -eq 0) { $script:Ok += $Plugin; Write-Host "   OK $Plugin" -ForegroundColor Green }
    else { $script:Gagal += $Plugin; Write-Host "   GAGAL $Plugin" -ForegroundColor Red }
}

function Pasang-Skill($Repo, $Nama) {
    $Tujuan = Join-Path $SkillsDir $Nama
    Write-Host "`n==> Skill: $Nama" -ForegroundColor Cyan
    if (Test-Path (Join-Path $Tujuan ".git")) {
        git -C $Tujuan pull --ff-only -q
        $label = "$Nama (di-update)"
    } elseif (Test-Path $Tujuan) {
        $script:Ok += "$Nama (sudah ada)"; Write-Host "   OK $Nama (sudah ada, dilewati)" -ForegroundColor Green; return
    } else {
        git clone -q --depth 1 "https://github.com/$Repo.git" $Tujuan
        $label = $Nama
    }
    if ($LASTEXITCODE -eq 0) { $script:Ok += $label; Write-Host "   OK $label" -ForegroundColor Green }
    else { $script:Gagal += $label; Write-Host "   GAGAL $label" -ForegroundColor Red }
}

Pasang-Plugin "thedotmack/claude-mem"                "claude-mem@thedotmack"
Pasang-Plugin "anthropics/skills"                    "example-skills@anthropic-agent-skills"
Pasang-Plugin "nextlevelbuilder/ui-ux-pro-max-skill" "ui-ux-pro-max@ui-ux-pro-max-skill"
Pasang-Plugin "DietrichGebert/ponytail" "ponytail@ponytail"
Pasang-Plugin "pbakaus/impeccable" "impeccable@impeccable"

Pasang-Skill "wheresryan22/anatomy"   "anatomy"
Pasang-Skill "BehiSecc/VibeSec-Skill" "vibesec"

# Remotion (bikin video pakai kode): salinan ada di repo ini, .claude\skills\
Write-Host "`n==> Skill: remotion-best-practices" -ForegroundColor Cyan
$Rem = Join-Path $SkillsDir "remotion-best-practices"
if (Test-Path $Rem) { Remove-Item -Recurse -Force $Rem }
Copy-Item -Recurse (Join-Path $PSScriptRoot "..\.claude\skills\remotion-best-practices") $Rem
if ($?) { $Ok += "remotion-best-practices" } else { $Gagal += "remotion-best-practices" }

Write-Host "`n========================================"
Write-Host " Berhasil: $($Ok.Count)   Gagal: $($Gagal.Count)"
foreach ($g in $Gagal) { Write-Host "   - gagal: $g" -ForegroundColor Red }
Write-Host "========================================`n"
Write-Host "Langkah berikutnya:"
Write-Host " 1. Tutup lalu buka lagi Claude Code supaya skill & plugin termuat."
Write-Host " 2. (Opsional) Chief of Staff: lihat setup\README.md bagian 'Chief of Staff'."

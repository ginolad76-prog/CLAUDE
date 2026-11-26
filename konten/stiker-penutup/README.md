# Stiker penutup jendela caravan (sisi dalam)

Dibuat 26 Nov 2026. Sisi dalam penutup hanya terlihat saat caravan buka, jadi isinya dipakai sebagai papan nama dan penunjuk antrean.

Versi 8 (26 Nov): ornamen lampion & awan, gelas diganti cup asli Toko Teh (Cup B, 1 warna hijau), set final 3 stiker. Ringkasan skala: `SET-FINAL-skala.png`.

| File | Ukuran jadi | Isi |
|---|---|---|
| `1-penutup-utama-320x90.pdf` | 320 × 90 cm | Logo besar, TOKO TEH · TJAP DUA KOI, "Sepasang koi, segelas teh", lampion di kedua ujung. |
| `2-samping-komik-140x90.pdf` | 140 × 90 cm | Komik 4 panel: Hari ini berat… / Mampir dulu. / Tehnya ditarik… / Ahh… enaknya! |
| `3-samping-uap-logo-140x90.pdf` | 140 × 90 cm | Uap segelas teh naik jadi logo + "IKUTI UAP TEHNYA!" + @tokoteh.tjapduakoi + QR ke Instagram. |

Tambahan (bukan stiker penutup): `meja-member-kolam-koi.pdf` (desain 140×90, untuk dicetak kecil di meja) berisi ajakan GABUNG MEMBER KOLAM KOI + QR ke https://tokotehtjapduakoi.github.io/kolam/.

Akun Instagram toko: @tokoteh.tjapduakoi. Sumber desain: `sumber/gen8.py` (stiker 2 & 3, cup asli + ornamen) dan `sumber/gen5.py` (rantai gen4 → gen3 → gen2 → gen.py).

## Catatan untuk percetakan
- PDF vektor, ukuran asli 1:1, sudah termasuk **bleed 2 cm** tiap sisi (file 324 × 94 cm dan 144 × 94 cm). Potong di ukuran jadi.
- Bahan saran: vinyl outdoor + laminasi doff/UV (kena panas & asap). Warna: hijau `#0E4D32`, emas `#C9A24B`, krem `#F6EFDF`, marun `#7A1F2B`.
- File `*-preview.png` memperlihatkan garis potong (putus-putus magenta); jangan dicetak.

## Arah tempel (penting)
- **Atas desain = tepi luar/bebas penutup** (yang jauh dari engsel). Bawah desain = sisi engsel, dekat lubang jendela. Saat penutup diangkat, pembeli yang mendongak akan membaca tulisan tegak dan panah ▼ menunjuk ke jendela.
- Penutup utama: "PESAN & BAYAR" di kanan (sisi kasir), "AMBIL" di kiri — dilihat dari depan caravan.
- Ukuran 90 × 140 diasumsikan **lebar 140, tinggi 90** (sama dengan 90 × 320 = lebar 320). Kalau terbalik, minta desain ulang.
- Rangka/rusuk besi di sisi dalam: ukur posisinya dulu. Kalau stiker harus dipotong per panel, potong di garis rangka, bukan di tengah tulisan.

## Ubah desain
`sumber/gen.py` menghasilkan HTML; ekspor ke PDF dengan Chromium (lihat riwayat sesi 26 Nov). Logo dari file vektor FINAL di Google Drive; maskot digambar ulang sebagai vektor.

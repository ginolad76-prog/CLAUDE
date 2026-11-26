# Stiker penutup jendela caravan (sisi dalam)

Dibuat 26 Nov 2026. Sisi dalam penutup hanya terlihat saat caravan buka, jadi isinya dipakai sebagai papan nama dan penunjuk antrean.

Versi 3 (26 Nov), set final 3 stiker. Ringkasan skala: `SET-FINAL-skala.png`.

| File | Ukuran jadi | Isi |
|---|---|---|
| `1-penutup-utama-320x90.pdf` | 320 × 90 cm | Logo besar, TOKO TEH · TJAP DUA KOI, "Sepasang koi, segelas teh", lampion di kedua ujung. |
| `2-samping-komik-140x90.pdf` | 140 × 90 cm | Komik 4 panel dua koi: Sendirian… / Wangi apa ini? / Hup! / Ketemu deh! |
| `3-samping-uap-koi-140x90.pdf` | 140 × 90 cm | Uap segelas teh berubah jadi sepasang koi + "TARIK NAPAS, TARIK TEH." |

Sumber desain: `sumber/gen3.py` (memakai gen2.py/gen.py).

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

# Branding badan caravan (draf 3: stiker elemen, 26 Nov 2026)

**Sistem: stiker potong (print & cut kontur).** Cat dinding tetap (marun di sisi 4 m, hijau di sisi 2 m); yang ditempel hanya elemennya. PDF berlatar TRANSPARAN; percetakan memotong mengikuti bentuk elemen (offset kontur ±3 mm). Pratinjau (`*-preview.png`, `TAMPAK-*`) memperlihatkan elemen di atas warna dinding.

Ukuran masih PERKIRAAN. Sudah diketahui: sisi 2 m bawah jendela 90 cm, kiri-kanan jendela ±30 cm (jendela ±140 cm). Ukur dulu bersama Pakde sebelum cetak: roda (diameter fender, posisi, tinggi tonjolan), jendela sisi 2 m, tinggi atas jendela, posisi pintu di sisi belakang.

| File | Ukuran | Letak | Isi |
|---|---|---|---|
| `4m-ruko-400x90.pdf` | 400 × 90 | Sisi 4 m, bawah jendela (marun) | Pilihan A: TOKO TEH · TJAP DUA KOI + deretan ruko kopitiam & lampion (motif cup); roda jatuh di "jalan" tengah. |
| `4m-kolam-400x90.pdf` | 400 × 90 | Sisi 4 m, bawah jendela | Pilihan B: TOKO TEH + kolam, dua koi besar, riak air mengelilingi roda. |
| `strip-kiri-40x100.pdf` | 40 × 100 | Kiri jendela utama | Stempel 茶 + "TEH TARIK" tersusun vertikal. |
| `strip-kanan-40x100.pdf` | 40 × 100 | Kanan jendela utama | Stempel 茶 + dua koi berenang naik. |
| `2m-spot-foto-200x90.pdf` | 200 × 90 | Cadangan (kurang awet) | Cup Toko Teh raksasa + "FOTO DULU, BARU TARIK." + @tokoteh.tjapduakoi. |
| `strip-2m-30x100.pdf` | 30 × 100 | Kiri & kanan jendela sisi 2 m (cetak 4) | Lampion menyala + dua koi berenang naik. |
| `2m-emblem-200x90.pdf` | 200 × 90 | Sisi 2 m (pilihan) | Emblem TOKO TEH · TJAP DUA KOI · EST. 2026 · SAMARINDA + lampion + koi & teratai lanjutan kolam. |
| `2m-lampion-cha-200x90.pdf` | 200 × 90 | Sisi 2 m (pilihan) | Untaian lampion + stempel 茶 besar + koi & teratai lanjutan kolam. |

- `TAMPAK-4m-ruko.png` / `TAMPAK-4m-kolam.png`: gambar tampak sisi 4 m lengkap (strip + panel bawah + roda perkiraan).
- `*-preview.png` panel 4 m memperlihatkan zona roda (magenta) — jangan dicetak. PDF sudah tanpa tanda itu, bleed 2 cm.
- Stiker di zona roda dipotong mengikuti lengkung fender saat pemasangan.
- Sumber: `sumber/gen9.py` (memakai gen8.py dst.).

## Warna & format cetak
- Semua PDF (badan caravan, stiker penutup, logo Ø195) sudah dikonversi ke **CMYK** (Ghostscript, DeviceCMYK) dan siap untuk percetakan.
- Palet kalem: warna brand + sage #A9C2A6 dan mustard #D9B35F (ruko), hijau teratai #5FAF5A & pink lotus #F29BB0 (kolam). Tanpa efek cahaya/gradasi transparan karena stiker dipotong.
- Warna di layar (RGB) akan sedikit lebih kalem setelah dicetak CMYK, terutama teal dan pink. Minta proof warna dulu.

Keputusan 26 Nov: sisi 4 m = **kolam koi**. Sisi 2 m = emblem EST. 2026 dan lampion + 茶 (isi permanen, tanpa harga/promo). Tampak: `TAMPAK-2m-emblem.png`, `TAMPAK-2m-lampion-cha.png`.

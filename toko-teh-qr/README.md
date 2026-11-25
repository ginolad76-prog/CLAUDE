# QR code website Toko Teh Tjap Dua Koi

Isi QR: `https://tokotehtjapduakoi.github.io`
QR versi 3 (29×29 modul), error correction **M** (±15% boleh rusak/kotor), quiet zone 4 modul di tiap sisi.

| File | Pakai untuk |
|---|---|
| `qr-tokotehtjapduakoi-hijau.svg` | Percetakan / desain (vektor, tajam di ukuran berapa pun). Warna #0E4D32 |
| `qr-tokotehtjapduakoi-hitam.svg` | Sama, warna hitam (paling aman untuk dibaca) |
| `qr-tokotehtjapduakoi-hijau.png` / `-hitam.png` | 2960×2960 px, latar putih |
| `...-transparan.png` | Latar transparan, untuk ditempel di desain yang latarnya sudah terang |

## Hasil tes decoder (ZXing + OpenCV)

Lulus di semua kondisi: ukuran asli, diperkecil ke 295 px (2,5 cm @300 dpi), 148 px, 90 px,
diburamkan, diputar 17°, diberi derau, dan diletakkan di atas warna teh tarik. SVG juga dirender dan dites.

## Catatan cetak di cup plastik bening (2,5 cm)

- **Minta percetakan memberi lapisan putih di belakang QR** (white underbase). Tanpa itu, isi cup
  (teh tarik coklat, es) terlihat menembus dan kamera HP bisa gagal membaca. Lapisan putih harus
  mencakup quiet zone (bingkai putih di sekeliling QR).
- Ukuran 2,5 cm sudah termasuk quiet zone. Jangan dipotong bingkai putihnya.
- Versi **hitam** paling kontras. Versi hijau #0E4D32 masih aman karena cukup gelap.
- Jangan letakkan QR tepat di lipatan/sambungan sablon cup, dan hindari bagian yang paling melengkung.
- Sebelum cetak massal, minta 1–2 contoh cetak lalu tes scan dengan beberapa HP (kamera bawaan, Android & iPhone), cup diisi minuman.

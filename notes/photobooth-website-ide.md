# Ide: Website Photobooth (disimpan dulu, belum dikerjakan)

Dicatat 25 Nov 2026 dari sesi Claude Code **"Photobooth Website"**.
Status: **ide — disimpan untuk nanti.** Belum ada kode.

## Ide inti (dari pemilik)
- Website photobooth: buka kamera (HP/laptop/tablet), ambil foto, jadi strip.
- Hasilnya bisa berupa **struk/receipt** (gaya kertas kasir thermal) dan **bisa langsung di-print**
  (printer thermal 58/80 mm atau printer biasa).
- Ditambah ide-ide photobooth lain yang menarik.

## Bank ide tambahan (usulan Claude, belum diputuskan)
1. **Struk Teh** — foto dicetak seperti struk kasir: "1x Senyum ......... Rp0", tanggal, jam, nomor antrean,
   QR ke Instagram toko. Cocok untuk caravan Toko Teh Tjap Dua Koi.
2. **Strip 4 frame** klasik (vertikal) + countdown 3-2-1 + flash layar putih.
3. **Bingkai/stiker tema**: koi, lampion (Mahakam Lampion Garden), musiman (Natal, Imlek, Ramadan).
4. **GIF / boomerang** — 4 jepretan digabung jadi animasi, bisa diunduh/di-share.
5. **QR unduh** — tamu scan QR untuk ambil file digital tanpa kirim WA satu-satu.
6. **Mode event** — nama acara/pengantin di struk, galeri semua foto acara.
7. **Filter** — hitam-putih jadul, film, sepia; mode "pas foto".
8. **Promo terselip** — kupon di bawah struk ("tunjukkan struk ini, diskon 2rb"), terhubung program Teman Tarik.
9. **Ramalan / kata-kata acak** di struk ("Hari ini cocok minum Matcha Tarik").
10. **Bisa disewakan** — photobooth untuk acara orang lain sebagai usaha sampingan.

## Catatan teknis kalau nanti dibuat
- Bisa jalan di browser saja (kamera via `getUserMedia`, gabung foto pakai canvas) — cocok di GitHub Pages
  seperti Dompet Koi.
- Print struk: CSS `@page` lebar 58/80 mm lewat dialog print; printer thermal Bluetooth perlu dicek mereknya.
- Pertanyaan yang belum dijawab: dipakai di mana (caravan toko / event / disewakan)? Printer apa?

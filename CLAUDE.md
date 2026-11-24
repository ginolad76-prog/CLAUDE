# Catatan untuk Claude

Pengguna berbicara Bahasa Indonesia; balas dalam Bahasa Indonesia.

## Mulai dari sini
- **Baca `MEMORI.md` dulu.** Isinya ringkasan semua yang pernah dibahas di sesi-sesi lain (usaha Toko Teh Tjap Dua Koi, Dompet Koi, skill yang dipasang, link artifact, catatan desain).
- Saat pengguna bilang "ingat" atau "simpan", tambahkan ke `MEMORI.md` atau `notes/`, perbarui indeksnya, lalu commit dan push.
- Saat pengguna minta bikin iklan/poster/video promo, baca juga `notes/README.md`.
- Skill & plugin yang pengguna pasang tercatat di `setup/` — jalankan `bash setup/install-skills.sh` kalau belum terpasang di sesi/laptop ini.


## Dompet Koi (keuangan keluarga + Toko Teh)

Website ada di `docs/` (GitHub Pages), database di Supabase project `fniplnydvtkampqqegjs`.
Pemilik meminta Claude mencatat transaksi yang ia sebut di chat ("keluar 150rb bensin", "omzet toko 1,2jt").

Cara mencatat:
- Secret key Supabase disuntikkan otomatis oleh proxy untuk host `fniplnydvtkampqqegjs.supabase.co` (environment "CLAUDE (Dompet Koi)"). Jangan menulis kunci di mana pun; cukup panggil REST tanpa header apikey.
- Ambil `household_id` dari tabel `households` dan `user_id` pemilik dari `members` (bukan dari catatan ini).
- Insert ke `public.transactions`: `household_id`, `book` (`keluarga` | `toko`), `kind` (`keluar` | `masuk`), `amount` (rupiah, bilangan bulat), `category` (pakai daftar kategori di `docs/index.html`, objek `CATS`), `note`, `tx_date`, `created_by` = user_id pemilik. Tambahkan "(dicatat Claude)" di `note`.
- Sebelum insert, sebutkan ulang ke pemilik: tanggal, buku, jenis, kategori, jumlah. Kalau ada yang ambigu (buku keluarga atau toko? tanggal?), tanyakan dulu.
- Setelah insert, baca balik barisnya untuk memastikan tersimpan, lalu laporkan.
- Cicilan pinjaman mama dicatat dengan kategori `Cicilan mama` (buku keluarga, keluar).

## Konten media sosial

Sebelum membuat postingan, story, reels, atau papan menu untuk Toko Teh Tjap Dua Koi, baca `konten/PANDUAN-KONTEN.md` (identitas brand, referensi gaya @madlyfuel, format, dan pola post).
Kalau pengguna menyebut "gaya krum" / "kayak krum.ae", baca juga `konten/REFERENSI-KRUM.md`.

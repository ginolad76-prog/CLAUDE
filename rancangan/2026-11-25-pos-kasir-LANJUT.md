# Kasir Koi — titik lanjut (dijeda 26 Nov 2026, kuota habis)

Kode: repo tokotehtjapduakoi/tokotehtjapduakoi.github.io, cabang `claude/pos-toko-teh-tjap-dua-koi-1mze9t` (HEAD 80192c7), sudah di-push. Main TIDAK disentuh; database asli BELUM diubah.
Semua 14 langkah rencana + review akhir + 2 gabungan dengan main (d4f2562, Teman Tarik/voucher) selesai. Uji: pytest 161, e2e 55 lulus.
Ledger lengkap (keputusan & temuan kecil yang ditunda): `rancangan/2026-11-25-pos-kasir-ledger.md`.

## Sisa langkah
1. (Opsional, dihentikan pemilik) review keamanan hasil gabungan cabang vs main.
2. Cek main belum berubah lagi (sesi lain sering mengubah Kolam Koi); kalau berubah, gabung lagi.
3. Merge cabang ke main (pemilik mengizinkan tindakan yang bisa dibalik).
4. Pemilik jalankan SQL dari HP: `/kolam/admin/sql.html` (Kolam Koi) lalu `/kolam/admin/sql.html?f=kasir`. Ikuti `kasir/PANDUAN.md`.
5. Kunci secret Kolam Koi sudah tersimpan di environment "Toko Teh Tjap Dua Koi" (network secret, header apikey). Sebelum SQL baru dijalankan, service_role ditolak (42501) — normal.
6. Jalankan `_uji/asap_asli.py` ke database asli (di luar jam buka), lalu minta pemilik jalankan SQL pembersih yang dicetak.
7. Pemilik pasang verifikasi 2 langkah (Google Authenticator) di /kasir/ dan /kolam/admin/ — belum pernah dicoba sungguhan.
8. Perbarui MEMORI.md & CLAUDE.md (bagian Kasir Koi).
9. Tahap berikut (rencana terpisah): stok & selisih stok; sinkron omzet ke Dompet Koi; hapus foto >3 bulan.

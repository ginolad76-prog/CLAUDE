# Kasir Koi — status (26 Nov 2026)

**TAYANG.** https://tokotehtjapduakoi.github.io/kasir/ (main = 4bed5f7). SQL Kolam Koi + Kasir Koi sudah dijalankan pemilik (versi terbaru). Pemilik sudah: verifikasi 2 langkah, nomor HP di Staf, HP disetujui, uji jual + batal (2 nota batal 26 Nov).
Masa transisi ESB menyala (nota manual kasir + klaim nota lama). Matikan keduanya di Admin Kolam Koi → Nota saat ESB berhenti.
Kunci secret Kolam Koi ada di environment "Toko Teh Tjap Dua Koi" (network secret, header apikey) → Claude baca semua tabel sebagai service_role. Catatan: proxy menimpa apikey di SETIAP request dari environment ini, jadi uji sebagai kasir/member tidak bisa dari sini; service_role tidak punya EXECUTE fungsi (baca tabel langsung).

## Fitur yang ada
Jual (tunai/QRIS/transfer, foto wajib, nota terkunci), kode Kolam Koi (QR/WA, terikat nomor), offline, shift + serah terima buta, void lewat pemilik, laporan Harian + Rentang (bebas, ≤366 hari), ambil/tambah kas pemilik, HP disetujui, 2 langkah pemilik, Teman Tarik/voucher bernota.

## Keputusan pemilik terbaru
- Menu tidak perlu dihapus: cukup nonaktif. Paket dibuat manual sebagai menu biasa (kategori Paket).
- Stok (tahap 2, belum dibangun): dua jalur — pemilik/Claude lewat chat (belanja & hitung); kasir WAJIB hitung stok buta setiap tutup toko (SOP harian, foto rak). Stok masuk hanya pemilik/Claude.

## Berikutnya
1. Tahap 2: stok & selisih stok (lihat atas) — brainstorm/rencana dulu.
2. Sinkron omzet harian ke Dompet Koi (perlu grant fungsi/tabel untuk service_role + kunci Dompet Koi).
3. Hapus foto bukti > 3 bulan.
4. Minor tertunda: lihat ledger (`rancangan/2026-11-25-pos-kasir-ledger.md`).

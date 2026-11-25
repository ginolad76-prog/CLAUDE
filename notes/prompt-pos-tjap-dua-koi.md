# Prompt: POS Toko Teh Tjap Dua Koi

Tempel teks di bawah ke sesi Claude Code baru (repo `tokotehtjapduakoi/tokotehtjapduakoi.github.io`, ditambah `ginolad76-prog/claude` untuk catatan).

---

Aku pemilik Toko Teh Tjap Dua Koi (caravan teh tarik di Mahakam Lampion Garden, Samarinda). Balas dalam Bahasa Indonesia, pakai bahasa sederhana, karena aku mengurus semuanya dari HP.

**Yang aku mau:** sistem kasir (POS) buatan sendiri yang betul-betul kami kelola. Sekarang kasir pakai ESB. Tujuanku:
1. Semua transaksi tercatat di sistem milik kami sendiri, jadi tidak tergantung ESB.
2. Karyawan tidak bisa membuat transaksi atau nota bodong. Setiap transaksi tercatat atas nama karyawan yang login, dan ada **foto bukti** (struk QRIS / uang / pesanan).
3. Tersambung ke **Kolam Koi** (gacha kartu koi untuk member). Setiap transaksi yang dibayar menghasilkan **kode klaim acak yang tidak bisa ditebak**, dicetak di struk atau tampil sebagai QR. Pelanggan cukup ketik atau scan kode itu di Kolam Koi, tanpa isi nominal. Jumlah tarikan otomatis mengikuti total transaksi.
4. Laporan harian: omzet, jumlah nota, per metode bayar, per karyawan, menu terlaris. Kalau bisa, omzet harian ikut tercatat ke Dompet Koi (buku `toko`).

**Yang sudah ada (baca dulu sebelum merancang):**
- Website toko: repo `tokotehtjapduakoi/tokotehtjapduakoi.github.io` (GitHub Pages, tanpa framework).
- Kolam Koi: folder `kolam/` di repo itu. Baca `kolam/PANDUAN.md`, `kolam/setup.sql`, `kolam/app.js`, `kolam/admin/admin.js`.
  - Database: project Supabase **kolam-koi** (URL & publishable key ada di `kolam/config.js`).
  - Nota masuk lewat tabel `kk_receipts(nota, total, created_by, ...)` dan fungsi `kk_add_receipt`. Pelanggan klaim lewat fungsi `kk_claim(p_nota, p_total)`, yang saat ini mewajibkan total karena nomor nota ESB mudah ditebak. Kalau POS sudah membuat kode acak, `kk_claim` boleh diubah jadi cukup kode saja.
  - Staf login dengan email di tabel `kk_staff` (peran `pemilik` / `kasir`). POS sebaiknya memakai akun staf yang sama.
  - Project Supabase baru **tidak** memberi izin tabel otomatis ke `anon`/`authenticated`, jadi tulis `grant` secara eksplisit. Semua perubahan data lewat fungsi `security definer`, dan RLS aktif di semua tabel.
- Dompet Koi (keuangan keluarga + toko): repo `ginolad76-prog/claude`, folder `docs/`, project Supabase **terpisah**. Baca `CLAUDE.md` dan `MEMORI.md` di repo itu. Jangan campur database POS dengan database keuangan keluarga.
- Menu & harga: tanyakan ke aku, atau cek `MEMORI.md` dan dokumen HPP yang tercatat di sana.

**Yang perlu diputuskan bersamaku dulu (tanya satu per satu, jangan langsung membangun):**
- ESB diganti total oleh POS ini, atau dipakai berdampingan untuk sementara?
- Pembayaran: tunai, QRIS statis, transfer? QRIS hanya dicatat (kasir foto bukti), bukan integrasi payment gateway, kecuali aku minta.
- Struk: dicetak ke printer thermal Bluetooth, dikirim ke WhatsApp pelanggan, atau cukup ditampilkan di layar sebagai QR?
- Perangkat kasir (HP Android / tablet), dan apakah harus tetap bisa mencatat saat internet putus.
- Stok bahan / HPP ikut dikelola atau tidak (untuk tahap pertama).
- Siapa boleh membatalkan transaksi (void) dan bagaimana jejaknya.

**Syarat:**
- Jalan di HP lewat browser (bisa dipasang ke layar utama), ringan, tanpa biaya bulanan selain Supabase gratis.
- Tidak ada kunci rahasia di kode website. Yang boleh hanya publishable key.
- Setiap void, diskon, dan perubahan harga tercatat siapa yang melakukannya dan kapan.
- Uji fungsi database dan alur di browser sebelum bilang selesai.
- Sertakan panduan pemasangan yang bisa kuikuti dari HP, seperti `kolam/PANDUAN.md`.
- Mulai dengan menanyakan tujuanku, lalu tawarkan 2–3 pendekatan beserta rekomendasimu sebelum menulis kode.

# Rancangan: Kasir Koi (POS Toko Teh Tjap Dua Koi)

Tanggal: 25 Nov 2026 · Status: menunggu persetujuan akhir pemilik

## 1. Tujuan dan alasannya

Pemilik ingin berhenti memakai ESB dan memakai kasir buatan sendiri, karena:
1. Semua transaksi tercatat di sistem milik toko sendiri.
2. Karyawan tidak bisa membuat nota bodong. Setiap nota tercatat atas nama karyawan yang login dan wajib punya foto bukti.
3. Setiap nota lunas langsung memberi pelanggan kode klaim Kolam Koi yang acak dan tidak bisa ditebak. Pelanggan tidak perlu mengetik nomor nota dan total lagi.
4. Laporan harian untuk pemilik. Omzet harian otomatis masuk ke Dompet Koi (buku "toko").
5. Stok bahan ikut dikelola, dan selisih stok dipakai sebagai alat anti-curang.

Pemilik mengurus semuanya dari HP dan ingin "satu tempat, Claude yang mengurus otomatisnya". **Keamanan adalah syarat utama:** sistem tidak boleh mudah dibobol, dan tidak boleh bergantung pada aplikasi kasir pihak lain.

## 2. Sasaran, bukan sasaran, anti-sasaran

**Sasaran (tahap 1)**
- Kasir di browser HP, Android maupun iPhone, bisa dipasang ke layar utama. Kasir bisa login dari HP mana saja.
- Jual: pilih menu → ukuran/varian → total → metode bayar → foto bukti → lunas → kode klaim (QR + tombol kirim WA).
- Kasir tetap bisa mencatat saat internet putus; nota dikirim otomatis begitu sinyal kembali.
- Pembatalan (void) hanya lewat pengajuan kasir disertai alasan, lalu disetujui pemilik.
- Shift dan serah terima kas antar kasir.
- Stok: bahan, resep per menu, stok masuk, hitung stok, dan laporan selisih.
- Laporan harian pemilik.
- Omzet harian dikirim ke Dompet Koi.
- Panduan pemasangan yang bisa diikuti dari HP.

**Bukan sasaran (tahap 1)**
- Payment gateway atau pengecekan QRIS otomatis. QRIS cukup dibuktikan dengan foto.
- Printer struk. Bisa ditambah nanti.
- GoFood/Grab di POS. Tetap dicatat terpisah di Dompet Koi.
- Banyak cabang. Rancangan tidak boleh menghalangi cabang di kemudian hari, tapi tahap 1 hanya satu toko.

**Anti-sasaran** (kalau ini terjadi, rancangan gagal meski aplikasinya "jalan")
- Kasir bisa mengubah atau menghapus nota yang sudah lunas, atau mengubah harga dan stok tanpa jejak.
- Kasir bisa memanen kode klaim pelanggan untuk akun Kolam Koi miliknya sendiri.
- Ada kunci rahasia di kode website.
- Data POS bercampur dengan database keuangan keluarga (Dompet Koi).
- Antrean berhenti karena sinyal jelek.
- Kasir harus mengetik banyak; satu transaksi biasa harus selesai dalam ±30 detik.

## 3. Batasan

- Gratis, tanpa biaya bulanan selain Supabase versi gratis. Akun Supabase gratis hanya boleh 2 project aktif, dan keduanya sudah terpakai (Dompet Koi, Kolam Koi).
- Website statis di GitHub Pages, tanpa framework, mengikuti gaya `kolam/` (HTML + JS biasa, `supabase-js` dari folder `vendor`).
- Hanya **publishable key** di kode website. Kunci rahasia hanya disimpan di pengaturan environment Claude (disuntikkan proxy), seperti Dompet Koi.
- RLS aktif di semua tabel. Tidak ada grant insert/update/delete ke anon/authenticated. Semua perubahan data lewat fungsi `security definer` yang mengecek peran. Grant select/execute ditulis eksplisit, karena project Supabase baru tidak memberi izin otomatis.
- Setiap void, diskon, perubahan harga/menu, dan perubahan stok tercatat: siapa, kapan, nilai lama, dan nilai baru.
- Zona waktu WITA (`Asia/Makassar`) untuk "hari ini" dan laporan.
- Fungsi database dan alur di browser harus diuji sebelum dinyatakan selesai.

## 4. Pendekatan yang dipertimbangkan

| | Pendekatan | Untung / rugi |
|---|---|---|
| **A (dipilih)** | POS menumpang di project Supabase **Kolam Koi**, halaman di `tokotehtjapduakoi.github.io/kasir/` | Akun staf sama. Nota dan kode klaim dibuat dalam satu transaksi database. Celah "daftarkan nota manual" bisa ditutup. Gratis. Kuota storage 1 GB harus dihemat. |
| B | POS di project Supabase sendiri | Butuh project ketiga (berbayar), kasir login dua kali, dan perlu server perantara untuk kode Kolam Koi. |
| C | Aplikasi kasir jadi (Loyverse, dll.) | Data bukan milik sendiri, tidak ada foto wajib, dan tidak bisa membuat kode Kolam Koi. Bertentangan dengan tujuan. |

Pemilik menyerahkan pilihan ke Claude dengan syarat aman dan tidak bergantung pada POS lain. A dipilih karena satu-satunya yang memenuhi semua syarat tanpa biaya.

## 5. Keputusan pemilik

| Hal | Keputusan |
|---|---|
| Pembayaran | Tunai, QRIS, transfer bank. QRIS akan ada lebih dari satu (GoPay, ShopeePay), jadi metode bayar berupa **daftar yang bisa diatur pemilik**. |
| Struk | Tanpa kertas. Utamanya **kirim WA** (link `wa.me` berisi rincian + link klaim). Cadangannya **QR di layar**. |
| Perangkat | Website, bisa pindah HP, dan HP boleh milik siapa saja; cukup login akun staf. Struk WA terkirim dari WhatsApp di HP yang dipakai. |
| Shift | Kasir bergantian shift; uang tunai diserahterimakan saat ganti shift. |
| Peralihan | Pelan-pelan dari ESB. Inti dulu, stok dan Dompet Koi menyusul. |
| Offline | Tetap bisa mencatat; dikirim otomatis saat online. |
| Stok | Ikut dikelola. Pemilik melaporkan jumlah stok ke Claude lewat chat (harian/mingguan), Claude yang memasukkan datanya. |
| Void | Kasir tidak boleh membatalkan atau mengubah sendiri. Nota lunas terkunci. Kasir hanya bisa mengajukan batal dengan alasan; pemilik yang menyetujui. Setelah disetujui, kasir membuat nota baru. |
| Diskon / ubah harga | Kebebasan kasir dibatasi; semua perubahan tercatat. |
| Pembangunan | Diserahkan ke Claude, dengan syarat aman, tidak bergantung POS lain, dan otomatis. |

## 6. Rancangan

### 6.1 Peran
- **pemilik**: semua hak, termasuk menyetujui void, mengatur menu/harga/metode bayar/diskon, stok, laporan, menyetujui HP baru, dan staf.
- **kasir**: membuat nota, mengirim kode/WA, mengajukan void, setoran kas, dan melihat nota miliknya hari ini. Kasir tidak bisa melihat laporan omzet keseluruhan dan tidak bisa mengubah menu, stok, atau harga.
- **Claude** (lewat kunci rahasia di environment): mencatat stok masuk dan hitung stok atas perintah pemilik, membaca laporan, dan mengirim omzet ke Dompet Koi. Setiap barisnya ditandai `source = 'claude'`.

Peran memakai `kk_staff` yang sudah ada. POS dan Admin Kolam Koi memakai akun yang sama.

### 6.2 Keamanan login
- Login dengan email + kata sandi (Supabase Auth), akun dari `kk_staff`.
- **HP baru harus disetujui pemilik sekali.** Saat login pertama di sebuah HP, POS membuat ID perangkat acak (disimpan di HP) dan mengajukannya. Sebelum disetujui pemilik, HP itu belum bisa membuat nota. Pemilik bisa mencabut HP. *(Keputusan Claude: menyeimbangkan "bisa pindah HP" dengan "tidak bisa dipakai dari HP sembarangan".)*
- **Pemilik wajib memakai verifikasi 2 langkah** (TOTP Supabase, aplikasi Google Authenticator) untuk tindakan pemilik, termasuk fungsi pemilik di Admin Kolam Koi (`kk_reset_pin`, `kk_set_staff`). Fungsi pemilik mengecek `aal2` di JWT. Menjual tidak butuh 2 langkah, jadi pemilik tetap bisa ikut melayani. *(Keputusan Claude.)*
- Logout otomatis setelah 30 menit tanpa aktivitas. Logout ditolak selama masih ada nota offline yang belum terkirim.
- Kasir tidak bisa login di dua HP sekaligus. *(Opsional, pembangun boleh menunda.)*
- Halaman memakai Content-Security-Policy ketat; tanpa skrip dari luar kecuali yang di-vendor.

### 6.3 Data (project Kolam Koi, awalan `pos_`)
Skema rinci diserahkan ke pembangun. Kebutuhannya:
- **Menu**: item (nama, kategori, aktif), varian/ukuran dengan harga, dan resep per varian (bahan + takaran). Perubahan harga tidak menimpa histori; nota menyimpan nama dan harga saat terjual.
- **Metode bayar**: daftar (Tunai, QRIS GoPay, QRIS ShopeePay, Transfer BCA, ...), aktif/nonaktif, dan wajib foto atau tidak. Semua metode wajib foto bawaan.
- **Nota**: nomor nota, kasir, perangkat, waktu dibuat di HP, waktu diterima server, flag offline, baris item, subtotal, diskon (+alasan, +siapa), total, metode bayar, uang diterima/kembalian untuk tunai, foto bukti, nomor HP pelanggan (opsional), status (`lunas` / `batal`).
- **Pengajuan void**: nota, alasan, pengaju, waktu, penyetuju, waktu setuju/tolak.
- **Setoran kas / sesi kasir**: buka (modal awal), tutup (uang dihitung + foto), selisih terhadap total tunai sistem.
- **Bahan**: nama, satuan dasar (g/ml/pcs), satuan beli (kaleng 490 g, dst.), harga per satuan terakhir, batas minimum.
- **Pergerakan stok**: masuk (belanja), keluar (otomatis dari nota), hitung (opname), koreksi; plus siapa dan sumbernya (`app` / `claude`).
- **Jejak audit**: satu tabel log umum (tabel, id, aksi, nilai lama, nilai baru, user, waktu, sumber), diisi oleh fungsi, bukan oleh klien.

Semua tabel: RLS aktif. Policy select: kasir hanya melihat nota miliknya hari ini; pemilik melihat semua. Tidak ada policy tulis. Bucket storage foto bersifat **privat**: kasir hanya bisa mengunggah ke folder notanya sendiri, hanya staf yang bisa membaca, dan foto ditampilkan lewat signed URL.

### 6.4 Alur jual (kasir)
1. Kasir mengetuk menu (tombol besar bergambar/berwarna), memilih ukuran, dan jumlah.
2. Ketuk **Bayar** → pilih metode → untuk tunai ketik uang diterima, kembalian tampil.
3. **Foto bukti wajib** (kamera HP langsung; gambar dikecilkan ke ±40 KB di HP).
4. Opsional: nomor HP pelanggan. Kalau nomor itu member Kolam Koi, namanya tampil.
5. Ketuk **Lunas** → satu panggilan fungsi `pos_checkout` di server yang, dalam satu transaksi: mengecek peran dan perangkat, menghitung ulang total dari harga di server (harga dari klien diabaikan), menyimpan nota, mengurangi stok sesuai resep, membuat baris `kk_receipts`, dan membuat kode klaim.
6. Layar menampilkan QR kode klaim + tombol **Kirim WA** (teks: rincian, total, link `…/kolam/?kode=XXXX`).
7. Nota terkunci. Tidak ada tombol ubah.

### 6.5 Kode klaim Kolam Koi
- Saat ini belum ada fungsi pembuat kode (`kk_issue_code` tidak ada). Pembuatan kode menjadi bagian dari `pos_checkout`. Kalau perlu dipisah, buat satu fungsi `kk_issue_code` yang hanya dipanggil dari `pos_checkout`, tidak di-grant ke klien. **Hanya ada satu jalur.**
- Kode: 10 karakter dari alfabet 31 huruf/angka tanpa yang mirip (0/O, 1/I/L), dari pembangkit acak kriptografis (±49 bit). Dicetak `XXXXX-XXXXX`.
- **Server hanya menyimpan hash kode (SHA-256)**, bukan kodenya, supaya staf yang membaca `kk_receipts` tidak bisa melihat kode pelanggan lain.
- `kk_claim` diperluas agar menerima kode (dicocokkan lewat hash); jalur nomor nota + total tetap ada selama masa transisi ESB, lalu dimatikan pemilik dengan satu pengaturan. Batas 10 kali salah per hari tetap berlaku.
- Halaman Kolam Koi: isian kode, scan QR, dan membaca `?kode=` dari link WA.
- **Anti-panen oleh kasir** *(keputusan Claude)*:
  - **Kode terikat nomor HP:** kalau kasir mengisi nomor HP pelanggan (jalur WA), kode hanya bisa diklaim akun member dengan nomor itu. Kode ini berlaku 7 hari.
  - **Kode tanpa nomor HP** (jalur QR di layar) berlaku hanya 2 jam, karena pelanggan memindainya saat itu juga.
  - `kk_staff` diberi kolom nomor HP. Akun member dengan nomor HP staf tidak bisa mengklaim kode dari nota yang dibuat staf itu sendiri.
  - Laporan pemilik menandai klaim yang terjadi sangat cepat dari perangkat/jaringan yang sama, atau oleh member yang sering mengklaim nota dari kasir yang sama.
- Menu "Daftarkan nota" manual di Admin Kolam Koi ditutup untuk kasir (khusus pemilik), dan dimatikan sepenuhnya setelah ESB berhenti.
- Jumlah tarikan tetap dihitung dari `kk_tiers` berdasarkan total nota.

### 6.6 Offline
- Halaman dan menu disimpan di HP (service worker + IndexedDB).
- Saat offline, nota disimpan di antrean lokal lengkap dengan foto. Kode klaim dibuat di HP dengan `crypto.getRandomValues`, lalu dikirim bersama nota dan disimpan server sebagai hash. QR/WA tetap bisa ditunjukkan; klaim berhasil setelah nota sampai di server (halaman Kolam Koi sudah punya daftar "nota belum tercatat, cek lagi").
- Antrean dikirim otomatis begitu online. Server menolak duplikat (ID nota lokal unik).
- Total yang disimpan adalah **total yang tercatat di HP** (uang yang benar-benar diterima). Kalau berbeda dari hitungan server, nota ditandai untuk diperiksa pemilik, tapi kodenya tidak ditahan.
- Saat offline: diskon hanya dari daftar yang sudah tersimpan di HP. Voucher `TK-` **tidak bisa** dipakai saat offline, karena tidak bisa dicek sudah terpakai atau belum. Nota dari HP yang dicabut saat offline tetap diterima, tapi ditahan (kode belum aktif) sampai pemilik menyetujui.
- Nota offline ditandai di laporan, beserta jeda antara waktu di HP dan waktu diterima. Harga untuk nota offline tetap dicek server terhadap daftar harga yang berlaku pada waktu itu; kalau beda, nota ditandai untuk diperiksa pemilik.
- Logout ditolak selama antrean belum kosong.

### 6.7 Void
1. Kasir membuka nota → **Ajukan batal** → pilih/ketik alasan.
2. Pemilik mendapat tanda di layarnya (dan Claude bisa memberi tahu lewat ringkasan).
3. Pemilik menyetujui atau menolak. Kalau disetujui: status `batal`, stok dikembalikan, kode klaim mati, nota tetap terlihat dicoret di laporan.
4. Kalau kode sudah diklaim: kartu hasil tarikan dari nota itu diambil kembali bila masih ada di inventaris member; bila sudah ditukar, pemilik diberi peringatan dan dicatat.

### 6.8 Diskon dan harga
- Kasir tidak bisa mengetik harga bebas.
- Diskon hanya dari daftar diskon yang dibuat pemilik (misalnya "Teman Tarik 10%", "Voucher Kolam Koi"), masing-masing tercatat di nota beserta nama kasir.
- Voucher hadiah Kolam Koi (`TK-XXXXX`) bisa dipakai langsung di POS: kasir scan/ketik kode, item gratis masuk nota, dan `kk_use_voucher` dipanggil dalam transaksi yang sama. *(Keputusan Claude; menyatukan dua layar kasir.)*
- Perubahan menu/harga hanya oleh pemilik, tercatat di jejak audit.

### 6.9 Shift dan serah terima kas
Kasir bekerja per **shift** dengan satu laci bersama. Uang tunai diserahterimakan saat ganti shift.
- **Buka shift:** kasir mengetik modal awal di laci (shift pertama) atau menerima laci dari shift sebelumnya.
- Selama shift, nota tercatat atas nama kasir yang login. Hanya satu shift yang terbuka dalam satu waktu.
- **Serah terima:** kasir yang pulang mengetik uang tunai yang dihitung dan memotret laci. Kasir berikutnya menghitung ulang dan mengetik angkanya sendiri. Kalau dua angka itu berbeda, langsung ditandai. Kedua nama, kedua angka, dan jamnya tercatat.
- **Tutup toko:** sama seperti serah terima, tanpa kasir berikutnya.
- Laporan pemilik per shift: tunai seharusnya (modal + tunai masuk) vs dihitung, dan selisihnya, beserta siapa yang memegang laci.

### 6.10 Stok
- Data awal bahan, satuan, dan harga diambil dari sheet "Database Bahan & HPP" (26 bahan; resep 14 oz versi A/B/C; 22 oz = bahan ×1,6 + cup/es 22 oz).
- Setiap nota mengurangi stok sesuai resep varian yang terjual.
- Stok masuk dan hitung stok diinput Claude dari chat pemilik, atau oleh pemilik di menu Stok. Claude selalu menyebut ulang angka dalam satuan dasar sebelum menyimpan.
- Laporan selisih: stok seharusnya vs dihitung, per bahan, dinyatakan juga dalam "± berapa cup".
- Peringatan stok menipis di layar pemilik.
- Belanja bahan bisa sekaligus dicatat Claude ke Dompet Koi (buku toko, "Bahan baku" / "Cup & kemasan").

### 6.11 Laporan harian (pemilik)
Omzet, jumlah nota, rata-rata per nota, per metode bayar, per kasir, menu terlaris, diskon, nota batal, nota offline, selisih kas, selisih stok terakhir, dan kode klaim yang dipakai/tidak dipakai. Pemilik bisa memilih tanggal.

### 6.12 Dompet Koi
- Database Dompet Koi tetap terpisah.
- **Otomatis:** sebuah tugas terjadwal Claude berjalan tiap malam (±23.30 WITA), membaca omzet hari itu dari POS, lalu mencatat satu transaksi `toko / masuk / Omzet harian` di Dompet Koi dengan catatan "POS: N nota (dicatat Claude)". Sebelum mencatat, tugas mengecek bahwa tanggal itu belum dicatat, supaya tidak dobel. Butuh environment yang menyimpan kunci kedua database.
- **Cadangan:** pemilik bisa minta di chat "kirim omzet kemarin ke Dompet Koi".
- Tombol di POS yang login ke Dompet Koi tidak dibuat di tahap 1. *(Keputusan Claude: menghindari dua login di satu halaman.)*

### 6.13 Tampilan
- Mengikuti warna brand: hijau koi `#0E4D32`, marun `#7A1F2B`, emas `#C9A24B`, krem `#F6EFDF`.
- Mobile-first, tombol besar, bisa dipakai satu tangan, dan bisa dipasang ke layar utama (manifest + ikon).
- Layar kasir: Jual · Nota shift ini · Serah terima / tutup. Layar pemilik menambah: Laporan · Void · Menu · Stok · Perangkat · Staf.

### 6.14 Peralihan dari ESB
- **Urutan pembangunan:** (1) inti: login, menu, jual, foto, kode Kolam Koi + WA, void, shift/serah terima kas, laporan harian; (2) stok dan selisih stok; (3) kirim otomatis ke Dompet Koi.
- Launching 29 Nov tetap memakai ESB.
- Minggu berikutnya: POS dipakai berdampingan selama 2–3 hari, lalu angkanya dibandingkan.
- Selama masa berdampingan, **POS yang memberi kode Kolam Koi**. Kasir tidak lagi mendaftarkan nota ESB di Admin Kolam Koi, supaya tidak ada tarikan ganda. Omzet ke Dompet Koi tetap dari ESB, seperti sekarang. Sinkron otomatis POS → Dompet Koi baru dinyalakan setelah ESB berhenti. *(Keputusan Claude.)*
- Menu "Daftarkan nota" langsung menjadi khusus pemilik begitu POS dipakai.
- Setelah cocok, ESB berhenti dan jalur nota + total di Kolam Koi dimatikan.

## 7. Yang masih dibutuhkan dari pemilik (data, bukan rancangan)
- Harga jual Milo, Matcha, dan Houjicha Tarik (14 oz & 22 oz); Teh Tarik sudah ada (Rp15.000 / Rp22.000).
- Menu bagel & wrap: nama, harga, dan bahan.
- Versi resep yang dipakai (A, B, atau C).
- Daftar metode bayar awal (nama bank untuk transfer).
- Email staf (Ocha, dll.).

## 8. Diserahkan ke pembangun
- Skema tabel rinci, nama fungsi selain yang disebut di atas, dan format nomor nota.
- Teknik kompresi foto dan struktur folder storage.
- Strategi cache service worker.
- Pengujian: fungsi SQL diuji di Postgres lokal (dengan tiruan `auth.uid()`/JWT), dan alur di browser diuji dengan Playwright terhadap database uji, termasuk skenario offline, void, kasir mencoba memanggil fungsi pemilik, dan klien mencoba menulis tabel langsung.
- Foto dikecilkan ±40 KB. Foto lebih dari 3 bulan dihapus otomatis (data nota tetap ada). Laporan pemilik menampilkan pemakaian storage, dan Claude memberi peringatan di 70%. Volume saat ini ±10 nota/hari (23 Nov: 9 bill). *(Keputusan Claude.)*

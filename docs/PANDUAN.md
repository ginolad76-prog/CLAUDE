# Dompet Koi: cara memasang

Dompet Koi adalah website untuk mencatat uang keluarga dan Toko Teh Tjap Dua Koi. Kamu dan istri masuk dengan email masing-masing, lalu melihat data yang sama. Kalau satu orang mencatat, HP yang lain langsung ikut berubah.

Isi folder ini:

| File | Isinya |
|---|---|
| `index.html` | Websitenya |
| `config.js` | Tempat menempel alamat dan kunci Supabase |
| `schema.sql` | Struktur database dan aturan akses |
| `manifest.webmanifest`, `icon.svg` | Supaya bisa dipasang di layar utama HP seperti aplikasi |

Total waktu sekitar 15 menit.

## 1. Buat database di Supabase (gratis)

1. Buka https://supabase.com, daftar, lalu klik **New project**. Beri nama `dompet-koi`, buat password database (simpan baik-baik), dan pilih region **Southeast Asia (Singapore)**.
2. Tunggu sekitar 2 menit sampai project siap.
3. Di menu kiri, buka **SQL Editor** lalu **New query**. Tempel seluruh isi `schema.sql`, kemudian klik **Run**. Hasilnya harus "Success".
4. Buka **Project Settings → API**. Salin dua hal:
   - **Project URL** (contoh `https://abcdefgh.supabase.co`)
   - **anon public** key (yang panjang). **Jangan** pakai `service_role`.

## 2. Isi config.js

Buka `docs/config.js`, lalu tempel dua nilai tadi:

```js
window.DOMPET_CONFIG = {
  SUPABASE_URL: "https://abcdefgh.supabase.co",
  SUPABASE_ANON_KEY: "eyJhbGciOi..."
};
```

Kunci `anon` memang boleh terlihat publik. Data tetap aman karena database hanya mengizinkan anggota keluarga membaca dan menulis datanya sendiri.

Bisa juga minta Claude untuk mengisikannya: kirim URL dan anon key, nanti Claude yang commit.

## 3. Pasang website di GitHub Pages

1. Di GitHub, buka repo `ginolad76-prog/claude` → **Settings → Pages**.
2. Di bagian **Source** pilih **Deploy from a branch**. Pilih branch yang berisi folder `docs` (misalnya `main` setelah perubahan ini digabung), lalu folder **/docs**. Klik **Save**.
3. Tunggu 1–2 menit. Alamat websitenya muncul di halaman itu, biasanya `https://ginolad76-prog.github.io/claude/`.

GitHub Pages gratis untuk repo **public**. Kalau repo ini private dan belum berlangganan GitHub Pro, ada dua pilihan: jadikan repo public (aman, karena repo ini tidak berisi data keuangan), atau unggah folder `docs` ke https://app.netlify.com/drop.

## 4. Sambungkan alamat website ke Supabase

Supabase → **Authentication → URL Configuration**:

- **Site URL**: alamat website dari langkah 3.
- **Redirect URLs**: tambahkan alamat yang sama.

Langkah ini membuat tautan konfirmasi di email pendaftaran kembali ke website kalian.

## 5. Mulai pakai

1. Kamu: buka website → **Daftar baru** → konfirmasi email → **Masuk** → isi nama panggilan → **Buat dompet**.
2. Buka **Atur** dan salin **kode undangan** (6 huruf). Kirim ke istri.
3. Istri: buka website yang sama → **Daftar baru** dengan emailnya sendiri → **Masuk** → isi nama panggilan → masukkan kode → **Gabung**.
4. Pasang di layar utama HP:
   - **Android (Chrome)**: menu ⋮ → **Tambahkan ke layar utama**.
   - **iPhone (Safari)**: tombol Bagikan → **Tambahkan ke Layar Utama**.

## Isi website

- **Ringkasan**: pengeluaran keluarga dibandingkan batas Rp9 juta per bulan, omzet Toko Teh dibandingkan target Rp1 juta per hari, uang keluarga per kategori, dan sisa pinjaman mama.
- **Catat**: pilih Keluarga atau Toko Teh, uang keluar atau masuk, lalu jumlah, kategori, tanggal, dan catatan.
- **Riwayat**: semua catatan per bulan, lengkap dengan siapa yang mencatat. Catatan juga bisa dihapus dari sini.
- **Anggaran**: batas bulanan per kategori keluarga. Sudah terisi Cicilan mama Rp1.400.000 dan Langganan (Claude dll) Rp500.000.
- **Atur**: kode undangan, nama panggilan, target bulanan, target harian, dan total pinjaman.

Paket gratis Supabase cukup untuk pemakaian keluarga. Satu hal yang perlu diingat: project gratis akan dijeda kalau tidak dipakai selama 7 hari. Selama website dibuka setiap hari, project tetap aktif.

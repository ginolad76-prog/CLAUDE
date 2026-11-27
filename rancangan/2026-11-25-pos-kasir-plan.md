# Kasir Koi (POS) — Rencana Pembangunan Tahap 1 (Inti)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Kasir berbasis browser di `tokotehtjapduakoi.github.io/kasir/` yang mencatat setiap nota atas nama kasir yang login, wajib foto bukti, mengunci nota yang sudah lunas, memberi kode klaim Kolam Koi, tetap jalan saat offline, memakai shift dengan serah terima kas, void lewat persetujuan pemilik, dan laporan harian.

**Architecture:** Semua data ada di project Supabase **Kolam Koi** (tabel awalan `pos_`, plus perubahan kecil pada `kk_*`). Klien hanya memanggil fungsi RPC `security definer`; tidak ada akses tabel langsung. Front-end memakai HTML + JS biasa seperti `kolam/`, dengan service worker + IndexedDB untuk mode offline. Pengujian memakai Postgres 16 lokal dengan tiruan skema Supabase (`auth`, `storage`, role `anon`/`authenticated`), server tiruan Node kecil yang meniru endpoint REST/Auth/Storage yang dipakai `supabase-js`, dan Playwright.

**Tech Stack:** Postgres 16 (plpgsql, pgcrypto), Supabase Auth/Storage, `supabase-js` 2.45.4 (sudah di `kolam/vendor/`), `qrcode-generator` 1.4.4 (vendor), Python 3 + pytest (uji SQL lewat `psql`), Node 22 + `pg` 8 (server tiruan), Playwright (sudah terpasang).

**Spec:** `rancangan/2026-11-25-pos-kasir-design.md` (repo `ginolad76-prog/claude`). Baca bersama rencana ini.

**Repo kerja:** `tokotehtjapduakoi/tokotehtjapduakoi.github.io`, cabang `claude/pos-toko-teh-tjap-dua-koi-1mze9t`. Semua path di bawah relatif ke repo ini kecuali disebut lain.

**Di luar tahap 1** (rencana terpisah nanti): stok & selisih stok (spec 6.10); sinkron otomatis ke Dompet Koi (6.12); hapus otomatis foto >3 bulan.

## Global Constraints

- Hanya publishable key di kode website. Tidak ada kunci secret/service_role di file mana pun.
- RLS aktif di **semua** tabel baru. Tidak ada grant insert/update/delete tabel ke `anon`/`authenticated`. Semua perubahan lewat fungsi `security definer set search_path = public` yang mengecek peran.
- Grant ditulis eksplisit: `revoke execute on all functions in schema public from public, anon, authenticated;` lalu grant per fungsi (pola sama seperti akhir `kolam/setup.sql`).
- `kasir/setup.sql` dan `kolam/setup.sql` aman dijalankan ulang (`create ... if not exists`, `create or replace`, `drop policy if exists`).
- Klien POS hanya memakai `sb.rpc(...)`, `sb.auth.*`, dan `sb.storage.from('bukti').upload(...)/createSignedUrl(...)`. Tidak ada `sb.from(table)`.
- Zona waktu "hari ini" dan laporan: `Asia/Makassar` (WITA).
- Uang dalam rupiah, `integer`.
- Setiap void, diskon, perubahan harga/menu/metode bayar/perangkat/staf menulis baris `pos_audit` (tabel, id baris, aksi, nilai lama, nilai baru, `auth.uid()`, `now()`, sumber `app`/`claude`).
- Fungsi khusus pemilik mewajibkan `kk_is_owner()` **dan** `(auth.jwt()->>'aal') = 'aal2'`.
- Kode klaim: 10 karakter dari alfabet `ABCDEFGHJKMNPQRSTUVWXYZ23456789` (31 karakter), dibuat dengan `gen_random_bytes` (server) / `crypto.getRandomValues` (HP), ditampilkan `XXXXX-XXXXX`, disimpan server **hanya** sebagai `encode(digest(kode_tanpa_strip,'sha256'),'hex')`.
- Masa berlaku kode: 7 hari kalau terikat nomor HP, 2 jam kalau tidak.
- Foto bukti: JPEG, sisi terpanjang 960 px, target ≤ 40 KB (turunkan kualitas 0.7 → 0.4 sampai muat). Bucket `bukti` privat.
- Logout otomatis setelah 30 menit tanpa aktivitas; logout ditolak selama antrean offline belum kosong.
- Bahasa antarmuka: Bahasa Indonesia sederhana. Warna: hijau `#0E4D32`, marun `#7A1F2B`, emas `#C9A24B`, krem `#F6EFDF`.
- Halaman `kasir/` memakai `<meta name="robots" content="noindex,nofollow">` dan CSP: `default-src 'self'; img-src 'self' blob: data: https://*.supabase.co; connect-src 'self' https://*.supabase.co; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; script-src 'self'`.

## Review Focus

1. **Dua HP mengirim nota yang sama dua kali** (antrean dikirim ulang setelah koneksi putus di tengah jalan) → server tidak boleh mencatat nota ganda; panggilan kedua mengembalikan nota yang sama. *(Diuji di Task 4: `test_checkout_idempoten`.)*
2. **Pelanggan mengetik kode dengan huruf kecil, spasi, atau tanpa strip** → kode tetap diterima. *(Task 2: `test_klaim_kode_dinormalisasi`.)*
3. **HP mati atau tab ditutup saat foto sedang diunggah offline** → nota dan fotonya tetap ada di antrean saat aplikasi dibuka lagi. *(Task 10: `antrean bertahan setelah reload`.)*
4. **Kasir membuka dua tab dan mencoba menutup shift dua kali / membuka shift saat shift lain masih terbuka** → ditolak dengan pesan jelas. *(Task 5: `test_shift_ganda_ditolak`.)*
5. **Kasir mencoba memanggil fungsi pemilik, atau menulis tabel langsung lewat REST** → ditolak. *(Task 3: `test_tabel_tidak_bisa_ditulis_klien`; Task 6: `test_kasir_tidak_bisa_setujui_void`.)*

---

## Peta file

| File | Tanggung jawab |
|---|---|
| `kolam/setup.sql` (ubah) | `kk_staff.phone`, kolom kode di `kk_receipts`, `kk_settings`, `kk_claim_code`, refactor undian ke `kk__draw`, `kk_add_receipt(s)`/`kk_delete_receipt` khusus pemilik, `aal2` untuk fungsi pemilik |
| `kasir/setup.sql` | Semua tabel, policy, bucket, dan fungsi `pos_*` |
| `kasir/index.html`, `kasir/kasir.css` | Kerangka halaman, gaya |
| `kasir/kasir.js` | Status aplikasi, router layar, layar kasir & pemilik |
| `kasir/kode.js` | Buat kode, normalisasi, hash, URL klaim, QR SVG, teks WA |
| `kasir/foto.js` | Ambil & kecilkan foto |
| `kasir/antrean.js` | Antrean IndexedDB + kirim ulang |
| `kasir/sw.js`, `kasir/manifest.webmanifest`, `kasir/ikon.svg` | Offline & pasang ke layar utama |
| `kasir/config.js` | `window.KASIR_CONFIG` (URL + publishable key yang sama dengan Kolam Koi) |
| `kasir/PANDUAN.md` | Panduan pasang dari HP |
| `kolam/app.js`, `kolam/index.html` (ubah) | Terima `?kode=` dan isian kode |
| `kolam/admin/admin.js` (ubah) | Tab Nota khusus pemilik |
| `kolam/vendor/qrcode-generator-1.4.4.js` | Library QR |
| `_uji/supabase_tiruan.sql` | Tiruan `auth`, `storage`, role |
| `_uji/db.py`, `_uji/conftest.py` | Bantu pytest: DB sementara, `sebagai(user, aal)` |
| `_uji/test_*.py` | Uji SQL |
| `_uji/server_tiruan.mjs`, `_uji/package.json` | Server REST/Auth/Storage tiruan untuk Playwright |
| `_uji/e2e/*.spec.mjs` | Uji browser |

---

### Task 1: Harness uji (Supabase tiruan)

**Files:**
- Create: `_uji/supabase_tiruan.sql`, `_uji/db.py`, `_uji/conftest.py`, `_uji/test_harness.py`, `_uji/README.md`

**Interfaces:**
- Produces:
  - `supabase_tiruan.sql`: role `anon`, `authenticated` (nologin), `authenticator`; schema `auth` dengan tabel `auth.users(id uuid pk default gen_random_uuid(), email text unique, encrypted_password text, raw_user_meta_data jsonb default '{}', created_at timestamptz default now(), updated_at timestamptz)`; fungsi `auth.uid()` = `nullif(current_setting('request.jwt.claims', true)::jsonb->>'sub','')::uuid`, `auth.jwt()` = `coalesce(nullif(current_setting('request.jwt.claims', true),''),'{}')::jsonb`; schema `storage` dengan `storage.buckets(id text pk, name text, public bool)`, `storage.objects(id uuid pk default gen_random_uuid(), bucket_id text, name text, owner uuid, created_at timestamptz default now())`, RLS aktif, fungsi `storage.foldername(name text) returns text[]` = `string_to_array(name,'/')` tanpa elemen terakhir; `create extension pgcrypto with schema extensions`.
  - `db.py`: `class Db` dengan `Db.baru() -> Db` (buat database baru dari cluster sementara, jalankan `supabase_tiruan.sql`, `kolam/setup.sql`, lalu `kasir/setup.sql` bila ada), `db.sql(q: str, *, sebagai: dict|None=None) -> list[tuple]` (lewat `psql -At -F '\t'`; bila `sebagai` diberikan: `set role authenticated; select set_config('request.jwt.claims', json, false);` sebelum `q`), `db.user(email, *, peran: str|None=None, phone: str|None=None) -> dict` (insert `auth.users`; isi `kk_staff` bila `peran`; kembalikan klaim `{"sub":id,"role":"authenticated","aal":"aal1","email":email}`), `db.member(phone) -> dict` (insert user `<phone>@member.tjapduakoi.id`, trigger membuat `kk_members`), `aal2(klaim) -> dict`.
  - `conftest.py`: fixture sesi `cluster` (initdb sebagai user `postgres` di direktori sementara, port 54329, socket di direktori itu; dihentikan di akhir), fixture `db` (Db baru per uji).
  - Eksepsi SQL dilempar sebagai `SqlError(message: str)` berisi teks pesan Postgres.

- [ ] **Step 1: Tulis uji `test_harness.py`**
  - `test_kolam_setup_jalan`: `db.sql("select count(*) from kk_cards")` → `[("13",)]`.
  - `test_klaim_nota_lama_masih_jalan`: kasir `k = db.user("k@x.id", peran="pemilik")` → `db.sql("select kk_add_receipt('POS-1',45000)", sebagai=aal2(k))`; member `m = db.member("6281200000001")`; `db.sql("select kk_claim('POS-1',45000)->>'status'", sebagai=m)` → `[("ok",)]`.
  - `test_anon_tidak_bisa_baca_staf`: `db.sql("select * from kk_staff", sebagai={"role":"anon"})` dengan role `anon` melempar `SqlError` berisi `permission denied`.
- [ ] **Step 2: Jalankan** `cd _uji && python3 -m pytest test_harness.py -q` → gagal (belum ada `db.py`).
- [ ] **Step 3: Implementasikan** `supabase_tiruan.sql`, `db.py`, `conftest.py`. `README.md`: satu paragraf cara menjalankan (`python3 -m pytest -q` dari `_uji/`, perlu Postgres 16 di `/usr/lib/postgresql/16/bin`).
- [ ] **Step 4: Jalankan** `python3 -m pytest test_harness.py -q` → `3 passed`. (Uji kedua akan gagal setelah Task 2 karena `kk_add_receipt` jadi khusus pemilik+aal2; itu sudah diantisipasi dengan `peran="pemilik"` dan `aal2`.)
- [ ] **Step 5: Commit** `git add _uji && git commit -m "Uji: harness Supabase tiruan untuk fungsi Kolam Koi & POS"`

### Task 2: Perubahan Kolam Koi (kode klaim, tutup celah nota manual, aal2)

**Files:**
- Modify: `kolam/setup.sql`
- Test: `_uji/test_kolam_kode.py`

**Interfaces:**
- Produces:
  - `kk_staff.phone text` (nullable, format `62…`), `kk_set_staff(p_email text, p_role text, p_name text default '', p_phone text default null)` (signature lama di-drop, grant diperbarui).
  - `kk_receipts` kolom baru: `code_hash text unique`, `bound_phone text`, `expires_at timestamptz`, `voided_at timestamptz`, `pos_nota_id uuid`, `held boolean not null default false`.
  - `kk_settings(id int primary key default 1 check (id=1), legacy_nota_claim boolean not null default true)`, RLS aktif, select untuk `authenticated`, satu baris diisi.
  - `kk__draw(p_member uuid, p_receipt text) returns jsonb` — isi undian lama dari `kk_claim` dipindah ke sini (pity, kartu rahasia, update member); **tidak** di-grant ke siapa pun. Mengembalikan objek sama seperti `kk_claim` status `ok`/`too_small`.
  - `kk_claim(p_nota text, p_total integer)` — perilaku lama; ditolak (`{"status":"not_found"}` tanpa menambah `fails`) bila `legacy_nota_claim = false`, atau bila nota punya `code_hash`, `voided_at`, atau `held`.
  - `kk_claim_code(p_code text) returns jsonb` — normalisasi: huruf besar, buang semua karakter selain `[A-Z0-9]` (spasi, strip). Alfabet sengaja tidak memuat O/0/I/1/L, jadi tidak ada huruf yang mirip; kode yang memuat karakter itu dianggap salah biasa. Status yang dikembalikan: `ok`, `too_small`, `not_found` (tambah `fails`, kembalikan `left`), `used` (+`mine`), `expired`, `wrong_phone` (kode terikat nomor lain; tambah `fails`), `void`, `pending` (nota `held`), `staff_own` (nomor member = `kk_staff.phone` pembuat nota), `blocked`. Grant ke `authenticated`.
  - `kk_issue_code` **tidak dibuat**; kode dibuat di dalam `pos_checkout` (Task 4).
  - `kk_add_receipt`, `kk_add_receipts`, `kk_delete_receipt` → `kk_owner_mfa()`.
  - `kk_owner_mfa() returns boolean` = `kk_is_owner() and coalesce(auth.jwt()->>'aal','') = 'aal2'`; dipakai juga oleh `kk_reset_pin`, `kk_set_staff`.
  - `kk_admin_summary()` menambah `'mfa', coalesce(auth.jwt()->>'aal','') = 'aal2'`.
  - `kk_set_legacy_claim(p_on boolean) returns void` (pemilik+aal2).

- [ ] **Step 1: Tulis uji** di `test_kolam_kode.py` (siapkan baris `kk_receipts` langsung sebagai superuser dengan `code_hash = encode(digest('ABCDE23456','sha256'),'hex')`, `total = 45000`, `expires_at = now()+interval '2 hours'`):
  - `test_klaim_kode_ok`: `kk_claim_code('ABCDE-23456')` → `status = ok`, `pulls = 2`.
  - `test_klaim_kode_dinormalisasi`: `kk_claim_code(' abcde 23456 ')` → `ok`.
  - `test_klaim_kode_sekali`: klaim kedua oleh member lain → `used`, `mine = false`.
  - `test_kode_kedaluwarsa`: `expires_at = now()-interval '1 minute'` → `expired`.
  - `test_kode_terikat_nomor`: `bound_phone='6281200000009'`; member `6281200000001` → `wrong_phone`; member `6281200000009` → `ok`.
  - `test_kode_staf_sendiri`: `created_by` = kasir dengan `phone='6281200000005'`; member nomor itu → `staff_own`.
  - `test_kode_void_dan_held`: `voided_at` terisi → `void`; `held=true` → `pending`.
  - `test_salah_10x_terkunci`: 10× kode acak → panggilan ke-11 `blocked`.
  - `test_nota_manual_khusus_pemilik_mfa`: kasir → `kk_add_receipt` melempar `Khusus pemilik`; pemilik `aal1` → melempar; pemilik `aal2` → berhasil.
  - `test_klaim_lama_bisa_dimatikan`: setelah `kk_set_legacy_claim(false)`, `kk_claim('POS-1',45000)` → `not_found`.
  - `test_klaim_lama_tidak_bisa_pakai_nota_berkode`: nota ber-`code_hash` tidak bisa diklaim lewat `kk_claim` meski nomor & total benar.
- [ ] **Step 2: Jalankan** `python3 -m pytest test_kolam_kode.py -q` → gagal.
- [ ] **Step 3: Implementasikan** di `kolam/setup.sql`. `alter table ... add column if not exists`. Pertahankan isi undian persis (peluang, pity 10/40, kartu rahasia).
- [ ] **Step 4: Jalankan** seluruh uji `python3 -m pytest -q` → semua lulus.
- [ ] **Step 5: Commit** `git commit -am "Kolam Koi: kode klaim acak, nota manual khusus pemilik, verifikasi 2 langkah"`

### Task 3: Skema POS, perangkat, katalog, pengaturan pemilik

**Files:**
- Create: `kasir/setup.sql`
- Test: `_uji/test_pos_dasar.py`

**Interfaces:**
- Produces (tabel, semua RLS aktif, select hanya lewat fungsi kecuali disebut):
  - `pos_devices(id text pk /* acak dari HP */, label text, requested_by uuid, requested_at timestamptz default now(), approved_by uuid, approved_at timestamptz, revoked_at timestamptz)`
  - `pos_items(id bigserial pk, name text, category text, sort int default 0, active bool default true)`
  - `pos_variants(id bigserial pk, item_id bigint references pos_items, name text /* '14 oz' */, price int check (price>=0), active bool default true)`
  - `pos_price_history(variant_id bigint, price int, valid_from timestamptz default now(), set_by uuid)`
  - `pos_pay_methods(id bigserial pk, name text unique, kind text check (kind in ('tunai','qris','transfer')), active bool default true, sort int default 0)` — isi awal: `Tunai/tunai`, `QRIS/qris`, `Transfer bank/transfer`.
  - `pos_discounts(id bigserial pk, name text, kind text check (kind in ('persen','rupiah')), value int, active bool default true)`
  - `pos_audit(id bigserial pk, tbl text, row_id text, action text, old jsonb, new jsonb, by_user uuid, at timestamptz default now(), source text default 'app')`
  - `storage.buckets` baris `('bukti','bukti',false)`; policy `storage.objects`: insert bila `bucket_id='bukti' and kk_is_staff() and (storage.foldername(name))[1] = auth.uid()::text`; select bila `bucket_id='bukti' and kk_is_staff()`. Tidak ada update/delete.
- Fungsi:
  - `pos_device_request(p_device text, p_label text) returns text` — staf; insert bila belum ada; kembalikan status `approved|pending|revoked`.
  - `pos_device_ok(p_device text) returns boolean` — internal (tidak di-grant).
  - `pos_devices_list() returns jsonb` / `pos_device_decide(p_device text, p_approve boolean) returns void` — pemilik+aal2; audit.
  - `pos_catalog() returns jsonb` — staf: `{items:[{id,name,category,variants:[{id,name,price}]}], methods:[{id,name,kind}], discounts:[{id,name,kind,value}], version: <text hash dari isi>}` hanya yang aktif.
  - `pos_item_save(p jsonb) returns bigint`, `pos_variant_save(p jsonb) returns bigint` (perubahan harga menulis `pos_price_history` + audit), `pos_method_save(p jsonb) returns bigint`, `pos_discount_save(p jsonb) returns bigint` — pemilik+aal2; `p` memuat `id` (null = baru) dan kolom tabel; semua menulis `pos_audit` dengan `old`/`new`.
  - `pos_me(p_device text) returns jsonb` — `{role, name, mfa:bool, device:'approved'|'pending'|'revoked'|'unknown', shift: <objek shift terbuka atau null>}` (shift dari Task 5; sampai saat itu `null`).

- [ ] **Step 1: Tulis uji**
  - `test_tabel_tidak_bisa_ditulis_klien`: untuk setiap tabel `pos_*`, `insert`/`update`/`delete` sebagai kasir melempar `permission denied`; `select` langsung mengembalikan 0 baris atau ditolak.
  - `test_semua_tabel_rls`: `select relname from pg_class where relnamespace='public'::regnamespace and relkind='r' and not relrowsecurity` → kosong.
  - `test_perangkat_baru_pending_lalu_disetujui`: kasir `pos_device_request('dev1','HP Ocha')` → `pending`; pemilik aal2 `pos_device_decide('dev1',true)` → kasir `pos_me('dev1')->>'device'` = `approved`; ada baris `pos_audit` `tbl='pos_devices'`.
  - `test_kasir_tidak_bisa_setujui_perangkat`: kasir `pos_device_decide` melempar.
  - `test_ubah_harga_tercatat`: pemilik aal2 simpan varian harga 15000 lalu 16000 → `pos_price_history` 2 baris; `pos_audit` punya `old->>'price'='15000'`, `new->>'price'='16000'`.
  - `test_katalog_hanya_aktif`: item nonaktif tidak muncul di `pos_catalog()`.
  - `test_anon_tidak_bisa_katalog`: role `anon` → ditolak.
  - `test_storage_folder_sendiri`: kasir insert `storage.objects(bucket_id,name)` dengan folder `auth.uid()` → berhasil; folder user lain → ditolak.
- [ ] **Step 2: Jalankan** → gagal.
- [ ] **Step 3: Implementasikan** `kasir/setup.sql` (header komentar cara pakai seperti `kolam/setup.sql`: jalankan **setelah** `kolam/setup.sql`).
- [ ] **Step 4: Jalankan** `python3 -m pytest -q` → semua lulus.
- [ ] **Step 5: Commit** `git add kasir/setup.sql _uji && git commit -m "POS: skema, perangkat, katalog, pengaturan pemilik"`

### Task 4: `pos_checkout` (nota, kode klaim, kunci, idempoten)

**Files:**
- Modify: `kasir/setup.sql`
- Test: `_uji/test_pos_checkout.py`

**Interfaces:**
- Consumes: `pos_device_ok`, tabel Task 3, kolom `kk_receipts` Task 2, shift terbuka dari Task 5 (lihat catatan).
- Produces:
  - `pos_notas(id uuid pk /* dibuat HP */, no text unique /* 'K'||yymmdd||'-'||lpad(seq,3,'0') per hari WITA */, cashier uuid, device text, shift_id bigint, client_at timestamptz, received_at timestamptz default now(), offline bool, subtotal int, discount_id bigint, discount_amt int, total int, server_total int, price_mismatch bool, method_id bigint, cash_received int, change int, photo_path text, customer_phone text, voucher_code text, status text check (status in ('lunas','batal')) default 'lunas', voided_at timestamptz, held bool default false)`
  - `pos_nota_lines(nota_id uuid, variant_id bigint, item_name text, variant_name text, qty int check (qty>0), price int, free bool default false)`
  - `pos_checkout(p jsonb) returns jsonb`. Input:
    ```
    {id: uuid, device: text, client_at: iso, offline: bool,
     lines: [{variant_id, qty}], discount_id: int|null, voucher_code: text|null,
     method_id: int, total: int, cash_received: int|null,
     photo_path: text, customer_phone: text|null, code: text /* 10 karakter, dibuat HP */}
    ```
    Output: `{id, no, total, pulls, code_status:'aktif'|'ditahan', expires_at}`.
    Aturan:
    1. Staf; perangkat disetujui, **kecuali** `offline=true` dan perangkat dicabut setelah `client_at` → nota diterima dengan `held=true` (kode `ditahan`).
    2. Idempoten: bila `id` sudah ada dan `cashier = auth.uid()` → kembalikan output yang sama tanpa perubahan.
    3. Harus ada shift terbuka milik kasir ini (Task 5); sampai Task 5 selesai, uji membuat shift langsung lewat superuser.
    4. `photo_path` wajib, harus diawali `auth.uid()::text || '/'`, dan ada di `storage.objects` bucket `bukti`. Untuk `offline=true`, nota boleh tiba sebelum fotonya (klien mengunggah foto dulu, lalu memanggil checkout; lihat Task 10), jadi tidak ada pengecualian: foto harus sudah ada.
    5. Harga: online → harga varian sekarang; offline → harga dari `pos_price_history` yang berlaku pada `client_at`. `server_total` dihitung dari harga itu dikurangi diskon (persen dibulatkan ke bawah per rupiah). `total` yang disimpan = `p.total`; `price_mismatch = total <> server_total`. Online dan tidak cocok → **tolak** (`Harga berubah, muat ulang menu`).
    6. `voucher_code` (opsional, online saja; offline → tolak): panggil logika `kk_use_voucher` di transaksi yang sama; satu baris item gratis (`free=true`, `price=0`) dari baris pertama ber-`qty`.
    7. Metode `tunai`: `cash_received >= total` wajib, `change = cash_received - total`.
    8. `customer_phone` dinormalisasi ke `62…` atau ditolak bila tidak valid.
    9. `code`: validasi 10 karakter dari alfabet; simpan `kk_receipts(nota = no, total, created_by = auth.uid(), code_hash, bound_phone = customer_phone, expires_at = received_at + (7 hari bila customer_phone, 2 jam bila tidak), pos_nota_id = id, held)`. Bentrok `code_hash` → tolak (`Kode bentrok, coba lagi`), klien membuat kode baru.
    10. `total = 0` boleh hanya bila semua baris gratis (voucher); `kk_receipts` tetap dibuat tetapi `pulls` 0.
  - `pos_my_notas() returns jsonb` — kasir: nota shift terbukanya (no, jam, total, metode, status, ada pengajuan void).
- Tidak ada fungsi yang meng-`update` kolom total/lines/metode setelah insert. Tambahkan trigger `before update on pos_notas` yang menolak perubahan kolom selain `status`, `voided_at`, `held`.

- [ ] **Step 1: Tulis uji**
  - `test_checkout_ok`: 2× Teh Tarik 14 oz Rp15.000, Tunai, uang 50.000 → `total 30000`, `no` cocok `^K\d{6}-001$`, `change 20000`, `pulls 1`, ada `kk_receipts` dengan `code_hash` = sha256 kode dan `nota = no`.
  - `test_checkout_idempoten`: panggil dua kali dengan `id` sama → satu baris `pos_notas`, output sama.
  - `test_harga_dari_klien_diabaikan`: online, `total` 1000 untuk barang Rp30.000 → ditolak.
  - `test_offline_harga_lama`: harga diubah 15000→16000 setelah `client_at`; offline `total` 15000 → diterima, `price_mismatch=false`.
  - `test_offline_harga_beda_ditandai`: offline `total` 14000 → diterima, `price_mismatch=true`.
  - `test_tanpa_foto_ditolak`, `test_foto_milik_orang_lain_ditolak`.
  - `test_perangkat_belum_disetujui_ditolak`; `test_perangkat_dicabut_offline_ditahan` → `code_status='ditahan'`, `kk_receipts.held=true`, dan `kk_claim_code` → `pending`.
  - `test_tanpa_shift_ditolak`.
  - `test_kode_terikat_nomor_7_hari` / `test_kode_tanpa_nomor_2_jam` (cek `expires_at`).
  - `test_nota_terkunci`: superuser mencoba `update pos_notas set total=1` → trigger menolak; tidak ada fungsi yang di-grant untuk mengubah total.
  - `test_voucher_dipakai_sekali`: voucher `TK-…` valid → baris gratis, voucher `used_at` terisi; checkout kedua dengan voucher sama → ditolak; offline dengan voucher → ditolak.
  - `test_tunai_kurang_ditolak`.
- [ ] **Step 2: Jalankan** → gagal.
- [ ] **Step 3: Implementasikan.** Nomor urut harian: `pos_counters(day date pk, seq int)` dengan `insert ... on conflict do update set seq = seq+1 returning seq`.
- [ ] **Step 4: Jalankan** `python3 -m pytest -q` → lulus.
- [ ] **Step 5: Commit** `git commit -am "POS: checkout terkunci dengan kode klaim Kolam Koi"`

### Task 5: Shift & serah terima kas

**Files:**
- Modify: `kasir/setup.sql`
- Test: `_uji/test_pos_shift.py`

**Interfaces:**
- Produces:
  - `pos_shifts(id bigserial pk, cashier uuid, device text, opened_at timestamptz default now(), cash_start int, received_from bigint /* shift sebelumnya */, closed_at timestamptz, cash_counted int, close_photo text, received_count int /* hitungan kasir berikutnya */, received_by uuid, received_at timestamptz)`
  - Aturan "satu laci": hanya **satu** shift terbuka di seluruh toko pada satu waktu.
  - `pos_shift_open(p_device text, p_cash_start int) returns jsonb` — hanya bila tidak ada shift terbuka **dan** tidak ada shift tertutup yang menunggu diterima; `cash_start` wajib ≥ 0.
  - `pos_shift_close(p_cash_counted int, p_photo_path text, p_handover boolean) returns jsonb` — oleh pemilik shift; foto wajib (aturan path sama dengan Task 4). `p_handover=true` → shift menunggu diterima; `false` → tutup toko.
  - `pos_shift_receive(p_device text, p_count int) returns jsonb` — kasir **lain** (atau pemilik); mengisi `received_*` lalu membuka shift baru untuk pemanggil dengan `cash_start = p_count`, `received_from` = shift lama. Kembalikan `{shift, selisih: p_count - cash_counted}`.
  - `pos_shift_expected(p_shift bigint) returns int` (internal) = `cash_start + sum(total)` nota `lunas` metode `tunai` di shift itu.
  - `pos_me` diperbarui: `shift` = shift terbuka milik pemanggil (`{id, opened_at, cash_start}`), plus `handover_waiting: {shift_id, cashier_name, cash_counted}` bila ada.

- [ ] **Step 1: Tulis uji**
  - `test_buka_jual_tutup`: buka 100.000, jual tunai 30.000, tutup dengan hitungan 130.000 → `pos_shift_expected` = 130.000.
  - `test_shift_ganda_ditolak`: kasir B membuka shift saat shift A terbuka → ditolak `Masih ada shift terbuka`; A menutup dua kali → panggilan kedua ditolak.
  - `test_serah_terima`: A tutup `p_handover=true` hitungan 130.000; B `pos_shift_receive` 125.000 → `selisih = -5000`, shift B terbuka `cash_start 125000`; A tidak bisa menerima shiftnya sendiri.
  - `test_buka_ditolak_saat_menunggu_diterima`: setelah serah terima diajukan, `pos_shift_open` ditolak (harus `receive`).
  - `test_tutup_tanpa_foto_ditolak`.
- [ ] **Step 2: Jalankan** → gagal. **Step 3: Implementasikan.** **Step 4:** `python3 -m pytest -q` → lulus (ubah uji Task 4 agar memakai `pos_shift_open` alih-alih insert superuser).
- [ ] **Step 5: Commit** `git commit -am "POS: shift dan serah terima kas"`

### Task 6: Void lewat persetujuan pemilik

**Files:**
- Modify: `kasir/setup.sql`
- Test: `_uji/test_pos_void.py`

**Interfaces:**
- Produces:
  - `pos_void_requests(id bigserial pk, nota_id uuid references pos_notas, reason text not null, requested_by uuid, requested_at timestamptz default now(), decided_by uuid, decided_at timestamptz, approved boolean, cards_note text)`; maksimal satu pengajuan terbuka per nota.
  - `pos_void_request(p_nota uuid, p_reason text) returns bigint` — kasir pembuat nota atau pemilik; alasan ≥ 5 karakter; nota harus `lunas`.
  - `pos_void_pending() returns jsonb` — pemilik: daftar pengajuan terbuka dengan rincian nota, nama kasir, alasan, status klaim.
  - `pos_void_decide(p_req bigint, p_approve boolean) returns jsonb` — pemilik+aal2. Bila disetujui: `pos_notas.status='batal'`, `voided_at=now()`, `kk_receipts.voided_at=now()`; bila nota sudah diklaim: kurangi `kk_inventory` untuk setiap baris `kk_pulls` nota itu selama `qty>0`, kartu yang tidak bisa dikurangi dicatat di `cards_note` dan dikembalikan sebagai `{cards_missing:[...]}`. Audit.

- [ ] **Step 1: Tulis uji**
  - `test_kasir_tidak_bisa_setujui_void`: kasir `pos_void_decide` → ditolak; pemilik aal1 → ditolak.
  - `test_void_disetujui_mematikan_kode`: setujui → status `batal`; `kk_claim_code` → `void`.
  - `test_void_setelah_klaim_tarik_kartu`: member klaim (2 kartu) → setujui → inventori member berkurang 2; bila salah satu kartu sudah ditukar (qty 0) → `cards_missing` berisi kartu itu.
  - `test_void_ditolak_nota_tetap`: pemilik menolak → status tetap `lunas`; pengajuan baru boleh diajukan lagi.
  - `test_void_ganda_ditolak`: dua pengajuan terbuka untuk nota sama → yang kedua ditolak.
  - `test_kasir_lain_tidak_bisa_ajukan`: kasir B mengajukan void nota kasir A → ditolak.
- [ ] **Step 2–4:** jalankan gagal → implementasi → `python3 -m pytest -q` lulus.
- [ ] **Step 5: Commit** `git commit -am "POS: void dengan persetujuan pemilik"`

### Task 7: Laporan harian

**Files:**
- Modify: `kasir/setup.sql`
- Test: `_uji/test_pos_laporan.py`

**Interfaces:**
- Produces: `pos_report(p_day date default null) returns jsonb` — pemilik (aal1 cukup untuk membaca); hari WITA (default hari ini):
  ```
  {day, omzet, notas, avg, by_method:[{name,total,count}], by_cashier:[{name,total,count}],
   top_items:[{item,variant,qty,total}] (10 teratas), discounts:{count,total},
   voids:[{no,total,reason,by,approved_by}], pending_voids:int,
   offline:{count, mismatch:[{no,total,server_total}], held:int},
   shifts:[{cashier,opened_at,closed_at,cash_start,expected,counted,received_count,selisih,selisih_terima}],
   codes:{issued, claimed, expired_unclaimed},
   suspicious:[{no, reason}] /* klaim < 60 detik setelah nota oleh member yang 3+ kali mengklaim nota kasir yang sama dalam 7 hari */,
   storage_mb: numeric /* jumlah ukuran objek bucket bukti bila tersedia, null bila tidak */}
  ```
  Omzet dan jumlah nota tidak menghitung nota `batal`.

- [ ] **Step 1: Tulis uji** `test_laporan_angka`: siapkan 3 nota oleh 2 kasir (tunai 30.000, tunai 15.000, QRIS 22.000), lalu void nota 15.000 → `omzet 52000`, `notas 2`, `by_method` Tunai 30.000/QRIS 22.000, `voids` panjang 1; `test_laporan_khusus_pemilik` (kasir ditolak); `test_laporan_batas_hari_wita` (nota pukul 23.30 WITA masuk hari itu, bukan besok).
- [ ] **Step 2–4:** gagal → implementasi → lulus.
- [ ] **Step 5: Commit** `git commit -am "POS: laporan harian"`

### Task 8: Server tiruan + kerangka halaman kasir (login, perangkat, idle)

**Files:**
- Create: `_uji/server_tiruan.mjs`, `_uji/package.json` (`{"type":"module","dependencies":{"pg":"8.13.1"}}`), `_uji/e2e/login.spec.mjs`, `_uji/e2e/bantu.mjs`
- Create: `kasir/index.html`, `kasir/kasir.css`, `kasir/config.js`, `kasir/kasir.js`

**Interfaces:**
- Produces (server tiruan, `node server_tiruan.mjs --db <conninfo> --port 8787 --web <repo root>`):
  - Menyajikan file statis repo di `/` (supaya halaman `kasir/` dan `kolam/` bisa dibuka).
  - `POST /auth/v1/token?grant_type=password` `{email,password}` → cocokkan `auth.users.encrypted_password` (crypt); kembalikan `{access_token, token_type:'bearer', expires_in:3600, refresh_token, user}`; access token = JWT HS256 dengan rahasia tetap `uji` dan klaim `{sub, role:'authenticated', aal: <'aal2' bila header uji X-Uji-AAL2: 1 atau user email diawali 'pemilik'>, email, exp}`.
  - `POST /auth/v1/token?grant_type=refresh_token`, `GET /auth/v1/user`, `POST /auth/v1/logout`.
  - `POST /rest/v1/rpc/:fn` → dalam transaksi: `set local role authenticated|anon`, `set_config('request.jwt.claims', <klaim>, true)`, `select to_jsonb(public.:fn(<args bernama>))`; kesalahan Postgres → HTTP 400 `{message, code}` seperti PostgREST.
  - `POST /storage/v1/object/:bucket/*path` → insert `storage.objects` dengan role yang sama (policy berlaku), simpan bytes di memori; `POST /storage/v1/object/sign/:bucket/*path` → `{signedURL}`; `GET /storage/v1/object/sign/...` → bytes.
  - Endpoint uji `POST /__uji/offline` `{on:boolean}` membuat semua endpoint selain statis mengembalikan koneksi putus (socket destroy).
- `bantu.mjs`: `siapkanDb()` (pakai cluster pytest yang sama lewat `python3 _uji/db.py --buat` yang mencetak conninfo; skrip ini menambah data contoh: pemilik `pemilik@uji.id`/`rahasia1`, kasir `ocha@uji.id`/`rahasia1` dan `budi@uji.id`/`rahasia1`, menu Teh Tarik 14 oz 15.000 & 22 oz 22.000, Milo Tarik 14 oz 18.000, metode bayar bawaan), `jalankanServer()`, `masuk(page, email)`.
- `kasir/config.js`: `window.KASIR_CONFIG = { supabaseUrl, supabaseKey, kolamUrl: "https://tokotehtjapduakoi.github.io/kolam/" }`; nilai URL/key sama dengan `kolam/config.js`. Uji Playwright menimpa `KASIR_CONFIG` lewat `page.route('**/kasir/config.js', ...)` ke server tiruan.
- `kasir.js` state: `S = {sb, user, me, catalog, device, screen}`; `deviceId()` → `localStorage['kasir.device']` (32 hex dari `crypto.getRandomValues`, dibuat sekali); `label` perangkat = `navigator.userAgent` dipendekkan + input nama opsional.
- Alur: belum login → form email/sandi. Login → `pos_device_request` → `pos_me`. `device !== 'approved'` → layar "Menunggu persetujuan pemilik" + tombol cek lagi. Disetujui → layar Jual (Task 9). Idle 30 menit (tanpa `pointerdown`/`keydown`) → logout, kecuali antrean tidak kosong (Task 10 menyediakan `Antrean.jumlah()`; sebelum itu anggap 0).

- [ ] **Step 1: Tulis uji** `login.spec.mjs`:
  - `kasir baru menunggu persetujuan`: Ocha login → teks "Menunggu persetujuan pemilik".
  - `setelah disetujui masuk layar jual`: setujui via RPC pemilik di uji → "Cek lagi" → terlihat tombol menu "Teh Tarik".
  - `logout otomatis setelah diam 30 menit`: `page.clock.install()` → majukan 31 menit → form login tampil.
  - `bukan staf ditolak`: user tanpa `kk_staff` → pesan "Akun ini bukan staf toko".
- [ ] **Step 2:** `cd _uji && npm install && npx playwright test e2e/login.spec.mjs --trace off` → gagal.
- [ ] **Step 3: Implementasikan** server tiruan dan kerangka halaman (CSP & noindex dari Global Constraints; muat `../kolam/vendor/supabase-2.45.4.js`).
- [ ] **Step 4:** jalankan lagi → `4 passed`.
- [ ] **Step 5: Commit** `git add kasir _uji && git commit -m "Kasir: kerangka halaman, login, persetujuan perangkat"`

### Task 9: Alur jual (menu → bayar → foto → lunas → QR/WA)

**Files:**
- Create: `kasir/kode.js`, `kasir/foto.js`, `kolam/vendor/qrcode-generator-1.4.4.js` (dari tarball npm `qrcode-generator@1.4.4`, file `qrcode.js`, dengan lisensi MIT di header)
- Modify: `kasir/kasir.js`, `kasir/kasir.css`, `kasir/index.html`
- Test: `_uji/e2e/jual.spec.mjs`, `_uji/test_kode_js.mjs` (node:test)

**Interfaces:**
- `kode.js` (global `KasirKode`):
  - `buat(): string` — 10 karakter alfabet, rejection sampling dari `crypto.getRandomValues` (buang byte ≥ 248).
  - `tampil(k: string): string` → `"XXXXX-XXXXX"`.
  - `normal(s: string): string` → huruf besar, buang selain `[A-Z0-9]`.
  - `urlKlaim(k: string): string` → `KASIR_CONFIG.kolamUrl + "?kode=" + tampil(k)`.
  - `qrSvg(text: string): string` (qrcode-generator, error level `M`).
  - `teksWa({no, lines, total, method, kode}): string` — format:
    ```
    Toko Teh Tjap Dua Koi
    Nota {no} · {tanggal jam}
    {qty}× {item} {varian}  Rp{harga×qty}
    ...
    Total Rp{total} ({metode})

    Tarik kartu koi-mu di Kolam Koi:
    {urlKlaim}
    Kode: {XXXXX-XXXXX} (berlaku 7 hari)

    Terima kasih, sampai ketemu lagi!
    ```
  - `linkWa(phone62: string, teks: string): string` → `https://wa.me/{phone62}?text={encodeURIComponent(teks)}`.
- `foto.js` (global `KasirFoto`): `ambil(): Promise<Blob>` — `<input type=file accept="image/*" capture="environment">`; `kecilkan(file: Blob): Promise<Blob>` sesuai Global Constraints.
- Layar Jual: grid tombol item per kategori → sheet varian (ukuran) → keranjang (± qty, hapus baris sebelum bayar) → **Bayar**: pilih metode (tombol), tunai → input uang diterima + tombol cepat (pas, 20rb, 50rb, 100rb) dan kembalian; diskon dari daftar (opsional); voucher `TK-` (opsional, ketik); nomor HP pelanggan (opsional, `inputmode=tel`); **Foto bukti** (wajib; tombol "Lunas" nonaktif sampai ada foto, pratinjau kecil). **Lunas** → unggah foto ke `bukti/{uid}/{nota_id}.jpg` → `pos_checkout` (online) atau antrean (Task 10) → layar Selesai: nomor nota, total, kembalian besar, QR `urlKlaim`, kode teks, tombol **Kirim WA** (hanya bila nomor HP diisi; membuka `linkWa`), tombol **Nota baru**.
- Kalau `pos_checkout` menolak "Harga berubah" → muat ulang katalog dan beri tahu kasir; keranjang dihitung ulang.

- [ ] **Step 1: Tulis uji**
  - `test_kode_js.mjs`: `buat()` 10.000 kali → semua panjang 10 dan hanya alfabet; tidak ada duplikat; `normal(' abcde-23456 ')==='ABCDE23456'`; `tampil('ABCDE23456')==='ABCDE-23456'`; `teksWa` memuat `?kode=ABCDE-23456`.
  - `jual.spec.mjs`:
    - `jual tunai lengkap`: Ocha (disetujui, shift terbuka lewat RPC uji) → Teh Tarik → 14 oz → ×2 → Bayar → Tunai → 50.000 → foto (`setInputFiles` gambar uji 3000×2000) → Lunas → layar menampilkan "Kembalian Rp20.000", nomor `K…-001`, QR `<svg>`; DB: `pos_notas` 1 baris total 30.000; objek storage ≤ 40 KB.
    - `lunas nonaktif tanpa foto`.
    - `kirim WA`: nomor `0812-0000-0001` → tombol Kirim WA `href` diawali `https://wa.me/6281200000001?text=` dan memuat kode.
    - `tidak ada tombol ubah setelah lunas`: layar Selesai dan daftar nota tidak punya kontrol ubah total/item.
- [ ] **Step 2:** jalankan → gagal. **Step 3:** implementasikan. **Step 4:** `node --test test_kode_js.mjs && npx playwright test e2e/jual.spec.mjs --trace off` → lulus.
- [ ] **Step 5: Commit** `git commit -am "Kasir: alur jual, foto bukti, kode klaim QR dan WA"`

### Task 10: Offline (antrean + service worker + pasang ke layar utama)

**Files:**
- Create: `kasir/antrean.js`, `kasir/sw.js`, `kasir/manifest.webmanifest`, `kasir/ikon.svg`
- Modify: `kasir/kasir.js`, `kasir/index.html`
- Test: `_uji/e2e/offline.spec.mjs`

**Interfaces:**
- `antrean.js` (global `Antrean`), IndexedDB `kasir` store `antrean` (key `id`):
  - `simpan(item: {id, payload, foto: Blob, fotoPath, dibuat}): Promise<void>`
  - `jumlah(): Promise<number>`
  - `kirimSemua(sb): Promise<{terkirim:number, gagal:number}>` — urut `dibuat`; per item: unggah foto (409/“already exists” dianggap berhasil) → `pos_checkout` (idempoten) → hapus item. Berhenti di kesalahan jaringan; kesalahan validasi server → tandai item `error` dengan pesan (tetap disimpan, tampil di layar Nota dengan tombol "Laporkan ke pemilik").
  - Pemicu: `online` event, setiap 30 detik saat ada isi, dan saat aplikasi dibuka.
- Alur Lunas: selalu `Antrean.simpan` dulu, lalu coba `kirimSemua`. Bila gagal jaringan → layar Selesai tetap tampil (QR & WA dari kode yang dibuat HP) dengan label "Tersimpan di HP, akan terkirim otomatis"; `payload.offline = true` hanya bila pengiriman pertama gagal.
- Saat offline: voucher `TK-` dinonaktifkan dengan keterangan; katalog dari cache terakhir (`localStorage['kasir.catalog']`).
- `sw.js`: cache-first untuk file `kasir/*`, `kolam/vendor/*`, font; network-only untuk `*.supabase.co`. Versi cache `kasir-v1`.
- Bilah status: titik hijau "Online" / oranye "Offline · N nota menunggu".
- Logout & idle-logout ditolak bila `Antrean.jumlah() > 0` dengan pesan "Masih ada N nota belum terkirim. Sambungkan internet dulu."

- [ ] **Step 1: Tulis uji** `offline.spec.mjs`:
  - `jual saat offline lalu terkirim`: `POST /__uji/offline {on:true}` + `context.setOffline(true)` → jual → layar Selesai "Tersimpan di HP" + QR → DB 0 nota → online → dalam 35 detik (`page.clock`) DB 1 nota `offline=true`.
  - `antrean bertahan setelah reload`: offline → jual → `page.reload()` → bilah "1 nota menunggu" → online → terkirim.
  - `kirim ulang tidak dobel`: server tiruan memutus koneksi **setelah** `pos_checkout` berhasil (opsi `/__uji/putus-setelah-rpc`) → klien mengirim ulang → tetap 1 nota.
  - `logout ditolak saat antrean ada`.
  - `halaman terbuka tanpa internet`: muat sekali, offline, reload → layar Jual tampil.
- [ ] **Step 2–4:** gagal → implementasi → `npx playwright test e2e/offline.spec.mjs --trace off` lulus.
- [ ] **Step 5: Commit** `git commit -am "Kasir: mode offline dan pasang ke layar utama"`

### Task 11: Layar kasir lainnya (shift, nota shift ini, ajukan batal)

**Files:**
- Modify: `kasir/kasir.js`, `kasir/kasir.css`
- Test: `_uji/e2e/shift.spec.mjs`

**Interfaces:**
- Consumes: `pos_shift_open/close/receive`, `pos_me().shift/handover_waiting`, `pos_my_notas`, `pos_void_request`.
- Tab bawah kasir: **Jual · Nota · Kas**.
- Tanpa shift: bila `handover_waiting` → layar "Terima laci dari {nama}: hitung uang di laci" + input → `pos_shift_receive`; tampilkan selisih bila ≠ 0. Bila tidak → "Buka toko: modal awal di laci" → `pos_shift_open`.
- Kas: "Serah terima ke kasir berikutnya" / "Tutup toko" → input hitungan + foto laci (wajib) → `pos_shift_close`.
- Nota: daftar `pos_my_notas` + nota di antrean; ketuk → rincian + foto (signed URL) + **Ajukan batal** (alasan: pilihan "Salah input", "Pelanggan batal", "Lainnya" + teks) → status "Menunggu persetujuan".

- [ ] **Step 1: Tulis uji**: `buka-jual-serah terima-terima`: Ocha buka 100.000 → jual tunai 30.000 → serah terima hitung 130.000 + foto → Budi login (perangkat sendiri disetujui) → layar terima laci → isi 125.000 → tampil "Selisih −Rp5.000"; `ajukan batal`: Ocha ajukan batal nota → status "Menunggu persetujuan", tidak ada tombol hapus.
- [ ] **Step 2–4:** gagal → implementasi → lulus.
- [ ] **Step 5: Commit** `git commit -am "Kasir: shift, serah terima, ajukan batal"`

### Task 12: Layar pemilik (laporan, void, perangkat, menu, verifikasi 2 langkah)

**Files:**
- Modify: `kasir/kasir.js`, `kasir/kasir.css`
- Test: `_uji/e2e/pemilik.spec.mjs`

**Interfaces:**
- Consumes: `pos_report`, `pos_void_pending/decide`, `pos_devices_list/decide`, `pos_*_save`, `pos_catalog`.
- Tab pemilik: **Jual · Laporan · Setujui · Atur** (Setujui = void + perangkat, dengan angka badge).
- **Verifikasi 2 langkah:** layar Atur/Setujui memeriksa `me.mfa`. Belum aal2: bila belum punya faktor → `sb.auth.mfa.enroll({factorType:'totp'})` → tampilkan QR (`totp.qr_code`) + kode rahasia + input 6 angka → `challenge`+`verify`; bila sudah punya → input 6 angka → `challengeAndVerify`. Setelah itu `pos_me` ulang. (Server tiruan memberi aal2 untuk email `pemilik*`; enroll diuji manual di Task 14.)
- Laporan: pemilih tanggal; kartu angka besar (omzet, nota, rata-rata); daftar per metode, per kasir, menu terlaris; bagian peringatan berwarna marun bila ada: void, nota offline beda harga, nota ditahan, selisih kas ≠ 0, klaim mencurigakan.
- Setujui: kartu per pengajuan (nota, item, total, kasir, alasan, foto) → Setujui / Tolak (konfirmasi dua ketuk). Hasil `cards_missing` ditampilkan.
- Atur: Menu (item + varian + harga, aktif/nonaktif), Metode bayar, Diskon, Perangkat (setujui/cabut), dan tautan ke Admin Kolam Koi untuk Staf.

- [ ] **Step 1: Tulis uji**: `pemilik menyetujui void`: siapkan nota + pengajuan → pemilik → Setujui → Setujui → nota tampil dicoret di Laporan, omzet berkurang; `ubah harga tercatat`: Atur → Teh Tarik 14 oz → 16.000 → simpan → `pos_audit` punya old 15000/new 16000; `kasir tidak melihat tab pemilik`: Ocha → tidak ada "Laporan"/"Atur".
- [ ] **Step 2–4:** gagal → implementasi → lulus.
- [ ] **Step 5: Commit** `git commit -am "Kasir: layar pemilik"`

### Task 13: Kolam Koi menerima kode

**Files:**
- Modify: `kolam/app.js`, `kolam/index.html`, `kolam/admin/admin.js`
- Test: `_uji/e2e/kolam.spec.mjs`

**Interfaces:**
- Consumes: `kk_claim_code`, `kk_admin_summary().mfa`, `kk_settings`.
- `kolam/app.js`: kartu "Masukkan nota" menjadi "Masukkan kode" (satu isian `XXXXX-XXXXX`, `autocapitalize=characters`). Bila `kk_settings.legacy_nota_claim` true, tampilkan tautan kecil "Punya nota lama? Masukkan nomor & total" untuk form lama. `?kode=` di URL: simpan di `sessionStorage`, minta login/daftar bila perlu, lalu klaim otomatis dan hapus parameter dari URL (`history.replaceState`). Pesan per status: `expired` "Kode sudah kedaluwarsa", `wrong_phone` "Kode ini untuk nomor HP lain. Masuk dengan nomor yang dipakai saat belanja", `pending` "Nota sedang diperiksa toko. Coba lagi nanti" (masuk daftar tunggu), `void` "Nota ini dibatalkan", `staff_own` "Kode dari nota yang kamu buat sendiri tidak bisa diklaim", `not_found` masuk daftar tunggu seperti sekarang (offline belum tiba).
- `kolam/admin/admin.js`: tab Nota hanya untuk pemilik dengan `mfa` true; tambah sakelar "Klaim nomor nota lama (ESB)" → `kk_set_legacy_claim`. Form Staf menambah isian nomor HP.

- [ ] **Step 1: Tulis uji**: `klaim dari link WA`: buat nota via RPC → buka `/kolam/?kode=XXXXX-XXXXX` sebagai member baru (daftar nomor + PIN) → animasi tarikan tampil, `kk_receipts.claimed_by` terisi, URL tidak lagi memuat `kode`; `kode nomor lain`: pesan wrong_phone; `kasir tidak melihat tab Nota admin`.
- [ ] **Step 2–4:** gagal → implementasi → lulus.
- [ ] **Step 5: Commit** `git commit -am "Kolam Koi: klaim dengan kode dari kasir"`

### Task 14: Panduan pasang, uji menyeluruh, uji di Supabase asli

**Files:**
- Create: `kasir/PANDUAN.md`
- Modify: `kolam/PANDUAN.md` (alur harian baru), `README.md` (tautan ke `kasir/PANDUAN.md`)
- Modify (repo `ginolad76-prog/claude`): `MEMORI.md` (bagian Kasir Koi: alamat, status, cara Claude mencatat), `CLAUDE.md` (cara Claude membaca POS & menyimpan stok nanti)

**Interfaces:**
- `kasir/PANDUAN.md` (gaya sama dengan `kolam/PANDUAN.md`, langkah bernomor, bisa dari HP):
  1. Supabase → SQL Editor: jalankan `kolam/setup.sql` (versi baru) lalu `kasir/setup.sql`.
  2. Authentication → MFA: aktifkan TOTP.
  3. Isi nomor HP staf di Admin Kolam Koi → Staf.
  4. Buka `/kasir/` → login pemilik → aktifkan verifikasi 2 langkah (Google Authenticator) → setujui HP sendiri.
  5. Atur → isi menu, harga, metode bayar (tambah "QRIS GoPay", "QRIS ShopeePay" saat sudah daftar), diskon.
  6. Kasir: login di HP masing-masing → pemilik menyetujui HP → pasang ke layar utama (Chrome: ⋮ → Tambahkan ke layar utama; iPhone Safari: Bagikan → Tambah ke Layar Utama).
  7. Alur harian: buka toko → jual → serah terima/tutup.
  8. Masa berdampingan dengan ESB: jangan daftarkan nota ESB di Admin Kolam Koi; setelah cocok, matikan "Klaim nomor nota lama".
  9. Kalau ada masalah: kasir lupa sandi, HP hilang (cabut perangkat), internet putus.
- Uji di Supabase asli (setelah pemilik menjalankan SQL): Claude meminta kunci secret project Kolam Koi lewat `request_credential` (host `trqjrhgtvvfviwcdhccp.supabase.co`), lalu menjalankan skrip asap `_uji/asap_asli.py` yang: membuat user uji `uji-kasir@…`, menjalankan alur buka shift → checkout → klaim kode → void → laporan lewat REST asli, memeriksa bahwa `anon` tidak bisa memanggil fungsi POS dan tidak bisa membaca tabel, lalu **menghapus semua data uji**. Hasil dilaporkan ke pemilik.

- [ ] **Step 1:** Jalankan seluruh uji: `cd _uji && python3 -m pytest -q && node --test && npx playwright test --trace off` → semua lulus; catat jumlahnya.
- [ ] **Step 2:** Tulis `kasir/PANDUAN.md`, perbarui `kolam/PANDUAN.md` dan `README.md`.
- [ ] **Step 3:** Pindai rahasia: `grep -rnE "service_role|sb_secret_|eyJhbGciOi" --include=*.js --include=*.html --include=*.md . | grep -v _uji/` → kosong.
- [ ] **Step 4:** Commit & push cabang; minta pemilik menjalankan langkah 1–2 panduan; jalankan `_uji/asap_asli.py` terhadap project asli; laporkan hasil.
- [ ] **Step 5:** Perbarui `MEMORI.md`/`CLAUDE.md` di repo `claude`; commit & push.

# Ringkasan simulasi Kasir Koi

> **DATA SIMULASI, bukan data asli.** Angka di bawah dibuat komputer secara acak (tetapi masuk akal) di database uji,
> bukan dari Supabase toko. Tujuannya hanya untuk melihat bentuk laporan setelah toko jalan beberapa bulan.

Isi simulasi: 1 September 2026 sampai 25 November 2026, 2 kasir (Ocha dan Budi, bergantian shift pagi dan sore),
menu Teh/Milo/Matcha/Houjicha Tarik 14 oz dan 22 oz, Bagel, Wrap; bayar Tunai, QRIS, Transfer bank.
Sabtu-Minggu dan tanggal gajian (1 dan 25) dibuat lebih ramai. Uang laci tidak diambil pemilik (modal = hitungan kemarin).

## Bulan lalu (Oktober 2026)

1 Oktober 2026 sampai 31 Oktober 2026 (31 hari)

- Omzet: **Rp27.570.900**
- Jumlah nota: **795**
- Rata-rata per nota: Rp34.680
- Rata-rata per hari: Rp889.384
- Hari terbaik: 10 Oktober 2026, Rp1.495.800

Per metode bayar:
- Tunai: Rp16.707.600 (482 nota)
- QRIS: Rp9.394.500 (274 nota)
- Transfer bank: Rp1.468.800 (39 nota)

Per kasir:
- Budi: Rp13.871.300 (403 nota)
- Ocha: Rp13.699.600 (392 nota)

5 menu terlaris:
1. Teh Tarik 14 oz: 269 porsi, Rp4.035.000
2. Bagel Biasa: 201 porsi, Rp3.618.000
3. Teh Tarik 22 oz: 187 porsi, Rp4.114.000
4. Wrap Biasa: 165 porsi, Rp3.630.000
5. Milo Tarik 14 oz: 126 porsi, Rp2.268.000

- Nota batal: 8 nota (Rp265.000)
- Diskon: 28 nota (Rp100.100)
- Selisih kas: kurang Rp1.500, di 4 dari 62 shift
- Nota offline: 16
- Kode klaim kartu: 323 dari 795 sudah diklaim

## Seluruh simulasi

1 September 2026 sampai 25 November 2026 (86 hari)

- Omzet: **Rp75.550.100**
- Jumlah nota: **2202**
- Rata-rata per nota: Rp34.310
- Rata-rata per hari: Rp878.490
- Hari terbaik: 10 Oktober 2026, Rp1.495.800

Per metode bayar:
- Tunai: Rp45.789.500 (1330 nota)
- QRIS: Rp25.841.200 (761 nota)
- Transfer bank: Rp3.919.400 (111 nota)

Per kasir:
- Budi: Rp38.239.400 (1118 nota)
- Ocha: Rp37.310.700 (1084 nota)

5 menu terlaris:
1. Teh Tarik 14 oz: 731 porsi, Rp10.965.000
2. Bagel Biasa: 571 porsi, Rp10.278.000
3. Wrap Biasa: 484 porsi, Rp10.648.000
4. Teh Tarik 22 oz: 481 porsi, Rp10.582.000
5. Milo Tarik 14 oz: 373 porsi, Rp6.714.000

- Nota batal: 21 nota (Rp668.000)
- Diskon: 86 nota (Rp311.900)
- Selisih kas: kurang Rp13.000, di 17 dari 172 shift
- Nota offline: 42 (2 beda harga)
- Kode klaim kartu: 886 dari 2202 sudah diklaim

## Gambar layar

- `01-rentang-bulan.png`: Laporan > Rentang > Bulan lalu (grafik per hari)
- `02-rentang-panjang.png`: seluruh simulasi (grafik per minggu)
- `03-rentang-rincian.png`: per metode bayar, per kasir, menu terlaris, catatan
- `04-harian.png`: Laporan harian hari terbaik bulan lalu (10 Oktober 2026)
- `05-setujui.png`: tab Setujui (1 pengajuan batal menunggu, 1 nota ditahan dari HP yang dicabut)

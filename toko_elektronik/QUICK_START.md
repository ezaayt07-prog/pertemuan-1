# Quick Start Guide - Toko Elektronik Mini v2.0

## 🚀 Mulai Cepat (3 Langkah)

### 1️⃣ Install PrettyTable
```bash
pip install prettytable
```

### 2️⃣ Jalankan Program
```bash
python main.py
```

### 3️⃣ Login dengan Akun Default

**Admin:**
- Username: `reza haikal`
- Password: `reza12345677`

**User:**
- Username: `pengguna`
- Password: `0990`

---

## 📁 Isi Project (16 Files)

### Python Modules (8 files)
```
main.py          → Program utama
models.py        → Data storage
auth.py          → Login & Register
inventory.py     → Manajemen barang
transaction.py   → Pembelian
menu.py          → Menu interface
utils.py         → Helper functions
__init__.py      → Package init
```

### Documentation (7 files)
```
README.md                 → Dokumentasi utama
PANDUAN_INSTALASI.md      → Guide instalasi lengkap
STRUKTUR_PROJECT.txt      → Visualisasi struktur
DIAGRAM_MODUL.txt         → Diagram dependencies
CONTOH_OUTPUT.txt         → Contoh tampilan
RINGKASAN_PROJECT.md      → Summary project
QUICK_START.md            → Panduan ini
```

### Configuration (1 file)
```
requirements.txt  → Dependencies (prettytable)
```

---

## 🎯 Fitur Utama

### Admin Menu
1. ✅ Lihat Daftar Barang (dengan PrettyTable)
2. ✅ Tambah Barang Baru
3. ✅ Ubah Data Barang
4. ✅ Hapus Barang
5. ✅ Lihat Statistik Toko
6. ✅ Lihat Log Aktivitas
7. ✅ Logout

### User Menu
1. ✅ Lihat Daftar Barang (dengan PrettyTable)
2. ✅ Beli Barang
3. ✅ Logout

---

## 📊 Contoh Tampilan

### Daftar Barang (PrettyTable)
```
+----+---------------------+---------------+------+
| No |    Nama Barang      |     Harga     | Stok |
+----+---------------------+---------------+------+
| 1  | Strika              |    Rp189,000  |  15  |
| 2  | Tv                  |  Rp2,500,000  |  10  |
| 3  | Laptop              |  Rp8,500,000  |  7   |
+----+---------------------+---------------+------+
```

### Statistik Toko
```
+-------------------------+------------------+
|       Keterangan        |       Nilai      |
+-------------------------+------------------+
| Total Barang            |      87 unit     |
| Total Nilai Inventaris  | Rp45,689,000     |
| Total Penjualan         |  Rp2,689,000     |
+-------------------------+------------------+
```

---

## 🔧 Troubleshooting Cepat

### Error: No module named 'prettytable'
```bash
pip install prettytable
# atau
pip3 install prettytable
```

### Error: pip not found
```bash
python -m pip install prettytable
# atau
python3 -m pip install prettytable
```

### Permission denied (Linux/Mac)
```bash
pip install --user prettytable
```

---

## 📖 Dokumentasi Lengkap

Untuk informasi lebih detail, baca:

1. **README.md** - Penjelasan modul dan fitur
2. **PANDUAN_INSTALASI.md** - Instalasi lengkap + troubleshooting
3. **STRUKTUR_PROJECT.txt** - Visualisasi struktur project
4. **DIAGRAM_MODUL.txt** - Hubungan antar modul
5. **CONTOH_OUTPUT.txt** - Screenshot tampilan program
6. **RINGKASAN_PROJECT.md** - Summary lengkap project

---

## 🎨 Keunggulan Versi 2.0

✅ **Modular Structure** - 8 modul terpisah
✅ **PrettyTable** - Tampilan tabel profesional
✅ **Well Documented** - 7 file dokumentasi
✅ **Easy to Maintain** - Kode terorganisir
✅ **Scalable** - Mudah dikembangkan
✅ **Professional** - Output yang rapi

---

## 📝 Catatan Penting

1. Program akan membuat file `log.txt` otomatis untuk menyimpan aktivitas
2. Semua transaksi akan tercatat dalam log
3. Stok barang akan update otomatis saat ada pembelian
4. Format harga otomatis ke Rupiah

---

## 💡 Tips

- Gunakan nomor atau nama barang saat memilih
- Lihat log untuk audit aktivitas
- Statistik menampilkan real-time data
- Tekan Ctrl+C untuk keluar paksa

---

## 🚀 Happy Coding!

Selamat menggunakan Toko Elektronik Mini v2.0!

**Created by:** Reza Haikal
**Version:** 2.0.0
**Year:** 2024

---

Need help? Baca file dokumentasi lainnya! 📚

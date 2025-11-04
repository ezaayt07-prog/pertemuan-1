# Panduan Instalasi dan Menjalankan Program

## Persyaratan Sistem

- Python 3.7 atau lebih tinggi
- pip (Python package manager)
- Terminal/Command Prompt

## Langkah Instalasi

### 1. Clone atau Download Project

```bash
# Jika menggunakan git
git clone <repository-url>

# Atau download dan ekstrak file ZIP
```

### 2. Masuk ke Direktori Project

```bash
cd toko_elektronik
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

atau jika menggunakan pip3:

```bash
pip3 install -r requirements.txt
```

atau install manual:

```bash
pip install prettytable
```

### 4. Jalankan Program

```bash
python main.py
```

atau:

```bash
python3 main.py
```

## Troubleshooting

### Masalah: pip tidak ditemukan

**Solusi:**
```bash
# Windows
py -m pip install -r requirements.txt

# Linux/Mac
python3 -m pip install -r requirements.txt
```

### Masalah: Permission denied (Linux/Mac)

**Solusi:**
```bash
# Gunakan virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

# Atau install dengan --user
pip install --user -r requirements.txt
```

### Masalah: ModuleNotFoundError: No module named 'prettytable'

**Solusi:**
```bash
pip install prettytable --upgrade
```

## Menggunakan Virtual Environment (Recommended)

Virtual environment membantu mengisolasi dependencies project.

### Windows

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Jalankan program
python main.py

# Deaktivasi (setelah selesai)
deactivate
```

### Linux/Mac

```bash
# Buat virtual environment
python3 -m venv venv

# Aktifkan virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Jalankan program
python main.py

# Deaktivasi (setelah selesai)
deactivate
```

## Akun Default

Setelah program berjalan, Anda dapat login dengan akun berikut:

### Admin
- **Username:** `reza haikal`
- **Password:** `reza12345677`

### User Biasa
- **Username:** `pengguna`
- **Password:** `0990`

## Fitur Program

### Menu Admin
1. Lihat Daftar Barang - Menampilkan semua barang dengan PrettyTable
2. Tambah Barang - Menambahkan barang baru ke inventori
3. Ubah Barang - Mengubah data barang yang sudah ada
4. Hapus Barang - Menghapus barang dari inventori
5. Lihat Statistik - Menampilkan statistik toko (total barang, nilai, penjualan)
6. Lihat Log Aktivitas - Menampilkan riwayat aktivitas
7. Logout - Keluar dari menu admin

### Menu User
1. Lihat Daftar Barang - Menampilkan katalog barang
2. Beli Barang - Melakukan pembelian barang
3. Logout - Keluar dari menu user

## Struktur File

```
toko_elektronik/
├── main.py              # Program utama
├── models.py            # Data models
├── auth.py              # Autentikasi
├── inventory.py         # Manajemen inventori
├── transaction.py       # Transaksi
├── menu.py              # Menu aplikasi
├── utils.py             # Fungsi utilitas
├── requirements.txt     # Dependencies
├── __init__.py         # Package initializer
├── README.md           # Dokumentasi
├── STRUKTUR_PROJECT.txt # Visualisasi struktur
└── PANDUAN_INSTALASI.md # Panduan ini
```

## File yang Dibuat Otomatis

Program akan membuat file berikut saat dijalankan:
- `log.txt` - File log aktivitas pengguna

## Tips Penggunaan

1. Gunakan nomor atau nama barang saat memilih barang
2. Log aktivitas tersimpan otomatis di `log.txt`
3. Stok barang akan berkurang otomatis saat ada pembelian
4. Total penjualan akan terakumulasi setiap transaksi
5. Tekan Ctrl+C untuk keluar paksa dari program

## Kontak

Jika mengalami masalah atau memiliki pertanyaan, silakan hubungi developer.

---
© 2024 Toko Elektronik Mini v2.0

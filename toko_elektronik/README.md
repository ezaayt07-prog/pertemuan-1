# Toko Elektronik Mini - Modular Version

Program manajemen toko elektronik dengan struktur modular menggunakan PrettyTable untuk tampilan.

## Struktur Project

```
toko_elektronik/
├── main.py              # Program utama
├── models.py            # Data models (akun, barang, penjualan)
├── auth.py              # Modul autentikasi (login, register)
├── inventory.py         # Modul manajemen inventori
├── transaction.py       # Modul transaksi pembelian
├── menu.py              # Modul menu aplikasi
├── utils.py             # Fungsi-fungsi utilitas
├── requirements.txt     # Dependencies
└── README.md           # Dokumentasi
```

## Deskripsi Modul

### 1. models.py
Menyimpan data aplikasi:
- Data akun pengguna (username, password, role)
- Data barang elektronik (nama, harga, stok)
- Total penjualan

### 2. auth.py
Menangani autentikasi:
- `login()`: Login pengguna
- `register()`: Registrasi akun baru

### 3. inventory.py
Manajemen inventori barang:
- `read_barang()`: Menampilkan daftar barang
- `create_barang()`: Menambah barang baru
- `update_barang()`: Mengubah data barang
- `delete_barang()`: Menghapus barang
- `tampilkan_statistik()`: Menampilkan statistik toko

### 4. transaction.py
Menangani transaksi:
- `beli_barang()`: Proses pembelian barang
- `proses_beli()`: Interface pembelian

### 5. menu.py
Menampilkan menu dengan PrettyTable:
- `menu_admin()`: Menu untuk admin
- `menu_user()`: Menu untuk pengguna biasa
- `tampilkan_menu_utama()`: Menu utama

### 6. utils.py
Fungsi-fungsi utilitas:
- `clear()`: Membersihkan layar
- `hitung_total()`: Menghitung total harga
- `format_rupiah()`: Format angka ke rupiah
- `log_aktivitas()`: Mencatat aktivitas
- `tampilkan_log()`: Menampilkan log
- `create_barang_table()`: Membuat tabel barang

### 7. main.py
Entry point aplikasi yang menjalankan program utama.

## Instalasi

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Jalankan program:
```bash
python main.py
```

## Akun Default

### Admin
- Username: `reza haikal`
- Password: `reza12345677`

### User
- Username: `pengguna`
- Password: `0990`

## Fitur

### Admin
- Lihat daftar barang
- Tambah barang baru
- Ubah data barang
- Hapus barang
- Lihat statistik toko
- Lihat log aktivitas

### User
- Lihat daftar barang
- Beli barang

## Perbaikan dari Versi Sebelumnya

1. **Modular**: Kode dipecah menjadi beberapa modul berdasarkan fungsi
2. **PrettyTable**: Menggunakan library PrettyTable untuk tampilan tabel yang lebih rapi
3. **Dokumentasi**: Setiap fungsi memiliki docstring
4. **Maintainability**: Lebih mudah dipelihara dan dikembangkan
5. **Separation of Concerns**: Setiap modul memiliki tanggung jawab yang jelas

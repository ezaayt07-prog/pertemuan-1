import os

# Data akun
akun = {
    "reza haikal": {"password": "reza12345677", "role": "admin"},
    "pengguna": {"password": "0990", "role": "user"}
}

# Data barang toko elektronik
barang = {
    "strika": {"harga": 189000, "stok": 15},
    "tv": {"harga": 2500000, "stok": 10},
    "laptop": {"harga": 8500000, "stok": 7},
    "kipas angin": {"harga": 285000, "stok": 10},
    "ac": {"harga": 3500000, "stok": 5},
    "mesin cuci": {"harga": 2750000, "stok": 8},
    "dispenser": {"harga": 450000, "stok": 12},
    "rice cooker": {"harga": 300000, "stok": 20}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# daftar barang
def read_barang(return_keys=False):
    clear()
    print("=== DAFTAR BARANG TOKO ELEKTRONIK MINI ===")
    if len(barang) == 0:
        print("Belum ada barang yang tersedia.")
        if return_keys:
            return []
        input("Tekan Enter untuk kembali...")
        return
    keys = list(barang.keys())
    print("{:<3} {:<20} {:<12} {:<5}".format("No", "Nama Barang", "Harga", "Stok"))
    print("-"*50)
    for i, k in enumerate(keys, start=1):
        data = barang[k]
        print("{:<3} {:<20} {:<12} {:<5}".format(i, k.title(), data["harga"], data["stok"]))
    print("-"*50)
    if return_keys:
        return keys
    input("Tekan Enter untuk kembali...")

# login
def login():
    clear()
    print("=== LOGIN TOKO ELEKTRONIK MINI ===")
    user = input("Username: ").lower().strip()
    pw = input("Password: ").strip()

    if user in akun and pw == akun[user]["password"]:
        print("\nLogin berhasil!")
        input("Tekan Enter untuk melanjutkan...")
        return akun[user]["role"]
    else:
        print("\nLogin gagal! Username atau password salah.")
        input("Tekan Enter untuk ulang...")
        return login()

# register
def register():
    clear()
    print("=== REGISTER AKUN BARU ===")
    username = input("Masukkan username baru: ").lower().strip()
    password = input("Masukkan password baru: ").strip()

    if username == "" or password == "":
        print("\nUsername atau password tidak boleh kosong!")
    elif username in akun:
        print("\nUsername sudah terdaftar!")
    else:
        akun[username] = {"password": password, "role": "user"}
        print("\nAkun berhasil dibuat!")

    input("Tekan Enter untuk kembali...")

# Tambah barang
def create_barang():
    clear()
    print("=== TAMBAH BARANG BARU ===")
    nama = input("Nama Barang: ").lower().strip()
    harga = input("Harga Barang: ").strip()
    stok = input("Stok Barang: ").strip()

    if nama == "" or not (harga.isdigit() and stok.isdigit()):
        print("\nNama tidak boleh kosong dan harga/stok harus angka!")
    elif nama in barang:
        print("\nBarang sudah ada!")
    else:
        barang[nama] = {"harga": int(harga), "stok": int(stok)}
        print("\nBarang berhasil ditambahkan!")

    input("Tekan Enter untuk kembali...")

# Ubah barang
def update_barang():
    keys = read_barang(return_keys=True)
    if len(keys) == 0:
        return

    pilih = input("\nMasukkan nomor atau nama barang yang ingin diubah: ").strip().lower()
    if pilih == "":
        print("\nInput tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return

    if pilih.isdigit():
        idx = int(pilih) - 1
        if 0 <= idx < len(keys):
            nama_key = keys[idx]
        else:
            print("\nNomor barang tidak valid!")
            input("Tekan Enter untuk kembali...")
            return
    else:
        nama_key = pilih
        if nama_key not in barang:
            print("\nBarang tidak ditemukan!")
            input("Tekan Enter untuk kembali...")
            return

    old = barang[nama_key]
    print(f"\nMengubah '{nama_key.title()}' (Harga: {old['harga']}, Stok: {old['stok']})")
    nama_baru = input("Nama baru (kosong = tetap): ").strip()
    harga = input("Harga baru (kosong = tetap): ").strip()
    stok = input("Stok baru (kosong = tetap): ").strip()

    if nama_baru == "":
        nama_baru = nama_key
    elif nama_baru.lower() != nama_key and nama_baru.lower() in barang:
        print("\nNama baru sudah digunakan!")
        input("Tekan Enter untuk kembali...")
        return

    harga_baru = int(harga) if harga.isdigit() else old["harga"] if harga == "" else None
    stok_baru = int(stok) if stok.isdigit() else old["stok"] if stok == "" else None

    if harga_baru is None or stok_baru is None:
        print("\nHarga dan stok harus angka!")
        input("Tekan Enter untuk kembali...")
        return

    barang[nama_baru.lower()] = {"harga": harga_baru, "stok": stok_baru}
    if nama_baru.lower() != nama_key:
        del barang[nama_key]

    print("\nBarang berhasil diperbarui!")
    input("Tekan Enter untuk kembali...")

# Hapus barang
def delete_barang():
    keys = read_barang(return_keys=True)
    if len(keys) == 0:
        return

    pilih = input("\nMasukkan nomor atau nama barang yang ingin dihapus: ").strip().lower()
    if pilih == "":
        print("\nInput tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return

    if pilih.isdigit():
        idx = int(pilih) - 1
        if 0 <= idx < len(keys):
            nama_key = keys[idx]
        else:
            print("\nNomor barang tidak valid!")
            input("Tekan Enter untuk kembali...")
            return
    else:
        nama_key = pilih
        if nama_key not in barang:
            print("\nBarang tidak ditemukan!")
            input("Tekan Enter untuk kembali...")
            return

    konfirm = input(f"Yakin ingin menghapus '{nama_key.title()}'? (iya/tidak): ").strip().lower()
    if konfirm in ["iya", "yes"]:
        del barang[nama_key]
        print("\nBarang berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan.")

    input("Tekan Enter untuk kembali...")

# Menu Admin
def menu_admin():
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. Lihat Daftar Barang")
        print("2. Tambah Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Logout")
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            read_barang()
        elif pilih == "2":
            create_barang()
        elif pilih == "3":
            update_barang()
        elif pilih == "4":
            delete_barang()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk ulang...")

# Menu User
def menu_user():
    while True:
        clear()
        print("=== MENU PENGGUNA ===")
        print("1. Lihat Daftar Barang")
        print("2. Logout")
        pilih = input("Silahkan pilih menu: ").strip()

        if pilih == "1":
            read_barang()
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk ulang...")

# Program utama
while True:
    clear()
    print("=== SELAMAT DATANG DI TOKO ELEKTRONIK MINI ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ").strip()

    if pilih == "1":
        role = login()
        if role == "admin":
            menu_admin()
        else:
            menu_user()
    elif pilih == "2":
        register()
    elif pilih == "3":
        clear()
        print("Terima kasih telah menggunakan program ini!")
        print("Sampai jumpa di toko kami!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk mengulang...")

import os

# data admin dan user
akun = [
    ["reza haikal", "reza12345677", "admin"],
    ["pengguna", "0990", "user"]
]

# Data barang / stok barang yang tersedia
barang = [
    ["strika", 189000, 15],
    ["tv", 2500000, 10],
    ["Laptop", 8500000, 7],
    ["kipas angin", 285000, 10],
    ["AC", 3500000, 5],
    ["mesin cuci", 2750000, 8],
    ["dispenser", 450000, 12],
    ["rice cooker", 300000, 20],
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# login
def login():
    clear()
    print("=== LOGIN TOKO ELEKTRONIK MINI ===")
    user = input("Username: ")
    pw = input("Password: ")

    for data in akun:
        if user == data[0] and pw == data[1]:
            print("\nLogin berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            return data[2]  # return role
    print("\nLogin gagal! Username atau password salah.")
    input("Tekan Enter untuk ulang...")
    return login()

# register untik pengguna baru
def register():
    clear()
    print("=== REGISTER AKUN BARU ===")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    # penrgecekan username
    duplikat = 0
    for data in akun:
        if username == data[0]:
            duplikat = 1
            break

    if duplikat == 1:
        print("\nUsername sudah terdaftar!")
    else:
        akun.append([username, password, "user"])
        print("\nAkun berhasil dibuat!")

    input("Tekan Enter untuk kembali...")

# Fungsi tampil daftar barang
def read_barang():
    clear()
    print("=== DAFTAR BARANG TOKO ELEKTRONIK MINI ===")
    print("{:<3} {:<20} {:<10} {:<5}".format("No", "Nama Barang", "Harga", "Stok"))
    print("-"*45)
    for i in range(len(barang)):
        print("{:<3} {:<20} {:<10} {:<5}".format(i+1, barang[i][0], barang[i][1], barang[i][2]))
    print("-"*45)

# menambahkan barang

def create_barang():
    clear()
    print("=== TAMBAH BARANG BARU ===")
    nama = input("Nama Barang: ")
    harga = input("Harga Barang: ")
    stok = input("Stok Barang: ")

    if harga.isdigit() and stok.isdigit():
        barang.append([nama, int(harga), int(stok)])
        print("\nBarang berhasil ditambahkan!")
    else:
        print("\nInput harga atau stok harus berupa angka!")

    input("Tekan Enter untuk kembali...")

# update barang/memperbarui barang

def update_barang():
    read_barang()
    pilih = input("\nMasukkan nomor barang yang ingin diubah: ")

    if pilih.isdigit():
        pilih = int(pilih)
        if 1 <= pilih <= len(barang):
            nama = input("Nama baru: ")
            harga = input("Harga baru: ")
            stok = input("Stok baru: ")

            if harga.isdigit() and stok.isdigit():
                barang[pilih-1] = [nama, int(harga), int(stok)]
                print("\nBarang berhasil diperbarui!")
            else:
                print("\nHarga dan stok harus angka!")
        else:
            print("\nNomor barang tidak valid!")
    else:
        print("\nInput harus berupa angka!")

    input("Tekan Enter untuk kembali...")

# Fungsi dari penghapusan barang

def delete_barang():
    read_barang()
    pilih = input("\nMasukkan nomor barang yang ingin dihapus: ")

    if pilih.isdigit():
        pilih = int(pilih)
        if 1 <= pilih <= len(barang):
            del barang[pilih-1]
            print("\nBarang berhasil dihapus!")
        else:
            print("\nNomor barang tidak valid!")
    else:
        print("\nInput harus angka!")

    input("Tekan Enter untuk kembali...")

# Menu untuk admin

def menu_admin():
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. Lihat Daftar Barang")
        print("2. Tambah Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            read_barang()
            input("Tekan Enter untuk kembali...")
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

# Menu untuk user/pengguna baru

def menu_user():
    while True:
        clear()
        print("=== MENU PENGGUNA ===")
        print("1. Lihat Daftar Barang")
        print("2. Logout/keluar")
        pilih = input("silahkan pilih menu: ")

        if pilih == "1":
            read_barang()
            input("Tekan Enter untuk kembali...")
        elif pilih == "2":
            break
        else:
            print("Pilihan anda tidak valid!")
            input("Tekan Enter untuk ulang...")

# Program utamayna

while True:
    clear()
    print("=== SELAMAT DATANG DI TOKO ELEKTRONIK MINI ===")
    print("    SILAHKAN LOGIN / REGISTER DI BAWA INI: ")
    print("ATAU PILIH MENU 3 UNTUK KELUAR DARI PROGRAM INI")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

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
        print("silahkan datang kembali di toko kami")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk mengulang...")

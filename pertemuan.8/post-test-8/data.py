import os
from prettytable import PrettyTable
from kalkulasi import hitung_total

akun = {
    "reza haikal": {"password": "reza12345677", "role": "admin"},
    "pengguna": {"password": "0990", "role": "user"}
}

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

total_penjualan = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_statistik():
    clear()
    print("=== STATISTIK TOKO ===")
    total_barang = sum(item["stok"] for item in barang.values())
    total_nilai = sum(item["harga"] * item["stok"] for item in barang.values())
    
    table = PrettyTable()
    table.field_names = ["Kategori", "Nilai"]
    table.add_row(["Total Barang", f"{total_barang}"])
    table.add_row(["Total Nilai Inventaris", f"Rp{total_nilai:,}"])
    table.add_row(["Total Penjualan", f"Rp{total_penjualan:,}"])
    print(table)
    input("Tekan Enter untuk kembali...")

def tampilkan_log():
    try:
        with open("log.txt", "r") as f:
            content = f.read().strip()
            logs = content.split('\n') if content else []
    except FileNotFoundError:
        logs = []
    
    print("=== LOG AKTIVITAS ===")
    if logs:
        table = PrettyTable()
        table.field_names = ["Aktivitas"]
        for log in logs:
            table.add_row([log])
        print(table)
    else:
        print("Belum ada log.")
    input("Tekan Enter untuk kembali...")

def log_aktivitas(aktivitas):
    try:
        with open("log.txt", "a") as f:
            f.write(f"{aktivitas}\n")
    except Exception as e:
        print(f"Error logging: {e}")

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
    
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga", "Stok"]
    for i, k in enumerate(keys, start=1):
        data = barang[k]
        table.add_row([i, k.title(), f"Rp{data['harga']:,}", data["stok"]])
    print(table)
    
    if return_keys:
        return keys
    input("Tekan Enter untuk kembali...")

def login():
    clear()
    print("=== LOGIN TOKO ELEKTRONIK MINI ===")
    user = input("Username: ").lower().strip()
    pw = input("Password: ").strip()

    if user in akun and pw == akun[user]["password"]:
        print("\nLogin berhasil!")
        log_aktivitas(f"Login berhasil: {user}")
        input("Tekan Enter untuk melanjutkan...")
        return akun[user]["role"]
    else:
        print("\nLogin gagal! Username atau password salah.")
        input("Tekan Enter untuk ulang...")
        return login()

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
        log_aktivitas(f"Akun baru dibuat: {username}")
        print("\nAkun berhasil dibuat!")

    input("Tekan Enter untuk kembali...")

def create_barang():
    clear()
    print("=== TAMBAH BARANG BARU ===")
    nama = input("Nama Barang: ").lower().strip()
    harga = input("Harga Barang: ").strip()
    stok = input("Stok Barang: ").strip()

    try:
        if nama == "" or not (harga.isdigit() and stok.isdigit()):
            print("\nNama tidak boleh kosong dan harga/stok harus angka!")
        elif nama in barang:
            print("\nBarang sudah ada!")
        else:
            barang[nama] = {"harga": int(harga), "stok": int(stok)}
            log_aktivitas(f"Barang ditambah: {nama}")
            print("\nBarang berhasil ditambahkan!")
    except ValueError:
        print("\nError: Input tidak valid!")

    input("Tekan Enter untuk kembali...")

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

    try:
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

        log_aktivitas(f"Barang diubah: {nama_key} -> {nama_baru}")
        print("\nBarang berhasil diperbarui!")
    except ValueError:
        print("\nError: Input tidak valid!")

    input("Tekan Enter untuk kembali...")

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
        log_aktivitas(f"Barang dihapus: {nama_key}")
        print("\nBarang berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan.")

    input("Tekan Enter untuk kembali...")

def beli_barang(nama_barang, jumlah):
    global total_penjualan
    if nama_barang in barang and barang[nama_barang]["stok"] >= jumlah:
        total = hitung_total(barang[nama_barang]["harga"], jumlah)
        barang[nama_barang]["stok"] -= jumlah
        total_penjualan += total
        log_aktivitas(f"Pembelian: {nama_barang} x{jumlah}, Total: Rp{total}")
        print(f"\nPembelian berhasil! Total: Rp{total:,}")
    else:
        print("\nStok tidak cukup atau barang tidak ditemukan!")

def proses_beli():
    keys = read_barang(return_keys=True)
    if len(keys) == 0:
        return

    pilih = input("\nMasukkan nomor atau nama barang yang ingin dibeli: ").strip().lower()
    jumlah = input("Jumlah: ").strip()

    try:
        jumlah = int(jumlah)
        if jumlah <= 0:
            print("\nJumlah harus positif!")
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

        beli_barang(nama_key, jumlah)
    except ValueError:
        print("\nError: Jumlah harus angka!")

    input("Tekan Enter untuk kembali...")

def menu_admin():
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. Lihat Daftar Barang")
        print("2. Tambah Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Lihat Statistik")
        print("6. Lihat Log Aktivitas")
        print("7. Logout")
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
            tampilkan_statistik()
        elif pilih == "6":
            tampilkan_log()
        elif pilih == "7":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk ulang...")

def menu_user():
    while True:
        clear()
        print("=== MENU PENGGUNA ===")
        print("1. Lihat Daftar Barang")
        print("2. Beli Barang")
        print("3. Logout")
        pilih = input("Silahkan pilih menu: ").strip()

        if pilih == "1":
            read_barang()
        elif pilih == "2":
            proses_beli()
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk ulang...")
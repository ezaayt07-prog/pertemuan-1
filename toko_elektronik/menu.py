"""
Module untuk menu aplikasi
"""
from prettytable import PrettyTable
from utils import clear, tampilkan_log
from inventory import read_barang, create_barang, update_barang, delete_barang, tampilkan_statistik
from transaction import proses_beli

def tampilkan_menu_admin():
    """Menampilkan menu admin menggunakan PrettyTable"""
    table = PrettyTable()
    table.field_names = ["No", "Menu"]
    table.align["No"] = "c"
    table.align["Menu"] = "l"

    menu_items = [
        "Lihat Daftar Barang",
        "Tambah Barang",
        "Ubah Barang",
        "Hapus Barang",
        "Lihat Statistik",
        "Lihat Log Aktivitas",
        "Logout"
    ]

    for i, item in enumerate(menu_items, start=1):
        table.add_row([i, item])

    print("=== MENU ADMIN ===\n")
    print(table)

def tampilkan_menu_user():
    """Menampilkan menu user menggunakan PrettyTable"""
    table = PrettyTable()
    table.field_names = ["No", "Menu"]
    table.align["No"] = "c"
    table.align["Menu"] = "l"

    menu_items = [
        "Lihat Daftar Barang",
        "Beli Barang",
        "Logout"
    ]

    for i, item in enumerate(menu_items, start=1):
        table.add_row([i, item])

    print("=== MENU PENGGUNA ===\n")
    print(table)

def tampilkan_menu_utama():
    """Menampilkan menu utama menggunakan PrettyTable"""
    table = PrettyTable()
    table.field_names = ["No", "Menu"]
    table.align["No"] = "c"
    table.align["Menu"] = "l"

    menu_items = [
        "Login",
        "Register",
        "Keluar"
    ]

    for i, item in enumerate(menu_items, start=1):
        table.add_row([i, item])

    print("=== SELAMAT DATANG DI TOKO ELEKTRONIK MINI ===\n")
    print(table)

def menu_admin():
    """Loop menu admin"""
    while True:
        clear()
        tampilkan_menu_admin()
        pilih = input("\nPilih menu: ").strip()

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
            print("\nPilihan tidak valid!")
            input("Tekan Enter untuk ulang...")

def menu_user():
    """Loop menu user"""
    while True:
        clear()
        tampilkan_menu_user()
        pilih = input("\nSilahkan pilih menu: ").strip()

        if pilih == "1":
            read_barang()
        elif pilih == "2":
            proses_beli()
        elif pilih == "3":
            break
        else:
            print("\nPilihan tidak valid!")
            input("Tekan Enter untuk ulang...")

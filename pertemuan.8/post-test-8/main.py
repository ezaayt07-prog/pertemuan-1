import os
from data import akun, barang, total_penjualan, clear, tampilkan_statistik, tampilkan_log, read_barang, login, register, create_barang, update_barang, delete_barang, menu_admin, menu_user, proses_beli
from kalkulasi import hitung_total
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
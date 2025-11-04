"""
Program Utama Toko Elektronik Mini
File ini adalah entry point aplikasi
"""
from auth import login, register
from menu import menu_admin, menu_user, tampilkan_menu_utama
from utils import clear

def main():
    """Fungsi utama program"""
    while True:
        clear()
        tampilkan_menu_utama()
        pilih = input("\nPilih menu: ").strip()

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
            print("\nPilihan tidak valid!")
            input("Tekan Enter untuk mengulang...")

if __name__ == "__main__":
    main()

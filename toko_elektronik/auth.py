"""
Module untuk autentikasi pengguna
"""
from models import akun
from utils import clear, log_aktivitas

def login():
    """
    Fungsi untuk login pengguna

    Returns:
        str: Role pengguna (admin/user)
    """
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
    """Fungsi untuk registrasi akun baru"""
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

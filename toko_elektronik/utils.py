"""
Module untuk fungsi-fungsi utilitas
"""
import os
from prettytable import PrettyTable

def clear():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_total(harga, jumlah):
    """
    Menghitung total harga

    Args:
        harga (int): Harga per unit
        jumlah (int): Jumlah barang

    Returns:
        int: Total harga
    """
    return harga * jumlah

def format_rupiah(angka):
    """
    Format angka menjadi format rupiah

    Args:
        angka (int): Angka yang akan diformat

    Returns:
        str: String dengan format rupiah
    """
    return f"Rp{angka:,}"

def log_aktivitas(aktivitas):
    """
    Mencatat aktivitas ke file log

    Args:
        aktivitas (str): Deskripsi aktivitas
    """
    try:
        with open("log.txt", "a") as f:
            f.write(f"{aktivitas}\n")
    except Exception as e:
        print(f"Error logging: {e}")

def tampilkan_log():
    """Menampilkan log aktivitas dari file"""
    clear()
    try:
        with open("log.txt", "r") as f:
            logs = f.read()
        print("=== LOG AKTIVITAS ===")
        print(logs if logs else "Belum ada log.")
    except FileNotFoundError:
        print("=== LOG AKTIVITAS ===")
        print("Belum ada log.")
    input("\nTekan Enter untuk kembali...")

def create_barang_table(data_barang):
    """
    Membuat tabel barang dengan PrettyTable

    Args:
        data_barang (dict): Dictionary berisi data barang

    Returns:
        PrettyTable: Objek tabel yang sudah diformat
    """
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga", "Stok"]
    table.align["No"] = "c"
    table.align["Nama Barang"] = "l"
    table.align["Harga"] = "r"
    table.align["Stok"] = "c"

    for i, (nama, data) in enumerate(data_barang.items(), start=1):
        table.add_row([i, nama.title(), format_rupiah(data["harga"]), data["stok"]])

    return table

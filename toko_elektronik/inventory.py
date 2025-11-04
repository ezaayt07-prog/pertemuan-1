"""
Module untuk manajemen inventori barang
"""
from prettytable import PrettyTable
from models import barang
from utils import clear, log_aktivitas, create_barang_table

def read_barang(return_keys=False):
    """
    Menampilkan daftar barang

    Args:
        return_keys (bool): Jika True, mengembalikan list keys barang

    Returns:
        list: List keys barang jika return_keys=True, None jika False
    """
    clear()
    print("=== DAFTAR BARANG TOKO ELEKTRONIK MINI ===\n")

    if len(barang) == 0:
        print("Belum ada barang yang tersedia.")
        if return_keys:
            return []
        input("\nTekan Enter untuk kembali...")
        return

    keys = list(barang.keys())
    table = create_barang_table(barang)
    print(table)

    if return_keys:
        return keys
    input("\nTekan Enter untuk kembali...")

def create_barang():
    """Fungsi untuk menambah barang baru"""
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
    """Fungsi untuk mengubah data barang"""
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
    """Fungsi untuk menghapus barang"""
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

def tampilkan_statistik():
    """Menampilkan statistik toko"""
    from models import total_penjualan
    from prettytable import PrettyTable

    clear()
    print("=== STATISTIK TOKO ===\n")

    total_barang = sum(item["stok"] for item in barang.values())
    total_nilai = sum(item["harga"] * item["stok"] for item in barang.values())

    table = PrettyTable()
    table.field_names = ["Keterangan", "Nilai"]
    table.align["Keterangan"] = "l"
    table.align["Nilai"] = "r"

    table.add_row(["Total Barang", f"{total_barang} unit"])
    table.add_row(["Total Nilai Inventaris", f"Rp{total_nilai:,}"])
    table.add_row(["Total Penjualan", f"Rp{total_penjualan:,}"])

    print(table)
    input("\nTekan Enter untuk kembali...")

"""
Module untuk transaksi pembelian
"""
import models
from inventory import read_barang
from utils import hitung_total, log_aktivitas

def beli_barang(nama_barang, jumlah):
    """
    Proses pembelian barang

    Args:
        nama_barang (str): Nama barang yang dibeli
        jumlah (int): Jumlah barang yang dibeli
    """
    if nama_barang in models.barang and models.barang[nama_barang]["stok"] >= jumlah:
        total = hitung_total(models.barang[nama_barang]["harga"], jumlah)
        models.barang[nama_barang]["stok"] -= jumlah
        models.total_penjualan += total
        log_aktivitas(f"Pembelian: {nama_barang} x{jumlah}, Total: Rp{total}")
        print(f"\nPembelian berhasil! Total: Rp{total:,}")
    else:
        print("\nStok tidak cukup atau barang tidak ditemukan!")

def proses_beli():
    """Fungsi untuk memproses pembelian barang"""
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
            if nama_key not in models.barang:
                print("\nBarang tidak ditemukan!")
                input("Tekan Enter untuk kembali...")
                return

        beli_barang(nama_key, jumlah)
    except ValueError:
        print("\nError: Jumlah harus angka!")

    input("Tekan Enter untuk kembali...")

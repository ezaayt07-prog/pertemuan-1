# imput data pelanggan
hallo = input("selamat datang di toko bahan bangunan, ada yang bisa kami bantu? (iya/tidak):")
iya = ("lanjutkan")
tidak = ("terimakasih sudah mampir di toko kami")
nama_pelanggan = input("harap masukkan nama anda: ")
jumlah_batu_bata = int(input("Masukkan jumlah batu-bata yang anda ingin beli: "))
jumlah_semen = int(input("Masukkan jumlah karung_semen yang anda ingin beli: "))

# harga barang
harga_batu_bata = 100
harga_semen = 100_000

# total biaya awal
total_biaya_awal = (jumlah_batu_bata * harga_batu_bata) + (jumlah_semen * harga_semen)

# diskon
is_paket_hemat = jumlah_batu_bata == 500 and jumlah_semen == 5
is_paket_ultra = jumlah_batu_bata == 2000 and jumlah_semen == 16

if is_paket_ultra:
   diskon_persen = 30
   keterangan_diskon = "Paket Ultra Mantap (30%)"
elif is_paket_hemat:
   diskon_persen = 15
   keterangan_diskon = "Paket Hemat (15%)"
else:
   diskon_persen = 0
   keterangan_diskon = "Tidak Ada Diskon"

diskon_rupiah = float(total_biaya_awal) * diskon_persen / 100
total_biaya_akhir = float(total_biaya_awal) - diskon_rupiah

# Output pembelian
print("="*42)
print("         STRUK BALANJAAN ANDA")
print("="*42)
print(f"Nama Pelanggan: {nama_pelanggan}")
print("-"*57)
print(f"| {'Barang':10} | {'Jumlah':6} | {'Harga Satuan':13} |")
print("-"*57)
print(f"| {'Batu Bata':10} | {jumlah_batu_bata:<6} | Rp{harga_batu_bata:<11,} |")
print(f"| {'Semen':10} | {jumlah_semen:<6} | Rp{harga_semen:<11,} |")
print("-"*57)
print(f"Total Biaya Awal{'':32}: Rp {total_biaya_awal:,.0f}")
print(f"Diskon yang Didapat{'':28}: {keterangan_diskon}")
print(f"Jumlah Diskon{'':37}: Rp {diskon_rupiah:,.0f}")
print("-"*57)
print(f"TOTAL BIAYA AKHIR{'':28}: Rp {total_biaya_akhir:,.0f}")
print("="*42)
print("terima kasih telah mampir di toko kami") and exit()

print("Penghitung Gaji Karyawan PT. BOM")

nama = input("Harap masukkan nama anda: ")
jabatan = input("Masukkan jabatan anda (peracik petasan/pengantar petasan): ").lower()
hari_kerja = int(input("Masukkan jumlah hari kerja anda: "))
jam_kerja = int(input("Masukkan jumlah jam kerja per hari anda: "))
jumlah_lembur = int(input("Masukkan jumlah lembur anda: "))

harga_petasan = 5000

bayaran_per_jam = 0
bayaran_per_lembur = 0

if jabatan == "peracik petasan":
    if hari_kerja >= 18 and jam_kerja >= 6 and jumlah_lembur >= 2:
        bayaran_per_jam = 20000
        bayaran_per_lembur = 10000
    elif hari_kerja >= 24 and jam_kerja >= 8 and jumlah_lembur >= 4:
        bayaran_per_jam = 25000
        bayaran_per_lembur = 15000
    else:
        bayaran_per_jam = 15000
        bayaran_per_lembur = 10000
elif jabatan == "pengantar petasan":
    if hari_kerja >= 16 and jam_kerja >= 5 and jumlah_lembur >= 4:
        bayaran_per_jam = 20000
        bayaran_per_lembur = 15000
    elif hari_kerja >= 20 and jam_kerja >= 7 and jumlah_lembur >= 7:
        bayaran_per_jam = 25000
        bayaran_per_lembur = 20000
    else:
        bayaran_per_jam = 15000
        bayaran_per_lembur = 12000
else:
    print("Jabatan tidak dikenali.")
    exit()

total_gaji = ((bayaran_per_jam * jam_kerja) * hari_kerja) + (jumlah_lembur * bayaran_per_lembur)

print("\n--- Detail Gaji Karyawan ---")
print(f"Nama Karyawan      : {nama}")
print(f"Jabatan            : {jabatan.title()}")
print(f"Harga Petasan/pcs  : Rp{harga_petasan:,}")
print(f"Hari Kerja         : {hari_kerja}")
print(f"Jam Kerja/hari     : {jam_kerja}")
print(f"Jumlah Lembur      : {jumlah_lembur}")
print(f"Bayaran per Jam    : Rp{bayaran_per_jam:,}")
print(f"Bayaran per Lembur : Rp{bayaran_per_lembur:,}")
print(f"Total Gaji         : Rp{total_gaji:,}")

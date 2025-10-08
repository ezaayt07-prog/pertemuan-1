stamina = int(input("Harap Masukkan 3 Digit terakhir  NIM Kamu (contoh 113): "))
chakra = 0

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print("\n--- HASIL MISI 1 ---")
print("Chakra yang terkumpul:", chakra)
print("Sisa stamina:", stamina)

if chakra >= 200:
    print("Naruto berhasil menyempurnakan Rasengan!")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra...")

tinggi_menara = int(input("\nHarap Masukkan 2 digit terakhir NIM kamu (contoh 13): "))

gulungan = 0
for tinggi in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print("\n--- HASIL MISI 2 ---")
print("Tinggi menara:", tinggi_menara, "meter")
print("Jumlah gulungan informasi yang didapat:", gulungan)

jumlah_koridor = int(input("\nHarap Masukkan digit kedua terakhir NIM kamu (contoh 1): "))

intelijen = 0
perangkap = 0

for koridor in range(1, jumlah_koridor + 1):
    print(f"\nKoridor {koridor}:")
    for ruangan in range(1, 4):
        nomor_ruangan = (koridor - 1) * 3 + ruangan
        if nomor_ruangan % 2 == 1:
            print(f"  Ruangan {nomor_ruangan} → Data Intelijen ditemukan!")
            intelijen += 1
        else:
            print(f"  Ruangan {nomor_ruangan} → Perangkap Peledak dijinakkan!")
            perangkap += 1

print("\n--- HASIL MISI 3 ---")
print("Total Data Intelijen yang dikumpulkan:", intelijen)
print("Total Perangkap Peledak yang dijinakkan:", perangkap)

print("\nSemua misi telah diselesaikan! Naruto membuktikan kecepatan berpikir dan logikanya.")

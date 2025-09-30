# Deklarasi variabel dan input
imput = int(input("Masukkan imputan: "))

angka1 = 1
angka2 = 0

# Perulangan dari 0 sampai imput - 1
for loop in range(imput):
    total = angka1 + angka2
    angka1 = angka2
    angka2 = total
    print(total)
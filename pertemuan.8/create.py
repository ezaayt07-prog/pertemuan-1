import random

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
def buat_kata_sandi(panjang=12):
    pilihan = [random.choice(karakter) for _ in range(panjang)]
    kata_sandi = "".join(pilihan)
    return kata_sandi

if __name__ == "__main__":
    print(buat_kata_sandi())
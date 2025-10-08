# Implementasi latihan: 3 misi berurutan untuk Naruto

def mission_one(stamina, target_chakra=200):
	"""Misi 1: Menyempurnakan Rasengan.

	- Mulai dengan `stamina`.
	- Setiap percobaan: +5 chakra, -3 stamina.
	- Gunakan while loop sampai chakra >= target_chakra atau stamina <= 0.
	- Kembalikan (chakra, sisa_stamina, berhasil_bool, percobaan)
	"""
	chakra = 0
	attempts = 0
	while chakra < target_chakra and stamina > 0:
		chakra += 5
		stamina -= 3
		attempts += 1
		# pastikan stamina tidak negatif
		if stamina < 0:
			stamina = 0
	success = chakra >= target_chakra
	return chakra, stamina, success, attempts


def mission_two(tower_height):
	"""Misi 2: Infiltrasi menara.

	- Diberi `tower_height` (meter).
	- Akan menemukan 1 gulungan setiap 3 meter.
	- Gunakan for + range(start, stop, step).
	- Kembalikan jumlah gulungan.
	"""
	scrolls = 0
	# mulai dari 3m, hingga termasuk tower_height, loncatan 3
	for meter in range(3, tower_height + 1, 3):
		scrolls += 1
	return scrolls


def mission_three(corridors):
	"""Misi 3: Menyelidiki koridor.

	- `corridors` adalah jumlah koridor.
	- Masing-masing koridor punya 3 ruangan (1..3).
	- Ruangan bernomor ganjil = Data Intelijen.
	- Ruangan bernomor genap = Perangkap Peledak.
	- Gunakan nested loops dan kondisi ganjil/genap.
	- Kembalikan (intel_count, bombs_count)
	"""
	intel = 0
	bombs = 0
	for k in range(1, corridors + 1):
		# setiap koridor punya 3 ruangan bernomor 1..3
		for room in range(1, 4):
			if room % 2 == 1:
				intel += 1
			else:
				bombs += 1
	return intel, bombs


def parse_nim(nim_str):
	"""Mengambil stamina (3 digit terakhir), tinggi menara (2 digit terakhir),
	dan jumlah koridor (digit kedua dari belakang) dari string NIM.

	Asumsi: NIM mengandung minimal 3 digit angka di akhir.
	"""
	# ambil hanya digit dari input
	digits = ''.join(ch for ch in nim_str if ch.isdigit())
	if len(digits) < 3:
		raise ValueError('NIM harus memiliki minimal 3 digit angka.')
	stamina = int(digits[-3:])
	tower_height = int(digits[-2:])
	corridors = int(digits[-2])  # digit kedua dari belakang
	return stamina, tower_height, corridors


def main():
	print('--- Tiga Misi Naruto (Masukkan NIM) ---')
	while True:
		nim = input('Masukkan NIM (contoh: 2409106029): ').strip()
		try:
			stamina, tower_height, corridors = parse_nim(nim)
			break
		except ValueError as e:
			print('Input tidak valid:', e)

	# Misi 1
	print('\nMisi 1: Tes Konsentrasi (Rasengan)')
	chakra, rem_stamina, success, attempts = mission_one(stamina, target_chakra=200)
	print(f'Chakra terkumpul: {chakra}')
	print(f'Sisa stamina: {rem_stamina}')
	if success:
		print(f'Naruto berhasil mencapai {chakra} Chakra setelah {attempts} percobaan!')
	else:
		print('Naruto kehabisan stamina sebelum mencapai 200 Chakra.')

	# Misi 2
	print('\nMisi 2: Infiltrasi Menara')
	print(f'Tinggi menara: {tower_height} meter')
	scrolls = mission_two(tower_height)
	print(f'Jumlah Gulungan Informasi yang ditemukan: {scrolls}')

	# Misi 3
	print('\nMisi 3: Penyelidikan Markas Rahasia')
	print(f'Jumlah koridor: {corridors}')
	intel, bombs = mission_three(corridors)
	print(f'Data Intelijen yang didapatkan: {intel}')
	print(f'Perangkap Peledak yang dijinakkan: {bombs}')


if __name__ == '__main__':
	main()

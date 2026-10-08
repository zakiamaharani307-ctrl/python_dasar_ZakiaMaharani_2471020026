# BAB 03 - Input & Output

# 1. Menampilkan output dengan print()
print("Halo", "Dunia")

# Mengatur pemisah dengan sep
print("A", "B", "C", sep="-")

# Mengatur akhir tampilan dengan end
print("Loading", end="...")
print("selesai")

# 2. Format angka
harga = 15000 / 7
print(f"Harga: Rp{harga:.2f}")

total = 1500000
print(f"Total: {total:,}")

# 3. Membaca input dari pengguna
nama = input("Siapa namamu? ")
umur = int(input("Berapa umurmu? "))

# 4. Perhitungan
tahun_depan = umur + 1

# 5. Menampilkan hasil menggunakan f-string
print(f"Halo {nama}!")
print(f"Tahun depan kamu {tahun_depan} tahun")
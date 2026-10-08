# BAB 11 - Pengolahan Data dengan Pandas

import pandas as pd

# Membaca file CSV
df = pd.read_csv("nilai.csv")

# Menampilkan data
print("Data Nilai:")
print(df)

# Menghitung rata-rata setiap kelas
print("\nRata-rata per kelas:")
print(df.groupby("kelas")["nilai"].mean())

# Menampilkan siswa yang lulus
print("\nSiswa yang lulus:")
print(df[df["nilai"] >= 75]["nama"].tolist())

# Mencari nilai tertinggi
print("\nNilai tertinggi:")
print(df.sort_values("nilai").tail(1))

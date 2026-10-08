# BAB 07 - Koleksi Data

# 1. List
nilai = [80, 65, 90]

nilai.append(75)
nilai.remove(65)
nilai[0] = 85

print("List:", nilai)
print("Nilai terakhir:", nilai[-1])
print("Jumlah data:", len(nilai))
print("Urutan:", sorted(nilai))


# 2. Tuple
titik = (3, 7)
warna = (255, 128, 0)

x, y = titik

print(f"x={x}, y={y}")
print("Warna pertama:", warna[0])
print("Jumlah warna:", len(warna))


# 3. Set
angka = {1, 2, 2, 3, 3, 3}

print("Set:", angka)

ipa = {"Ani", "Budi", "Dodi"}
ips = {"Budi", "Citra"}

print("Gabungan:", ipa | ips)
print("Irisan:", ipa & ips)
print("Perbedaan:", ipa - ips)


# 4. Dictionary
siswa = {
    "nama": "Sari",
    "umur": 19
}

siswa["kota"] = "Bandung"
siswa["umur"] = 20

print("Nama:", siswa["nama"])
print("Hobi:", siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(f"{k}: {v}")
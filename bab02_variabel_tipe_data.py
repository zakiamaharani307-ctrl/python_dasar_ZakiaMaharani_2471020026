# BAB 02 - Variabel & Tipe Data

# Variabel
nama = "Budi"       # str
umur = 20           # int
tinggi = 170.5      # float
aktif = True        # bool

# Nilai bisa diganti
umur = umur + 1

# Multiple assignment
x, y, z = 1, 2, 3

print(nama, umur, x + y + z)


# Empat tipe data dasar
print(type(10))       # int
print(type(3.14))     # float
print(type("A"))      # str
print(type(True))     # bool


# Casting / konversi tipe data
angka = int("25")
print(angka + 5)

harga = float("12500.75")
print(type(harga))

umur = 20
print("Umur: " + str(umur))

print(bool(0), bool("hai"))


# Bekerja dengan String
nama = "Python Dasar"

print(len(nama))
print(nama.upper())
print(nama[0:6])
print(nama.split(" "))

bab = 2
print(f"Belajar {nama} bab {bab}")
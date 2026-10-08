# BAB 08 - Function

# 1. Function dengan parameter dan return
def hitung_luas(panjang, lebar):
    return panjang * lebar

print("Luas:", hitung_luas(5, 3))
print("Luas:", hitung_luas(10, 2))


# 2. Default parameter dan keyword argument
def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))


# 3. *args
def total(*angka):
    return sum(angka)

print("Total:", total(1, 2, 3, 4))


# 4. Lambda
kuadrat = lambda x: x ** 2

print("Kuadrat:", kuadrat(4))


# 5. Lambda dengan max()
siswa = [("Ani", 80), ("Budi", 95)]

tertinggi = max(siswa, key=lambda s: s[1])
print("Nilai tertinggi:", tertinggi)


# 6. Scope variabel
x = "global"

def tes():
    x = "lokal"
    print("Di dalam function:", x)

tes()
print("Di luar function:", x)

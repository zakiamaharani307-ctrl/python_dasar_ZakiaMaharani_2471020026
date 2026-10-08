# BAB 06 - Perulangan

# 1. Perulangan for dengan range()
for i in range(1, 4):
    print(f"Putaran ke-{i}")

# 2. Perulangan for pada list
buah = ["apel", "jeruk", "mangga"]

for b in buah:
    print(b.upper())

# 3. Perulangan while
hitung = 3

while hitung > 0:
    print(f"Hitung mundur: {hitung}")
    hitung -= 1

print("Meluncur!")

# 4. break dan continue
for n in range(1, 10):
    if n == 3:
        continue

    if n == 6:
        break

    print(n)

# 5. pass
for i in range(3):
    pass
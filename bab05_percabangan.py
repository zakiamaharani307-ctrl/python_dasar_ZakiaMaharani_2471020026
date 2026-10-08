# BAB 05 - Percabangan

# 1. if dan else
nilai = 80

if nilai >= 75:
    print("Selamat, kamu lulus!")
else:
    print("Ayo remedial dulu")


# 2. if - elif - else
nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

print(f"Nilai {nilai} -> grade {grade}")


# 3. Nested if
umur = 20
punya_ktp = True

if umur >= 17:
    if punya_ktp:
        print("Boleh memilih")
    else:
        print("Buat KTP dulu")


# 4. Ternary
umur = 16
status = "dewasa" if umur >= 17 else "anak"
print(status)


# 5. Match-case
hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")
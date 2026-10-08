# BAB 09 - Error Handling

# 1. Try - Except - Else - Finally
try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka

except ValueError:
    print("Harus berupa angka!")

except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")

else:
    print(f"Hasil: {hasil}")

finally:
    print("Program selesai.")


# 2. Raise
def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak valid")
    return umur


try:
    set_umur(-5)

except ValueError as e:
    print(f"Error: {e}")
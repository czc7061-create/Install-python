# Kalkulator Sederhana di Python

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi 0"
    return a / b

print("=== Kalkulator Sederhana ===")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Pilih operasi (1/2/3/4): ")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    print(f"Hasil: {tambah(a, b)}")
elif pilihan == "2":
    print(f"Hasil: {kurang(a, b)}")
elif pilihan == "3":
    print(f"Hasil: {kali(a, b)}")
elif pilihan == "4":
    print(f"Hasil: {bagi(a, b)}")
else:
    print("Pilihan tidak valid")

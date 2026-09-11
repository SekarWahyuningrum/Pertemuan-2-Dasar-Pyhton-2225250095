# ==========================================
# PROGRAM ANALISIS PERSEGI PANJANG
# ==========================================

import math

print("╔══════════════════════════════════╗")
print("║     ANALISIS PERSEGI PANJANG     ║")
print("╚══════════════════════════════════╝")

# Input
p = float(input("\nMasukkan panjang : "))
l = float(input("Masukkan lebar   : "))

# Proses perhitungan
luas = p * l
keliling = 2 * (p + l)
diagonal = math.sqrt(p**2 + l**2)

# Menentukan karakteristik
if p == l:
    jenis = "Persegi"
elif p > l:
    jenis = "Persegi Panjang (horizontal)"
else:
    jenis = "Persegi Panjang (vertikal)"

# Output
print("\n────── HASIL ANALISIS ──────")
print(f"Panjang       : {p}")
print(f"Lebar         : {l}")
print(f"Luas          : {luas}")
print(f"Keliling      : {keliling}")
print(f"Diagonal      : {diagonal:.2f}")
print(f"Karakteristik : {jenis}")

print("\nProgram selesai ✓")
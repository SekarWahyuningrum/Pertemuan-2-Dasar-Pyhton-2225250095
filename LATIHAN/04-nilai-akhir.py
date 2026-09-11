# Program Menghitung Nilai Akhir

tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Bobot nilai
nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

print("\n=== HASIL NILAI ===")
print("Nilai Tugas :", tugas)
print("Nilai UTS   :", uts)
print("Nilai UAS   :", uas)
print("Nilai Akhir :", nilai_akhir)
# Data Mahasiswa

nama = input("nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun Lahir: "))
tahun_sekarang = int(input("Tahun Sekarang: "))

umur = tahun_sekarang - tahun_lahir

print("Nama:", nama)
print("NIM:", nim)
print("Kelas:", kelas)
print("Tahun Lahir:", tahun_lahir)
print("Umur:", umur, "tahun")
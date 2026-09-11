# Identitas

**Nama:** Sekar Wahyuningrum

**NIM:** 2225250095

**Kelas:** 3E

**Mata Kuliah:** Algoritma dan Pemrograman  

**Program Studi:** Pendidikan Matematika  

**Universitas:** Universitas Sultan Ageng Tirtayasa (UNTIRTA)

## Tujuan Repository

Repository ini dibuat untuk menyimpan dan mendokumentasikan hasil latihan pemrograman Python pada mata kuliah Algoritma dan Pemrograman.

Melalui repository ini, mahasiswa dapat:
- Mempraktikkan dasar-dasar pemrograman Python.
- Memahami penggunaan input dan output.
- Menerapkan variabel, konstanta, dan tipe data.
- Menggunakan operasi aritmatika dalam program.
- Melakukan pengujian program dengan beberapa contoh input.
- Mendokumentasikan hasil latihan menggunakan GitHub.

- ## Daftar Berkas dan Fungsi

| No. | Berkas | Fungsi |
|---|---|---|
| 1 | `latihan/01_biodata.py` | Meminta nama, NIM, kelas, dan tahun lahir, kemudian menghitung perkiraan umur dan menampilkan kartu biodata. |
| 2 | `latihan/02_persegi_panjang.py` | Meminta panjang dan lebar, kemudian menghitung luas dan keliling persegi panjang. |
| 3 | `latihan/03_konversi_suhu.py` | Mengubah suhu dari Celsius ke Fahrenheit dan Kelvin menggunakan rumus konversi suhu. |
| 4 | `latihan/04_nilai_akhir.py` | Menghitung nilai akhir berdasarkan nilai tugas, UTS, dan UAS dengan bobot 30%, 30%, dan 40%. |
| 5 | `tugas_utama/kalkulator_koordinat.py` | Menghitung perubahan koordinat, jarak antara dua titik, dan titik tengah dari titik A dan titik B. |
| 6 | `README.md` | Berisi identitas, tujuan repository, daftar berkas, cara menjalankan program, hasil pengujian, refleksi, dan sumber yang digunakan. |

## Cara Menjalankan Program

Program dapat dijalankan melalui terminal dengan perintah berikut:

### Latihan 1 - Biodata

```bash
python latihan/01_biodata.py
```

### Latihan 2 - Persegi Panjang

```bash
python latihan/02_persegi_panjang.py
```

### Latihan 3 - Konversi Suhu

```bash
python latihan/03_konversi_suhu.py
```

Setelah menjalankan program, masukkan data sesuai dengan input yang diminta pada terminal.

### Latihan 4 - Nilai Akhir

```bash
python latihan/04_nilai_akhir.py
```

### Tugas Utama - Kalkulator Koordinat Dua Titik

Jalankan program melalui terminal dengan perintah:

```bash
python tugas_utama/kalkulator_koordinat.py
```

Kemudian masukkan koordinat titik A dan titik B sesuai dengan input yang diminta.

## Hasil Test Case

### 1. Program Biodata

| Test Case | Nama | NIM | Kelas | Tahun Lahir | Hasil Umur |
|---|---|---|---|---:|---:|
| 1 | Sekar Wahyuningrum | 2225250095 | Pendidikan Matematika | 2007 | 19 tahun |


**Hasil:** Program berhasil menerima input nama, NIM, kelas, dan tahun lahir serta menghitung perkiraan umur berdasarkan tahun lahir.

---

### 2. Program Persegi Panjang

| Test Case | Panjang | Lebar | Luas | Keliling |
|---|---:|---:|---:|---:|
| 1 | 8 | 5 | 40.00 | 26.00 |


**Hasil:** Program berhasil menghitung luas dan keliling persegi panjang sesuai dengan rumus.

---

### 3. Program Konversi Suhu

| Test Case | Celsius | Fahrenheit | Kelvin |
|---|---:|---:|---:|
| 1 | 0 | 32.00 °F | 273.15 K |
| 2 | 100 | 212.00 °F | 373.15 K |

**Hasil:** Program berhasil mengonversikan suhu dari Celsius ke Fahrenheit dan Kelvin dengan hasil yang sesuai.

---

### 4. Program Nilai Akhir

| Test Case | Nilai Tugas | Nilai UTS | Nilai UAS | Nilai Akhir |
|---|---:|---:|---:|---:|
| 1 | 100 | 98 | 97 | 98.02 |


**Hasil:** Program berhasil menghitung nilai akhir berdasarkan bobot nilai tugas 30%, UTS 30%, dan UAS 40%.

---

### 5. Tugas Utama – Kalkulator Koordinat Dua Titik

| Test Case | Titik A | Titik B | dx | dy | Jarak | Titik Tengah |
|---|---|---|---:|---:|---:|---|
| 1 | (0, 0) | (3, 4) | 3.00 |4.00 | 5.00 | (1.50, 2.00) |
| 2 | (-2, 4) | (4, 1) | 6.00 | 0.00 | 6.00 | (1.00, 1.00) |
| 3 | (2,5, -1) | (2,5, 3) | 0.00 | 4.00 | 4.00 | (2.50, 1.00) |


**Hasil:** Program berhasil menghitung perubahan koordinat, jarak antara dua titik, dan titik tengah dengan hasil yang sesuai.

---

## Kesimpulan Pengujian

Berdasarkan test case yang telah dilakukan, seluruh program dapat menerima input dan menghasilkan output sesuai dengan perhitungan yang diharapkan. Pengujian dilakukan menggunakan beberapa variasi data untuk memastikan setiap program dapat berjalan dengan baik.


### Kesimpulan Pengujian

Berdasarkan beberapa pengujian, program berhasil menghitung perubahan koordinat, jarak antara dua titik, dan titik tengah dengan hasil yang sesuai dengan perhitungan manual.

## Refleksi

Melalui tugas utama ini, saya belajar menerapkan konsep koordinat dua titik ke dalam program Python. Saya memahami cara menghitung perubahan koordinat, jarak antara dua titik, dan titik tengah menggunakan rumus matematika.

Saya juga belajar menggunakan input `float`, operasi aritmatika, serta f-string untuk menampilkan hasil dengan format yang lebih rapi. Dari pengujian yang dilakukan, saya memahami pentingnya mengecek hasil program dengan perhitungan manual agar program dapat dipastikan berjalan dengan benar.

## Sumber yang Digunakan

1. Modul/Bahan Ajar Mata Kuliah Algoritma dan Pemrograman.
2. Materi koordinat Kartesius dan jarak antara dua titik.
3. Dokumentasi resmi Python untuk penggunaan `input()`, `float()`, operasi aritmatika, dan f-string.

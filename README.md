1. Import Modul
import random
import statistics

- `random` digunakan untuk menghasilkan nilai acak antara 0 dan 100.
- `statistics` digunakan untuk menghitung rata-rata nilai siswa.

2. Fungsi `main()`
def main():
    """Program sederhana untuk mengolah data nilai siswa."""
    data_siswa = {}
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    for i in range(jumlah_siswa):
        nama = input(f"Masukkan nama siswa ke-{i+1}: ")
        nilai = [random.randint(0, 100) for _ in range(5)]
        data_siswa[nama] = nilai

- `data_siswa = {}` adalah dictionary untuk menyimpan data siswa dalam format `{nama: [nilai1, nilai2, ..., nilai5]}`.
- Pengguna memasukkan jumlah siswa, lalu program meminta nama setiap siswa.
- Untuk setiap siswa, program membuat 5 nilai acak (0–100) menggunakan `random.randint(0, 100)`, lalu menyimpannya dalam dictionary.


3. Menu Pilihan
while True:
    print("\nMenu:")
    print("1. Tampilkan data siswa")
    print("2. Hitung rata-rata nilai")
    print("3. Hitung nilai tertinggi dan terendah")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        tampilkan_data_siswa(data_siswa)
    elif pilihan == "2":
        hitung_rata_rata(data_siswa)
    elif pilihan == "3":
        hitung_nilai_ekstrem(data_siswa)
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid.")

- Looping menu: Program akan terus berjalan sampai pengguna memilih "4" untuk keluar.
- Jika pengguna memilih 1, program memanggil `tampilkan_data_siswa(data_siswa)`.
- Jika pengguna memilih 2, program memanggil `hitung_rata_rata(data_siswa)`.
- Jika pengguna memilih 3, program memanggil `hitung_nilai_ekstrem(data_siswa)`.
- Jika pengguna memilih opsi lain, program akan menampilkan pesan "Pilihan tidak valid."


4. Fungsi `tampilkan_data_siswa(data_siswa)`
def tampilkan_data_siswa(data_siswa):
    """Menampilkan data nilai siswa."""
    print("\nData Nilai Siswa:")
    for nama, nilai in data_siswa.items():
        print(f"{nama}: {nilai}")

- Fungsi ini menampilkan semua data siswa dalam bentuk `{nama: [nilai1, nilai2, ..., nilai5]}`.


5. Fungsi `hitung_rata_rata(data_siswa)`
def hitung_rata_rata(data_siswa):
    """Menghitung dan menampilkan rata-rata nilai siswa."""
    nama_siswa = input("Masukkan nama siswa: ")
    if nama_siswa in data_siswa:
        rata_rata = statistics.mean(data_siswa[nama_siswa])
        print(f"Rata-rata nilai {nama_siswa}: {rata_rata}")
    else:
        print("Nama siswa tidak ditemukan.")

- Pengguna memasukkan nama siswa.
- Jika siswa ada dalam dictionary, program menghitung rata-rata dengan `statistics.mean()` dan menampilkannya.
- Jika siswa tidak ditemukan, muncul pesan error.

---

6. Fungsi `hitung_nilai_ekstrem(data_siswa)`
def hitung_nilai_ekstrem(data_siswa):
    """Menghitung dan menampilkan nilai tertinggi dan terendah siswa."""
    nama_siswa = input("Masukkan nama siswa: ")
    if nama_siswa in data_siswa:
        nilai_tertinggi = max(data_siswa[nama_siswa])
        nilai_terendah = min(data_siswa[nama_siswa])
        print(f"Nilai tertinggi {nama_siswa}: {nilai_tertinggi}")
        print(f"Nilai terendah {nama_siswa}: {nilai_terendah}")
    else:
        print("Nama siswa tidak ditemukan.")

- Pengguna memasukkan nama siswa.
- Jika siswa ditemukan, program menampilkan nilai tertinggi dengan `max()` dan nilai terendah dengan `min()`.
- Jika siswa tidak ada, program menampilkan pesan error.

7. Blok `if __name__ == "__main__":`
if __name__ == "__main__":
    main()

- Memastikan bahwa program hanya berjalan jika dieksekusi langsung, bukan diimpor sebagai modul.

Cara Kerja Program
1. Pengguna memasukkan jumlah siswa dan nama-nama mereka.
2. Program secara otomatis memberikan 5 nilai acak untuk setiap siswa.
3. Pengguna memilih dari menu:
   - 1 untuk melihat data siswa.
   - 2 untuk melihat rata-rata nilai siswa tertentu.
   - 3 untuk melihat nilai tertinggi dan terendah siswa tertentu.
   - 4 untuk keluar.

Contoh Output

Masukkan jumlah siswa: 2
Masukkan nama siswa ke-1: Budi
Masukkan nama siswa ke-2: Ani

Menu:
1. Tampilkan data siswa
2. Hitung rata-rata nilai
3. Hitung nilai tertinggi dan terendah
4. Keluar
Masukkan pilihan Anda: 1

Data Nilai Siswa:
Budi: [87, 45, 78, 90, 66]
Ani: [55, 100, 88, 79, 92]

Masukkan pilihan Anda: 2
Masukkan nama siswa: Budi
Rata-rata nilai Budi: 73.2

Masukkan pilihan Anda: 3
Masukkan nama siswa: Ani
Nilai tertinggi Ani: 100
Nilai terendah Ani: 55

Masukkan pilihan Anda: 4

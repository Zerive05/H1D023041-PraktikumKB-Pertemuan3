import random
import statistics

def main():
  """Program sederhana untuk mengolah data nilai siswa."""
  data_siswa = {}
  jumlah_siswa = int(input("Masukkan jumlah siswa: "))
  for i in range(jumlah_siswa):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = [random.randint(0, 100) for _ in range(5)]
    data_siswa[nama] = nilai

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

def tampilkan_data_siswa(data_siswa):
  """Menampilkan data nilai siswa."""

  print("\nData Nilai Siswa:")
  for nama, nilai in data_siswa.items():
    print(f"{nama}: {nilai}")

def hitung_rata_rata(data_siswa):
  """Menghitung dan menampilkan rata-rata nilai siswa."""

  nama_siswa = input("Masukkan nama siswa: ")
  if nama_siswa in data_siswa:
    rata_rata = statistics.mean(data_siswa[nama_siswa])
    print(f"Rata-rata nilai {nama_siswa}: {rata_rata}")
  else:
    print("Nama siswa tidak ditemukan.")

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

if __name__ == "__main__":
  main()
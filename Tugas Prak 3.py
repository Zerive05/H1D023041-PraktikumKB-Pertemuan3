import random
import statistics

def main():
  """Program sederhana untuk mengolah data nilai siswa."""
  datas = {}
  jumlahs = int(input("Masukkan jumlah siswa: "))
  for i in range(s):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = [random.randint(0, 100) for _ in range(5)]
    datas[nama] = nilai

  while True:
    print("\nMenu:")
    print("1. Tampilkan data siswa")
    print("2. Hitung rata-rata nilai")
    print("3. Hitung nilai tertinggi dan terendah")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
      tampilkan_data_siswa(datas)
    elif pilihan == "2":
      hitung_rata_rata(datas)
    elif pilihan == "3":
      hitung_nilai_ekstrem(datas)
    elif pilihan == "4":
      break
    else:
      print("Pilihan tidak valid.")

def tampilkan_data_siswa(datas):
  """Menampilkan data nilai siswa."""

  print("\nData Nilai Siswa:")
  for nama, nilai in datas.items():
    print(f"{nama}: {nilai}")

def hitung_rata_rata(datas):
  """Menghitung dan menampilkan rata-rata nilai siswa."""

  namas = input("Masukkan nama siswa: ")
  if namas in datas:
    rata_rata = statistics.mean(datas[namas])
    print(f"Rata-rata nilai {namas}: {rata_rata}")
  else:
    print("Nama siswa tidak ditemukan.")

def hitung_nilai_ekstrem(datas):
  """Menghitung dan menampilkan nilai tertinggi dan terendah siswa."""

  namas = input("Masukkan nama siswa: ")
  if namas in datas:
    nilaitinggi = max(datas[namas])
    nilairendah = min(data_siswa[namas])
    print(f"Nilai tertinggi {namas}: {ntinggi}")
    print(f"Nilai terendah {namas}: {nrendah}")
  else:
    print("Nama siswa tidak ditemukan.")

if __name__ == "__main__":
  main()

# Gaji Pokok
gaji_pokok = 3000000
nama_karyawan = input("Nama Karyawan: ")

# Input Tunjangan Jabatan
golongan = int(input("Masukan Golongan Jabatan (1/2/3): "))

# Hitung Tunjangan Jabatan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan Jabatan Tidak Valid!")

# Input Tunjangan Pendidikan
pendidikan = input("Masukan Pendidikan Terakhir (SMA/D1/D3/S1): ").upper()

# Hitung Tunjangan Pendidikan
if pendidikan == "SMA": 
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    print("Pendidikan Tidak Valid!")

# Input Jam Lembur
jam_lembur = int(input("Masukan Jumlah Jam Lembur: "))
honor_lembur = 35000 * jam_lembur if jam_lembur > 8 else 0

# Hitung Total Gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Output
print("--- Rincian Gaji ---")
print(f"Karyawan Yang Bernama {nama_karyawan} honor yang diterima")
print(f"Gaji Pokok: Rp.{gaji_pokok}")
print(f"Tunjangan Jabatan: Rp.{tunjangan_jabatan}")
print(f"Honor Lembur: Rp.{honor_lembur}")
print(f"Total Gaji: Rp.{total_gaji}")
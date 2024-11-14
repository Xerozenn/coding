# Input Data dari Pengguna
nama = input("Masukkan Nama Karyawan: ")
golongan = int(input("Masukkan Golongan Jabatan [1/2/3]: "))
pendidikan = input("Masukkan Tingkat Pendidikan [SMA/D1/D3/S1]: ").upper()
jam_kerja_per_hari = int(input("Masukkan jumlah jam kerja per hari: "))  # Input jumlah jam kerja per hari
jumlah_hari_kerja = int(input("Masukkan jumlah hari kerja: "))  # Input jumlah hari kerja

# Gaji Pokok
gaji_pokok = 3000000  # Gaji pokok diubah menjadi Rp. 3.000.000

# Tunjangan Jabatan berdasarkan Golongan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid, tunjangan jabatan = 0")

# Tunjangan Pendidikan berdasarkan Pendidikan
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
    print("Pendidikan tidak valid, tunjangan pendidikan = 0")

# Perhitungan Honor Lembur
if jam_kerja_per_hari > 8:
    jam_lembur_per_hari = jam_kerja_per_hari - 8  # Menghitung jumlah jam lembur per hari
    honor_lembur_per_hari = jam_lembur_per_hari * 35000  # Perhitungan honor lembur per hari (Rp. 35.000 per jam lembur)
else:
    honor_lembur_per_hari = 0  # Tidak ada lembur jika jam kerja <= 8

# Perhitungan Total Jam Kerja
total_jam_kerja = jam_kerja_per_hari * jumlah_hari_kerja  # Menghitung total jam kerja

# Perhitungan Honor Lembur Total
total_honor_lembur = honor_lembur_per_hari * jumlah_hari_kerja  # Menghitung total honor lembur

# Total Gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + total_honor_lembur

# Tampilkan Hasil
print("\n--- Rincian Gaji ---")
print(f"Nama Karyawan: {nama}")
print(f"Gaji Pokok: Rp. {gaji_pokok}")
print(f"Tunjangan Jabatan: Rp. {tunjangan_jabatan}")
print(f"Tunjangan Pendidikan: Rp. {tunjangan_pendidikan}")
print(f"Honor Lembur: Rp. {total_honor_lembur}")
print(f"Total Jam Kerja: {total_jam_kerja} jam")
print(f"Total Gaji: Rp. {total_gaji}")

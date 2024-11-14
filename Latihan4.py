# Program Toko Mainan Anak

# Input Data Pembeli dan Mainan
nama_pembeli = input("Masukkan Nama Pembeli: ")
kode_mainan = input("Masukkan Kode Mainan: ")
harga = int(input("Masukkan Harga: "))
jumlah_beli = int(input("Masukkan Jumlah Beli: "))

# Menghitung Total Harga
total_harga = harga * jumlah_beli

# Output Struk Pembelian
print("\n")
print("")
print("            TOKO MAINAN ANAK        ")
print("")
print(f"Nama Pembeli : {nama_pembeli}")
print(f"Kode Mainan  : {kode_mainan}")
print(f"Harga        : {harga}")
print(f"Jumlah Beli  : {jumlah_beli}")
print("------------------------------------")
print(f"Total        : {total_harga}")
print("**************************************************")
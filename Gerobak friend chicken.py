#daftar harga ayam perpotong
harga_ayam = {'D' : 10000, 'P' : 8000, 'S' : 7000}

#harga dan jenis ayam yang dibeli
jumlah_jenis = int(input("Berapa banyak jenis ayam yang dibeli? "))

total_bayar = 0

#loop untuk input jenis potongan ayam yang dibeli
for i in range (jumlah_jenis):
    kode = input("Kode Potong(D/P/S): ").upper()
    jumlah = int(input("Berapa banyak potong? "))

#perhitungan total harga potongan ayam
if kode in harga_ayam: total_bayar+= harga_ayam[kode] * jumlah
else:
    print("Kode potong tidak valid!")

#pajak dan total harga
pajak = total_bayar *0.10
total_dengan_pajak = total_bayar + pajak

#hasil
print("\nGEROBAK FRIED CHICKEN")
print("--------------------------------------------------")
print("No. Jenis Potong  Harga   Banyak  Jumlah")
print("                 Satuan  Beli    Harga")
print("--------------------------------------------------")

total_bayar = 0

print("--------------------------------------------------")
print(f"Jumlah Bayar   Rp. {total_bayar}")
print(f"Pajak 10%      Rp. {pajak}")
print(f"Total Bayar    Rp. {total_dengan_pajak}")


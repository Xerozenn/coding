# Daftar harga potongan ayam
harga_ayam = {'D (Dada)': 10000, 'P (Paha)': 8000, 'S (Sayap)': 7000}

# Input jumlah jenis potongan yang dibeli
jumlah_jenis = int(input("Banyak Jenis : "))
transaksi = []

# Loop untuk menginput jenis potongan dan jumlah beli
for i in range(jumlah_jenis):
    print(f"\nJenis Ke-{i + 1}:")
    kode = input("Kode Potong (D/P/S): ").upper()
    jumlah = int(input("Banyak Potong: "))
    
    # Hitung total harga untuk setiap jenis potongan
    if kode in harga_ayam:
        harga_satuan = harga_ayam[kode]
        total_harga = harga_satuan * jumlah
        transaksi.append([kode, harga_satuan, jumlah, total_harga])
    else:
        print("Kode potong tidak valid!")

# Menampilkan hasil transaksi
print("\nGEROBAK FRIED CHICKEN")
print("--------------------------------------------------")
print("No. Jenis   Harga   Banyak  Jumlah")
print("    Potong  Satuan  Beli    Harga")
print("--------------------------------------------------")

total_bayar = 0
for i, item in enumerate(transaksi, 1):
    kode_potong, harga_satuan, jumlah_beli, total_harga = item
    print(f"{i}.   {kode_potong}          Rp. {harga_satuan}     {jumlah_beli}     Rp. {total_harga}")
    total_bayar += total_harga

# Menghitung pajak dan total bayar dengan pajak
pajak = total_bayar * 0.10
total_dengan_pajak = total_bayar + pajak

print("--------------------------------------------------")
print(f"Jumlah Bayar   Rp. {total_bayar}")
print(f"Pajak 10%      Rp. {pajak}")
print(f"Total Bayar    Rp. {total_dengan_pajak}")
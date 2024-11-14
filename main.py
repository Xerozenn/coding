MENU =['CAPUCINO', 'LATTE', 'EMERICANO', 'VIETNAM DRIP']

for item in MENU:
    print(f' {item}')

choise = input('pilih menu yangg anada mau: ')

if  choise == 'capucino':
    harga = int(200000)
elif choise == 'latte':
    harga = int(250000)
elif choise == 'americano':
    harga = int(300000)
elif choise == 'vietnam drip':
    harga = int(3500000)

many = int(input('mau berapa banyak:  '))

total = harga * many
pajak = total * (10/100)
total_akhir = total + pajak

print(f'anda membeli {item} dengan harga {harga} anda membeli sebnayak {many}')
print(f'pajak {pajak}')
print(f'total {total_akhir}')
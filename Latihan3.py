nama= input("Masukan Nama Anda : ")
jabatan= input("Masukan Jabatan Anda : ")
gaji= int(input("Masukan Gaji Anda : "))

#Listing rumus pajak
pajak= 0.1*gaji

print("Nama : " +str(nama))
print("Jabatan : " +str(jabatan))
print("gaji : " ,(gaji))
print("pajak : " ,int(pajak))
#Kullanicadan hangi islem yapmasını istiyoruz.

print("Hesap Makinesi")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
#input fonksiyonu ile secim islemini kullanicidan aliyoruz
secim = input("İşlem yapmak istediğiniz numarayı girin (1)-(2)-(3)-(4): ")
#Kullanicidan iki tane sayi alıyoruz. Islemi yapmak icin
sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
#Kullaici 1 ile 4 arasinda secim yapıyor. Yapmak istedigi islemi bu sekilde seciyor.
if secim == '1':
   print(sayi1,"+",sayi2,"=", sayi1+sayi2)

elif secim == '2':
   print(sayi1,"-",sayi2,"=", sayi1-sayi2)

elif secim == '3':
   print(sayi1,"*",sayi2,"=", sayi1*sayi2)

elif secim == '4':
   print(sayi1,"/",sayi2,"=", sayi1/sayi2)

else:
   print("Geçersiz işlem seçtiniz.")
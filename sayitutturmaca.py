# modüller
import random

# başlangıç
print("----------------")
print("SAYI TUTTURMACA")
print("Coded By Xale ~ @xaletr")
print("----------------")
print(" ")
sayi = int(input("0 ile 10 arasında bir sayı girin : "))

# random sayı
rndm = random.randint(0,10)

# tuttu & tutmadı
if sayi == rndm:
	print("Tuttu :)")
	print("Olması Gereken Sayı : ")
	print(rndm)
	print("Girdiğiniz Sayı : ")
	print(sayi)
else:
	print("Tutmadı :(")
	print("Olması Gereken Sayı : ")
	print(rndm)
	print("Girdiğiniz Sayı : ")
	print(sayi)

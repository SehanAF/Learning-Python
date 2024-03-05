# Tuliskan program untuk menentukan bilangan itu bilangan positif, negatif atau 0

bilangan = int(input("Masukan bilangan anda: "))

if bilangan == 0:
    print(f"Bilangan ini adalah {bilangan}")
elif bilangan >= 1:
    print("Bilangan ini adalah positif")
else:
    print("Bilangan ini adalah negatif")
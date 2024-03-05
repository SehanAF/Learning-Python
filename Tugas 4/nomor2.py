# Tulisan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih kecil

bilangan1 = 10
bilangan2 = 20
bilangan3 = 2

if bilangan1 < bilangan2 and bilangan1 < bilangan3:
    print(f"Angka {bilangan1} lebih kecil dari angka {bilangan2} dan angka {bilangan3}")
elif bilangan2 < bilangan3 and bilangan2 < bilangan1:
    print(f"Angka {bilangan2} lebih kecil dari angka {bilangan3} dan angka {bilangan1}")
elif bilangan3 < bilangan1 and bilangan3 < bilangan2:
    print(f"Angka {bilangan3} lebih kecil dari angka {bilangan2} dan angka {bilangan1}")
else:
    print(f"Angka {bilangan3}, angka {bilangan2} dan angka {bilangan1} adalah sama besar.")    
    
    
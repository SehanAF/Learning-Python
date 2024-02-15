alas = float(input("Masukan angka alas: "))
tinggi = float(input("Masukan angka tinggi: "))

sisiA = 20
sisiB = 15
sisiC = 10

rumusLuas = 1 / 2 * alas * tinggi
rumusKelilingSegitiga = sisiA + sisiB + sisiC

print("Hasil luas segitiga dengan alas %.0f cm dan tinggi %.0f cm adalah %.2f cm." % (alas, tinggi, rumusLuas))
print("Hasil keliling segitiga dengan sisi A %.0f cm, sisi B %.0f cm, dan sisi C %.0f cm adalah %.2f cm." % (sisiA, sisiB, sisiC, rumusKelilingSegitiga))
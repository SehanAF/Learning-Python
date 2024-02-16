alas = float(input("Masukan angka alas: "))
tinggi = float(input("Masukan angka tinggi: "))

sisi_a = 20
sisi_b = 15
sisi_c = 10

rumusLuas = 1 / 2 * alas * tinggi
rumusKelilingSegitiga = sisi_a + sisi_b + sisi_c

print(f"Hasil luas segitiga dengan alas {alas:.0f} cm dan tinggi {tinggi:.0f} cm adalah {rumusLuas:.2f} cm².")
print(f"Hasil keliling segitiga dengan sisi A {sisi_a:.0f} cm, sisi B {sisi_b:.0f} cm, dan sisi C {sisi_c:.0f} cm adalah {rumusKelilingSegitiga:.2f} cm.")
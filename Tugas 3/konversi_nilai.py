nilai = float(input("Masukan nilai anda: "))

if nilai >= 0 and nilai < 50:
    print("Nilai kamu E")
elif nilai >= 50 and nilai <= 60:
    print("Nilai kamu D")
elif nilai >= 60 and nilai <= 70:
    print("Nilai kamu C")
elif nilai >= 70 and nilai <= 80:
    print("Nilai kamu B")
else:
    print("Nilai kamu A")
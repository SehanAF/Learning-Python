# Program yang mensimulasikan permainan batu-gunting-kertas antara dua pemain dan menentukan pemenangnya.

pemain_satu = input("Masukan: ").lower()
pemain_dua = input("Masukan: ").lower()

if pemain_satu == "batu" and pemain_dua == "gunting":
    print("Pemenang: pemain satu")
elif pemain_satu == "batu" and pemain_dua == "kertas":
    print("Pemenang: pemain dua")
elif pemain_satu == "gunting" and pemain_dua == "kertas":
    print("Pemenang: pemain satu")
elif pemain_satu == "gunting" and pemain_dua == "batu":
    print("Pemenang: pemain dua")
elif pemain_satu == "kertas" and pemain_dua == "batu":
    print("Pemenang: pemain satu")
elif pemain_satu == "kertas" and pemain_dua == "gunting":
    print("Pemenang: pemain dua")
else:
    print("Permainan seri!")

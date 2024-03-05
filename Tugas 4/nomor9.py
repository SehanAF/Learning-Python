# Buatlah Perhitungan IPK untuk semester ini berdasarkan nilai yang di input
# Mata kuliah semster ini adalah Algoritma, Perancangan Objek, Kalkulus, Etika Profesi, Databases, dan English 1
# referensi : https://www.ekrut.com/media/cara-menghitung-ipk

algoritma = int(input("Masukkan nilai Algoritma: "))
perancangan_objek = int(input("Masukkan nilai Perancangan Objek: "))
kalkulus = int(input("Masukkan nilai Kalkulus: "))
etika_profesi = int(input("Masukkan nilai Etika Profesi: "))
database = int(input("Masukkan nilai Database: "))
english = int(input("Masukkan nilai Bahasa Inggris: "))

kredit_per_matkul = 3

def skor_bobot(skor):
    if skor >= 90:
        return 4
    elif skor >= 85:
        return 3.75
    elif skor >= 80:
        return 3.5
    elif skor >= 75:
        return 3.25
    elif skor >= 70:
        return 3
    elif skor >= 65:
        return 2.75
    elif skor >= 60:
        return 2.5
    elif skor >= 55:
        return 2.25
    elif skor >= 50:
        return 2
    elif skor >= 45:
        return 1.75
    elif skor >= 40:
        return 1.5
    elif skor >= 35:
        return 1.25
    elif skor >= 30:
        return 1
    elif skor < 30:
        return 0, 'E'
    else:
        return None, "Invalid Score"
    
total_algoritma = kredit_per_matkul * skor_bobot(algoritma)
total_perancangan_objek  = kredit_per_matkul * skor_bobot(perancangan_objek)
total_kalkulus = kredit_per_matkul * skor_bobot(kalkulus)
total_etika_profesi = kredit_per_matkul * skor_bobot(etika_profesi)
total_database = kredit_per_matkul * skor_bobot(database)
total_english = kredit_per_matkul * skor_bobot(english)

total_kredit = kredit_per_matkul * 6  # 6 = jumlah matkul.

total_ipk = (total_algoritma + total_perancangan_objek + total_kalkulus + total_etika_profesi + total_database + total_english) / total_kredit

print(f"Indeks Prestasi Kumulatif (IPK) Anda adalah: {total_ipk:.2f}")
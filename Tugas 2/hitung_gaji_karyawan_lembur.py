# masih ada 1 error yg blm di perbaiki, yaitu ketika memasukan input gaji >= 1.000.000 , maka kode akan error (masih blm nemu solusi).
# jika <= 1.000.000 masih aman.

hari_kerja = ("senin", "selasa", "rabu", "kamis", "jumat")
hari_libur_sabtu = ("sabtu")
hari_libur_minggu = ("minggu")
hari_libur_nasional = ("natal", "tahun baru")
lembur_hari = 0

uang_transport = 150.000
uang_makan = 255.000
tunjangan = 355.000

gaji_pokok = float(input("Masukan gaji pokok anda: "))
mencari_hari_lembur = input("Masukan hari lembur: ").lower()
mencari_jam_lembur = float(input("Masukan jam lembur: "))
 
if mencari_hari_lembur in hari_kerja:
    if mencari_jam_lembur == 1:
        lembur_hari = mencari_jam_lembur * 1.5 * (1/173) * gaji_pokok
    elif mencari_jam_lembur >= 2:
        lembur_hari = mencari_jam_lembur * 2 * (1/173) * gaji_pokok
    else:
        print("Maaf anda mencapai batas jam lembur")
elif mencari_hari_lembur in hari_libur_sabtu:
    if mencari_jam_lembur >= 1:
        lembur_hari = mencari_jam_lembur * 2 * (1/173) * gaji_pokok
    elif mencari_jam_lembur == 9:
        lembur_hari = mencari_jam_lembur * 3 * (1/173) * gaji_pokok
    elif 10 <= mencari_jam_lembur <= 11:
        lembur_hari = mencari_jam_lembur * 4 * (1/173) * gaji_pokok
    else:
        print("Maaf anda mencapai batas jam lembur")
elif mencari_hari_lembur in hari_libur_minggu:
    if mencari_jam_lembur <= 7:
        lembur_hari = mencari_jam_lembur * 2 * (1/173) * gaji_pokok
    elif mencari_jam_lembur == 8:
        lembur_hari = mencari_jam_lembur * 3 * (1/173) * gaji_pokok
    elif 9 <= mencari_jam_lembur <= 10:
        lembur_hari = mencari_jam_lembur * 4 * (1/173) * gaji_pokok
    else:
        print("Maaf anda mencapai batas jam lembur")
elif mencari_hari_lembur in hari_libur_nasional:
    if mencari_jam_lembur <= 5:
        lembur_hari = mencari_jam_lembur * 2 * (1/173) * gaji_pokok
    elif mencari_jam_lembur == 6:
        lembur_hari = mencari_jam_lembur * 3 * (1/173) * gaji_pokok
    elif 7 <= mencari_jam_lembur <= 8:
        lembur_hari = mencari_jam_lembur * 4 * (1/173) * gaji_pokok
    else:
        print("Maaf anda mencapai batas jam lembur")
else:
    print("Hari lembur tidak valid")
    
if lembur_hari > 0:
    gaji_total = gaji_pokok + (uang_transport + uang_makan + tunjangan + lembur_hari)
    print(f"Total gaji lembur adalah: {lembur_hari:,.2f} rupiah")
    print(f"Total gaji karyawan setelah digabung dengan gaji lembur adalah: {gaji_total:,.2f} rupiah.")
else:
    print("Tidak ada gaji lembur yang dihitung.")

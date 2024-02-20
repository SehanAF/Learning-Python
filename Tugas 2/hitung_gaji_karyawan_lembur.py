hari_kerja = ("senin", "selasa", "rabu", "kamis", "jumat")
hari_libur_sabtu = ("sabtu")
hari_libur_minggu = ("minggu")

uang_transport = 150000
uang_makan = 255000
tunjangan = 355000

gaji_pokok = float(input("Masukan gaji pokok anda: "))
mencari_hari_lembur = input("Lembur dihari apa? ").lower()
mencari_jam_lembur = float(input("Masukan jam lembur yang diinginkan: "))
 
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
    print("Hari lembur tidak valid")
    
gaji_total = gaji_pokok + (uang_transport + uang_makan + tunjangan + lembur_hari)

print(f"Total gaji lemburnya adalah: {lembur_hari: 1,.3f} rupiah")

print(f"Total gaji karyawan setelah digabung gaji lembur adalah: {gaji_total: 1,.3f} rupiah.")






# if (mencari_hari_lembur in hari_kerja and mencari_jam_lembur == 1):
#     lembur_hari = mencari_jam_lembur * 1.5 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif (mencari_hari_lembur in hari_kerja and mencari_jam_lembur >= 2):
#     lembur_hari = mencari_jam_lembur * 2 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif (mencari_hari_lembur in hari_libur and mencari_jam_lembur >= 1):
#     lembur_hari = mencari_jam_lembur * 2 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif (mencari_hari_lembur in hari_libur == 9):
#     lembur_hari = mencari_jam_lembur * 3 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif (mencari_hari_lembur in hari_libur >= 10 <= 11):
#     lembur_hari = mencari_jam_lembur * 4 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# else:
#     print("Maaf anda mencapai batas jam lembur")
    



# Perhitungan Lembur Pada Hari Kerja

# if hari_kerja == 1:
#     lembur_hari = hari_kerja * 1.5 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif hari_kerja >= 2:
#     lembur_hari = hari_kerja * 2 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# else:
#     print("Maaf anda mencapai batas jam lembur")
    
    
# # Perhitungan Lembur Jumlah Hari Kerja 5 Hari Seminggu
    
# if lembur <= 8:
#     lembur_hari = lembur * 2 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif lembur == 9:
#     lembur_hari = lembur * 3 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif lembur >= 10 <= 11:
#     lembur_hari = lembur * 4 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# else:
#     print("Maaf anda mencapai batas jam lembur")
    
# # Perhitungan Lembur Jumlah Hari Kerja 6 Hari Seminggu

# if lembur <= 7:
#     lembur_hari = lembur * 2 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif lembur == 8:
#     lembur_hari = lembur * 3 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# elif lembur >= 9 <= 10:
#     lembur_hari = lembur * 4 * (1/173) * gaji_pokok
#     print(int(lembur_hari))
# else:
#     print("Maaf anda mencapai batas jam lembur")


# # Perhitungan Lembur Pada Hari Libur Nasional
    
    


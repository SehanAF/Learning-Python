gaji_pokok = float(input("Masukan gaji pokok anda: "))

uang_transport = 150.000
uang_makan = 255.000
tunjangan = 355.000
honor_lembur = 550.000

gaji_total = gaji_pokok + ( uang_transport + uang_makan + tunjangan + honor_lembur)

print(f"Total gaji karyawan adalah: {gaji_total: 1,.3f} rupiah.")
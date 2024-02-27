gaji_pokok = float(input("Masukan gaji pokok anda: "))

uang_transport = 150_000
uang_makan = 255_000
tunjangan = 355_000
honor_lembur = 550_000

gaji_total = gaji_pokok +  uang_transport + uang_makan + tunjangan + honor_lembur

print(f"Total gaji karyawan adalah: {gaji_total: 1,.0f} rupiah.")
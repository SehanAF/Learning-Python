uang_belanja = float(input("Masukan jumlah uang belanja: "))
total_barang = float(input("Masukan jumlah total harga barang: "))

sisa_kembalian = uang_belanja - total_barang

if total_barang > 70.000:
    diskon = total_barang * 0.10 
    sisa_kembalian += diskon
    print(f"Sisa kembalian anda setelah diskon adalah: {sisa_kembalian:.3f}")
else:     
    print(f"Sisa Kembalian anda adalah: {sisa_kembalian:.3f} rupiah.")
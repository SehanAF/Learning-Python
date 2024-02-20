uang_belanja = float(input("Masukan jumlah uang belanja: "))
total_barang = float(input("Masukan jumlah total harga barang: "))

total_belanja = uang_belanja - total_barang

if total_barang > 70.000:
    diskon = total_barang - 0.1
    print(f"Sisa kembalian anda setelah diskon adalah: {diskon:.3f}")
else:     
    print(f"Sisa Kembalian anda adalah: {total_belanja:.3f} rupiah.")
kilo_jeruk = 3
kilo_apel = 4
kilo_mangga = 5
kilo_manggis = 6
kilo_durian = 7

harga_jeruk = 15_000
harga_apel = 30_000
harga_mangga = 20_000
harga_manggis = 7_000
harga_durian = 50_000

total_harga = (kilo_jeruk * harga_jeruk) + (kilo_apel * harga_apel) + (kilo_mangga * harga_mangga) + (kilo_manggis * harga_manggis) + (kilo_durian * harga_durian)

print(f"Total harganya adalah: {total_harga:1,.3f} rupiah.")
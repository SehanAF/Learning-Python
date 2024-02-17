import datetime

year_born = int(input("Masukan tahun lahir kamu: "))
month_born = int(input("Masukan bulan lahir kamu: "))
day_born = int(input("Masukan tanggal lahir kamu: "))

now = datetime.datetime.now()

year_difference = now.year - year_born
month_difference =  month_born - now.month
day_difference = now.day - day_born

print(f"Umur kamu sekarang adalah: {year_difference} tahun, {month_difference} bulan, dan {day_difference} hari.")
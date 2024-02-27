import datetime

sekarang = datetime.datetime.now()

nama = input("Masukkan nama Anda: ")
tempat_lahir = input("Masukkan tempat lahir Anda: ")
tanggal_lahir = float(input("Masukkan tanggal lahir Anda: "))
bulan_lahir = float(input("Bulan lahir Anda: "))
tahun_lahir = float(input("Masukkan tahun lahir Anda: "))
nilai_indonesia = float(input("Masukkan nilai mata kuliah Bahasa Indonesia: "))
nilai_inggris = float(input("Masukkan nilai mata kuliah Bahasa Inggris: "))
nilai_matematika = float(input("Masukkan nilai mata kuliah Matematika: "))
jenis_kelamin = input("Silakan masukkan jenis kelamin Anda (Laki-laki/Perempuan): ").lower()

umur = sekarang.year - tahun_lahir
total_nilai = int(nilai_indonesia + nilai_inggris + nilai_matematika) / 3

if umur >= 25:
    print("Umur anda {umur} tahun, dan itu melebihi batas maksimum 25 tahun.")
elif total_nilai >= 80:
    if jenis_kelamin == "laki laki":
        jurusan = "Teknik Informatika"
        print(f"{nama}, selamat! Anda lolos dengan nilai total {total_nilai:0.0f}, berjenis kelamin {jenis_kelamin}, dan berumur {umur} tahun. Selamat bergabung di Jurusan {jurusan}.")
    elif jenis_kelamin == "perempuan":
        jurusan = "Sistem Informasi"
        print(f"{nama}, selamat! Anda lolos dengan nilai total {total_nilai:0.0f}, berjenis kelamin {jenis_kelamin}, dan berumur {umur} tahun. Selamat bergabung di Jurusan {jurusan}.")
    else:
        print("Jurusan tidak diketahui karena jenis kelamin tidak valid.")     
else:
    print(f"Maaf, nilai total kamu tidak mencapai 80, yaitu {total_nilai}, Jadi disarankan masuk DKV")




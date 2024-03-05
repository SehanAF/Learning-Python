# Buatlah form pendaftaran untuk masuk universitas
# Nama, Tempat lahir, Tanggal Lahir, Tahun lahir, 3 Nilai Mata Pelajaran (English, Mtk, Indonesia), Jenis Kelamin.
# Dia akan disarankan ke Jurusan Teknik Informatika jika rata-rata nilainya >=80 dan jenis kelaminnya laki-laki.
# Jurusan Sistem Informasi jika rata-rata nilainya >=80 dan jenis kelamin Perempuan
# Selebihnya disarankan masuk jurusan DKV
# Meskipun demikian, Mahasiswa yang diterima hanya yang dibawah umur 25

import datetime

sekarang = datetime.datetime.now()

nama = input("Masukkan nama Anda: ")
tempat_lahir = input("Masukkan tempat lahir Anda: ")
tanggal_lahir = int(input("Masukkan tanggal lahir Anda: "))
tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
nilai_indonesia = float(input("Masukkan nilai mata kuliah Bahasa Indonesia: "))
nilai_inggris = float(input("Masukkan nilai mata kuliah Bahasa Inggris: "))
nilai_matematika = float(input("Masukkan nilai mata kuliah Matematika: "))
jenis_kelamin = input("Silakan masukkan jenis kelamin Anda (Laki-laki/Perempuan): ").lower()

umur = sekarang.year - tahun_lahir
total_nilai = int(nilai_indonesia + nilai_inggris + nilai_matematika) / 3

if umur >= 25:
    print(f"Umur anda {umur} tahun, dan itu melebihi batas maksimum 25 tahun.")
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
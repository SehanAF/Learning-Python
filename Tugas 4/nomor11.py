# Buatlah program untuk menghitung kelayakan orang lulus organisasi X. Organisasi X memiliki kriteria untuk Anggota
# 1. Perempuan dengan berat badan minimal 45kilo gram, maks 50 kilogram dan Tingginya minimal 165 cm dan Usianya kurang dari 20 tahun
# 2. Laki-laki dengan berat badan maks 70 kilo dan Tingginya minimal 170 cm dan usianya maks 25 tahun
# 3. Laki-laki dan Perempuan dengan nilai rata-rata Akademis 90 dan usianya kurang dari 30 tahun
# 4. Laki-laki dan Perempuan yang Memiliki Skill Menembak, Memanah atau Berkuda

# Ke 4 Kriteria diatas akan diterima hanya dan hanya jika tidak memiliki anggota tubuh yang cacat.

# Buatlah Program Questioner untuk mengakomodasi kasus diatas.

jenis_kelamin = "perempuan"
berat_badan = 46
tinggi_badan = 175
usia = 21
nilai_akademis = 89
cek_cacat = False
cek_skill = "TIDAK ADA"

if cek_cacat == True:
    print("Maaf kamu tidak lulus karena cacat.")
       
elif ((jenis_kelamin == "laki-laki" or jenis_kelamin == "perempuan") and (cek_skill == "Menembak" or cek_skill == "Memanah" or cek_skill == "Berkuda")):
    print(f"Kamu lolos dengan jenis kelamin {jenis_kelamin}, karena kamu memiliki skill {cek_skill}.")
    
elif (jenis_kelamin == "perempuan" and (berat_badan >= 45 or berat_badan <= 50) and tinggi_badan >= 165 and (usia >= 15 or usia <= 20)):
    print(f"Kamu lulus, dengan jenis kelamin {jenis_kelamin}, berat badan {berat_badan}, dan tingginya {tinggi_badan} dan usianya {usia} tahun.")

elif ((jenis_kelamin == "laki-laki" or jenis_kelamin == "perempuan") and berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25):
    print(f"Kamu lulus, dengan jenis kelamin {jenis_kelamin}, berat badan {berat_badan} dan tinggIi {tinggi_badan} dan usianya {usia} tahun .")

elif ((jenis_kelamin == "laki-laki" or jenis_kelamin == "perempuan") and nilai_akademis >= 90 and usia <= 30):
    print(f"Kamu lulus, dengan jenis kelamin {jenis_kelamin}, karna nilai rata-rata akademis kamu {nilai_akademis} dan usia {usia} tahun.")
     
else:
    print("Maaf kamu tidak lolos")

    
    
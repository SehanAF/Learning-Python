# Buatlah program untuk menghitung kelayakan orang lulus organisasi X. Organisasi X memiliki kriteria untuk Anggota
# 1. Perempuan dengan berat badan minimal 45kilo gram, maks 50 kilogram dan Tingginya minimal 165 cm dan Usianya kurang dari 20 tahun
# 2. Laki-laki dengan berat badan maks 70 kilo dan Tingginya minimal 170 cm dan usianya maks 25 tahun
# 3. Laki-laki dan Perempuan dengan nilai rata-rata Akademis 90 dan usianya kurang dari 30 tahun
# 4. Laki-laki dan Perempuan yang Memiliki Skill Menembak, Memanah atau Berkuda

# Ke 4 Kriteria diatas akan diterima hanya dan hanya jika tidak memiliki anggota tubuh yang cacat.

# Buatlah Program Questioner untuk mengakomodasi kasus diatas.

cek_cacat = input("Apakah ada cacat? (ya/tidak): ").lower()

if cek_cacat == "ya":
    print("Maaf kamu tidak lulus karena cacat.")
    exit()

jenis_kelamin = input("Masukkan Jenis Kelamin (Laki-laki/Perempuan): ").lower()
berat_badan = int(input("Masukkan Berat Badan: "))
tinggi_badan = int(input("Masukan Tinggi Badan: "))
usia = int(input("Masukkan Usia: "))
nilai_akademis = int(input("Masukkan Nilai Akademis: "))
cek_skill = input("Masukkan Skill: ").split()


if any(skill in cek_skill for skill in ["Menembak", "Memanah", "Berkuda"]):
    print(f"Kamu lolos Syarat no 4 dengan jenis kelamin {jenis_kelamin}, karena kamu memiliki skill {cek_skill}.")
elif nilai_akademis >= 90 and usia <= 30:
    print(f"Kamu lulus Syarat nomor 3 dengan jenis kelamin {jenis_kelamin}, karena nilai rata-rata akademismu {nilai_akademis} dan usia {usia} tahun.")
elif jenis_kelamin == "perempuan" and 45 <= berat_badan <= 50 and tinggi_badan >= 165 and 15 <= usia <= 20:
    print(f"Kamu lulus Syarat nomor 1 yaitu dengan jenis kelamin {jenis_kelamin}, berat badan {berat_badan}, tingginya {tinggi_badan}, dan usianya {usia} tahun.")
elif jenis_kelamin == "laki-laki" and berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25:
    print(f"Kamu lulus Syarat nomor 2, dengan jenis kelamin {jenis_kelamin}, berat badan {berat_badan}, tingginya {tinggi_badan}, dan usianya {usia} tahun.")
else:
    print("Maaf kamu tidak lolos karena tidak memenuhi beberapa syarat.")
    
    
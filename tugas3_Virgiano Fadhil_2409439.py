# Nama: Virgiano Fadhil
# NIM: 2409439
# Kelas: 1B

import math

def selisih_waktu(jam_awal, menit_awal, detik_awal, jam_akhir, menit_akhir, detik_akhir):
    if jam_awal >= 24 or jam_akhir >= 24 or menit_awal >= 60 or menit_akhir >= 60 or detik_awal >= 60 or detik_akhir >= 60:
        print("Waktu yang dimasukkan tidak valid")
        exit()

    waktu_awal_detik = (jam_awal * 3600) + (menit_awal * 60) + detik_awal
    waktu_akhir_detik = (jam_akhir * 3600) + (menit_akhir * 60) + detik_akhir

    selisih_total_detik = waktu_akhir_detik - waktu_awal_detik

    hasil_jam = math.floor(selisih_total_detik / 3600)
    hasil_menit = math.floor((selisih_total_detik - (hasil_jam * 3600)) / 60)
    hasil_detik = selisih_total_detik - (hasil_jam * 3600) - (hasil_menit * 60)
    
    return hasil_jam, hasil_menit, hasil_detik



print("Waktu awal:")
jam_awal = int(input("Jam: "))
menit_awal = int(input("Menit: "))
detik_awal = int(input("Detik: "))

print("Waktu akhir:")
jam_akhir = int(input("Jam: "))
menit_akhir = int(input("Menit: "))
detik_akhir = int(input("Detik: "))

selisih_jam, selisih_menit, selisih_detik = selisih_waktu(jam_awal, menit_awal, detik_awal, jam_akhir, menit_akhir, detik_akhir)
print(f"{selisih_jam} jam - {selisih_menit} menit - {selisih_detik} detik")
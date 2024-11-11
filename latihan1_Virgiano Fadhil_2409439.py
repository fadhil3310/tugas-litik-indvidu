# Nama: Virgiano Fadhil
# NIM: 2409439
# Kelas: 1B

import math

def hitung_volume_tabung(jari_jari, tinggi):
    return math.pi * math.pow(jari_jari, 2) * tinggi

input_jari_jari = int(input("Jari-jari: "))
input_tinggi = int(input("Tinggi: "))

print(f"{hitung_volume_tabung(input_jari_jari, input_tinggi)}")
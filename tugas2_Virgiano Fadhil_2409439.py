# Nama: Virgiano Fadhil
# NIM: 2409439
# Kelas: 1B

def login(username, password):
    return username == "dudul" and password == "Latihan"

try_count = 0
while try_count < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if (login(username, password)):
        print("Berhasil login!")
        break
    else:
        print("Salah username atau password\n")
        try_count += 1

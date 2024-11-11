# Nama: Virgiano Fadhil
# NIM: 2409439
# Kelas: 1B

def login(password):
    return password == "Latihan"

try_count = 0
while try_count < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if (login(password)):
        print("Berhasil login!")
        break
    else:
        print("Salah username atau password\n")
        try_count += 1

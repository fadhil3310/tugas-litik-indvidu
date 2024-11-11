# Nama: Virgiano Fadhil
# NIM: 2409439
# Kelas: 1B

def fibonacci(a, b, i, max):
    if i >= max: 
        return
    result = 1 if i <= 1 else a + b
    print(result)
    fibonacci(b, result, i + 1, max)

jumlah = int(input("Masukkan jumlah fibonacci: "))
fibonacci(0, 1, 0, jumlah)
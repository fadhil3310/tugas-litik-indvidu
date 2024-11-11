# Nama: Virgiano Fadhil
# NIM: 2409439
# Kelas: 1B

def total_rata_rata(*angka):
    iteration_step = ""
    hasil = 0
    first_time = True
    for a in angka:
        iteration_step += (" + " if first_time == False else "") + str(a)
        hasil += a
        first_time = False

    return iteration_step, hasil, hasil / len(angka), len(angka)

input_angka = []
while True:
    input_angka.append(int(input("Input angka: ")))
    if input("Selesai? (ya/tidak): ") == "ya":
        break

iteration_step, total, rata_rata, length = total_rata_rata(*input_angka)
print(f"\nTotal: {iteration_step} = {total}")
print(f"Rata-rata: = {total} / {length} = {rata_rata}")

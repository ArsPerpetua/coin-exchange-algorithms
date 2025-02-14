import time


def menu():
    print(
        """
Pilih Algoritma
1. Tukar Rupiah ke Koin dengan Metode Brute Force
2. Tukar Rupiah ke Koin dengan Algoritma Greedy
0. Keluar
"""
    )


def hapus_duplikat(kombinasi):
    terfilter = set()
    for combo in kombinasi:
        combo.sort()
        terfilter.add(tuple(combo))
    return [list(i) for i in terfilter]


def tukar_koin(jumlah):
    if jumlah == 0:
        return [[]]  # satu-satunya kombinasi yang mungkin adalah tanpa koin
    if jumlah < 0:
        return []  # tidak ada kombinasi yang mungkin
    else:
        semua_kombinasi = []
        for nilai in koin:
            hasil_rekursif = tukar_koin(jumlah - nilai)
            for kombinasi in hasil_rekursif:
                kombinasi.append(nilai)
                semua_kombinasi.append(
                    kombinasi
                )  # Tambahkan kombinasi ke semua_kombinasi
        return semua_kombinasi


def algoritma_greedy(tukar):
    jmlh7, jmlh5, jmlh3, jmlh1 = 0, 0, 0, 0
    while tukar != 0:
        if tukar >= 1000:
            tukar -= 1000
            jmlh7 += 1
        elif tukar >= 500:
            tukar -= 500
            jmlh5 += 1
        elif tukar >= 200:
            tukar -= 200
            jmlh3 += 1
        else:
            tukar -= 100
            jmlh1 += 1
    print(" Jumlah koin 1000 :", jmlh7)
    print(" Jumlah koin 500 :", jmlh5)
    print(" Jumlah koin 200 :", jmlh3)
    print(" Jumlah koin 100 :", jmlh1)


def cetak_animasi():
    for _ in range(3):
        print(".", end=" ", flush=True)
        time.sleep(0.5)


def cetak_pemisah():
    print("\n" + "=" * 40 + "\n")


if __name__ == "__main__":
    koin = [100, 200, 500, 1000]
    cetak_pemisah()
    print("Selamat datang di Program Tukar Koin!")
    cetak_pemisah()
    st_jumlah = input("Masukkan nominal Rupiah untuk ditukarkan ke koin: ")
    jumlah = int(st_jumlah)

    while True:
        menu()
        pilihan = input("Masukkan pilihan Anda: ")
        if pilihan == "0":
            cetak_pemisah()
            print("Terima kasih telah menggunakan program ini!")
            cetak_pemisah()
            break
        elif pilihan == "1":
            cetak_pemisah()
            print("Anda memilih Metode Brute Force.")
            print("Menghitung kombinasi koin...")
            cetak_animasi()
            mulai = time.perf_counter()
            kombinasi_koin = tukar_koin(jumlah)
            kombinasi_optimal = min(kombinasi_koin, key=len) if kombinasi_koin else []
            print("\nKombinasi koin minimum: ", kombinasi_optimal)
            print("Jumlah koin optimal: ", len(kombinasi_optimal))
            selesai = time.perf_counter()
            print("Waktu eksekusi: ", selesai - mulai, "detik")
            cetak_pemisah()
        elif pilihan == "2":
            cetak_pemisah()
            print("Anda memilih Algoritma Greedy.")
            print("Menghitung koin menggunakan algoritma Greedy...")
            cetak_animasi()
            mulai = time.perf_counter()
            algoritma_greedy(jumlah)
            selesai = time.perf_counter()
            print("Waktu eksekusi: ", selesai - mulai, "detik")
            cetak_pemisah()
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

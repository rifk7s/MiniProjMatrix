import os

while True:
    while True:  # Loop ini untuk memperbaiki kesalahan input dari pengguna
        print('Seberapa besar matriks yang Anda inginkan? (<=4) ')
        c = input('Pilihan Anda: ')
        try:
            ch = int(c)  # Mengubah input ke integer agar pengguna tidak memasukkan kata
            if ch in [2, 3, 4]: 
                break  # Jika input pengguna valid, keluar dari loop
            else:
                print('Pilihan tidak valid')
        except ValueError:
            print('Pilihan tidak valid')  # Jika input menghasilkan error, akan kembali ke loop
        if ch == 1 and ch > 5:
            print("Tidak valid")

    def input_matrix(rows, cols, name):
        print(f"Masukkan elemen matriks {name} baris per baris (n n n):")
        matrix = []
        for i in range(rows):
            row = list(map(int, input(f"Baris {i + 1}: ").split()))
            if len(row) != cols:
                print(f"Harap masukkan tepat {cols} angka untuk baris ini (n n n).")
                return input_matrix(rows, cols, name)
            matrix.append(row)
        return matrix

    # Dimensi matriks
    rows = cols = ch

    # Input matriks
    X = input_matrix(rows, cols, "X")
    Y = input_matrix(rows, cols, "Y")

    # Inisialisasi matriks hasil
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Penjumlahan matriks
    for i in range(rows):
        for j in range(cols):
            result[i][j] = X[i][j] * Y[i][j]

    # Menampilkan hasil
    print("\nMatriks Hasil:")
    for r in result:
        print(r)

    while True:
        print('Lagi?\n1. Ya\n2. Tidak')
        ag = input('Pilihan Anda: ')
        try:
            ag = int(ag)  # Mengubah input ke integer
            if ag == 1:
                continue
                # 
                
                break
            elif ag == 2:
                break  # Keluar dari program
            else:
                print('Pilihan tidak valid, pilih 1 atau 2.')  # Menangani input yang di luar pilihan
        except ValueError:
            print('Input tidak valid. Harap masukkan angka (1 atau 2).')  # Menangani input bukan angka

    # Mengarahkan kembali ke pemilihan operasi atau langsung keluar
    while True:
        print('Kembali ke layar pemilihan operasi?\n1. Ya\n2. Tidak')
        opr = input('Pilihan Anda: ')
        try:
            opr = int(opr)  # Mengubah input ke integer
            if opr == 1:
                os.system("py ../MINIPROJMATRIX/matrix_app.py")
                break
            elif opr == 2:
                exit(0)  # Keluar dari program
            else:
                print('Pilihan tidak valid, pilih 1 atau 2.')  # Menangani input yang di luar pilihan
        except ValueError:
            print('Input tidak valid. Harap masukkan angka (1 atau 2).')  # Menangani input bukan angka

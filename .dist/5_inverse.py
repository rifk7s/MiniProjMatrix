import os

while True:
    while True:  # loop untuk menangani kesalahan input
        print('Seberapa besar matriks yang Anda inginkan? (<=4) ')
        c = input('Pilihan Anda: ')
        try:
            ch = int(c)  # ubah input ke tipe int agar tidak menerima huruf
            if ch in [2, 3, 4]:
                break  # jika input user sesuai pilihan, keluar dari loop
            else:
                print('Pilihan tidak valid')
        except ValueError:
            print('Pilihan tidak valid')  # jika input user menghasilkan error, akan terus mengulang
        if ch == 1 and ch > 5:
            print("Pilihan tidak valid")

    def input_matrix(rows, cols, name):
        print(f"Masukkan elemen-elemen matriks {name} baris per baris (contoh: n n n):")
        matrix = []
        for i in range(rows):
            row = list(map(int, input(f"Baris {i + 1}: ").split()))
            if len(row) != cols:
                print(f"Harap masukkan tepat {cols} angka untuk baris ini (contoh: n n n).")
                return input_matrix(rows, cols, name)
            matrix.append(row)
        return matrix

    # Fungsi untuk mencari determinan sebuah matriks.
    def getDet(mat, n):

        # Kasus dasar: jika matriks berukuran 1x1
        if n == 1:
            return mat[0][0]

        # Kasus dasar untuk matriks 2x2
        if n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        # Kasus rekursif untuk matriks yang lebih besar
        res = 0
        for col in range(n):

            # Buat submatriks dengan menghapus baris pertama 
            # dan kolom saat ini
            sub = [[0] * (n - 1) for _ in range(n - 1)]
            for i in range(1, n):
                subcol = 0
                for j in range(n):

                    # Lewati kolom saat ini
                    if j == col:
                        continue

                    # Isi submatriks
                    sub[i - 1][subcol] = mat[i][j]
                    subcol += 1

            # Ekspansi kofaktor
            sign = 1 if col % 2 == 0 else -1
            res += sign * mat[0][col] * getDet(sub, n - 1)

        return res

    # Fungsi untuk menemukan matriks kofaktor
    def getCofactor(mat, n):
        cofactor = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                sub = [[mat[row][col] for col in range(n) if col != j] for row in range(n) if row != i]
                sign = 1 if (i + j) % 2 == 0 else -1
                cofactor[i][j] = sign * getDet(sub, n - 1)
        return cofactor

    # Fungsi untuk mentranspos matriks
    def transpose(mat, n):
        return [[mat[j][i] for j in range(n)] for i in range(n)]

    # Fungsi untuk menemukan invers matriks
    def getInverse(mat, n):
        det = getDet(mat, n)
        if det == 0:
            return None  # Invers tidak ada
        cofactor = getCofactor(mat, n)
        adjoint = transpose(cofactor, n)
        inverse = [[adjoint[i][j] / det for j in range(n)] for i in range(n)]
        return inverse

    # Program utama
    print("Kalkulator Invers Matriks")
    rows = cols = ch  # Sesuaikan ukuran matriks persegi sesuai kebutuhan
    matrix = input_matrix(rows, cols, "A")

    inverse = getInverse(matrix, rows)

    if inverse is None:
        print("\nInvers tidak ada (determinan = 0).")
    else:
        print("\nInvers dari matriks adalah:")
        for row in inverse:
            print(" ".join(f"{val:.2f}" for val in row))

    while True:
        print('Lagi?\n1. Ya\n2. Tidak')
        ag = input('Pilihan Anda: ')
        try:
            ag = int(ag)  # Ubah ke integer
            if ag == 1:
                continue
                break
            elif ag == 2:
                break  # Keluar dari program
            else:
                print('Pilihan tidak valid, harap pilih 1 atau 2.')  # Tangani input di luar jangkauan
        except ValueError:
            print('Input tidak valid. Harap masukkan angka (1 atau 2).')  # Tangani input bukan angka

    # Kembali ke pilihan operasi atau keluar program
    while True:
        print('Kembali ke layar pemilihan operasi?\n1. Ya\n2. Tidak')
        opr = input('Pilihan Anda: ')
        try:
            opr = int(opr)  # Ubah ke integer
            if opr == 1:
                os.system("py ../MINIPROJMATRIX/matrix_app.py")

                break
            elif opr == 2:
                exit(0)  # Keluar dari program
            else:
                print('Pilihan tidak valid, harap pilih 1 atau 2.')  # Tangani input di luar jangkauan
        except ValueError:
            print('Input tidak valid. Harap masukkan angka (1 atau 2).')  # Tangani input bukan angka  


            
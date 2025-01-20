import os

while True:
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
            return mat[0][0] * mat[1][1] - \
                mat[0][1] * mat[1][0]
        
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

    # Ukuran matriks (matriks persegi)
    size = 3  # Contoh: Untuk matriks 3x3

    # Input matriks
    matrix = input_matrix(size, size, "A")

    # Hitung determinan
    determinant = getDet(matrix, size)

    # Cetak hasil
    print(f"Determinan matriks adalah: {determinant}")

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
import os 

while True:
    while True:  # Loop ini untuk memastikan input yang diberikan valid
        print('Seberapa besar matriks yang Anda inginkan? (<=4) ')
        c = input('Pilihan Anda: ')
        try:
            ch = int(c)  # Ubah input ke tipe integer agar tidak menerima huruf
            if ch in [2, 3, 4]: 
                break  # Jika input user sesuai pilihan, keluar dari loop
            else:
                print('Pilihan tidak valid')
        except ValueError:
            print('Pilihan tidak valid')  # Jika input user menghasilkan error, akan terus mengulang 
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

    # Ukuran matriks
    rows = cols = ch

    # Input matriks
    X = input_matrix(rows, cols, "X")
    Y = input_matrix(rows, cols, "Y")

    # Inisialisasi matriks hasil
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Mengurangi matriks
    for i in range(rows):
        for j in range(cols):
            result[i][j] = X[i][j] - Y[i][j]

    # Cetak hasil
    print("\nMatriks Hasil:")
    for r in result:
        print(r)

        while True:
            print('Lagi?\n1. Ya\n2. Tidak')
            ag = input('Pilihan Anda: ')
            try:
                ag = int(ag)  # Ubah ke tipe integer
                if ag == 1:
                    continue
                    break
                elif ag == 2:
                    break  # Keluar dari program
                else:
                    print('Pilihan tidak valid, harap pilih 1 atau 2.')  # Tangani input di luar jangkauan
            except ValueError:
                print('Input tidak valid. Harap masukkan angka (1 atau 2).')  # Tangani input bukan angka

    # Kembali ke pemilihan operasi atau keluar dari program
        while True:
            print('Kembali ke layar pemilihan operasi?\n1. Ya\n2. Tidak')
            opr = input('Pilihan Anda: ')
            try:
                opr = int(opr)  # Ubah ke tipe integer
                if opr == 1:
                    os.system("py ../MINIPROJMATRIX/matrix_app.py")
                    break
                elif opr == 2:
                    exit(0)  # Keluar dari program
                else:
                    print('Pilihan tidak valid, harap pilih 1 atau 2.')  # Tangani input di luar jangkauan
            except ValueError:
                print('Input tidak valid. Harap masukkan angka (1 atau 2).')  # Tangani input bukan angka
  
  
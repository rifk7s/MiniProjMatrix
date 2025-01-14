def input_matriks(baris, kolom, nama):
    print(f"Masukkan elemen matriks {nama} baris demi baris (contoh: n n n):")
    matriks = []
    for i in range(baris):
        baris_data = list(map(int, input(f"Baris {i + 1}: ").split()))
        if len(baris_data) != kolom:
            print(f"Masukkan tepat {kolom} angka untuk baris ini (contoh: n n n).")
            return input_matriks(baris, kolom, nama)
        matriks.append(baris_data)
    return matriks

# Dimensi matriks
baris = 3
kolom = 3

# Input matriks
X = input_matriks(baris, kolom, "X")
Y = input_matriks(baris, kolom, "Y")

# Inisialisasi matriks hasil
hasil = [[0 for _ in range(kolom)] for _ in range(baris)]

# Penjumlahan matriks
for i in range(baris):
    for j in range(kolom):
        hasil[i][j] = X[i][j] + Y[i][j]

# Cetak hasil
print("\nMatriks Hasil:")
for r in hasil:
    print(r)
 
 
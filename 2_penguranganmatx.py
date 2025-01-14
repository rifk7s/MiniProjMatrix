def input_matriks(baris, kolom, nama):
    print(f"Masukkan elemen-elemen matriks {nama} baris per baris (n n n):")
    matriks = []
    for i in range(baris):
        baris_input = list(map(int, input(f"Baris {i + 1}: ").split()))
        if len(baris_input) != kolom:
            print(f"Harap masukkan tepat {kolom} angka untuk baris ini (n n n).")
            return input_matriks(baris, kolom, nama)
        matriks.append(baris_input)
    return matriks

# Dimensi matriks
baris = 3
kolom = 3

# Masukkan matriks
X = input_matriks(baris, kolom, "X")
Y = input_matriks(baris, kolom, "Y")

# Inisialisasi matriks hasil
hasil = [[0 for _ in range(kolom)] for _ in range(baris)]

# Kurangkan matriks
for i in range(baris):
    for j in range(kolom):
        hasil[i][j] = X[i][j] - Y[i][j]

# Cetak hasil
print("\nMatriks Hasil:")
for r in hasil:
    print(r) 
    
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

# Fungsi untuk mencari determinan matriks.
def getDet(matriks, n):
  
    # Kasus dasar: jika matriks 1x1
    if n == 1:
        return matriks[0][0]
    
    # Kasus dasar untuk matriks 2x2
    if n == 2:
        return matriks[0][0] * matriks[1][1] - \
               matriks[0][1] * matriks[1][0]
    
    # Kasus rekursif untuk matriks yang lebih besar
    hasil = 0
    for kolom in range(n):
      
        # Membuat submatriks dengan menghapus baris pertama 
        # dan kolom yang sedang diproses
        sub = [[0] * (n - 1) for _ in range(n - 1)]
        for i in range(1, n):
            subkolom = 0
            for j in range(n):
              
                # Lewati kolom yang sedang diproses
                if j == kolom:
                    continue
                
                # Isi submatriks
                sub[i - 1][subkolom] = matriks[i][j]
                subkolom += 1
        
        # Ekspansi kofaktor
        tanda = 1 if kolom % 2 == 0 else -1
        hasil += tanda * matriks[0][kolom] * getDet(sub, n - 1)
    
    return hasil


# Fungsi untuk mencari matriks kofaktor
def getKofaktor(matriks, n):
    kofaktor = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sub = [[matriks[row][col] for col in range(n) if col != j] for row in range(n) if row != i]
            tanda = 1 if (i + j) % 2 == 0 else -1
            kofaktor[i][j] = tanda * getDet(sub, n - 1)
    return kofaktor

# Fungsi untuk mentranspos matriks
def transpose(matriks, n):
    return [[matriks[j][i] for j in range(n)] for i in range(n)]

# Fungsi untuk mencari invers matriks
def getInvers(matriks, n):
    det = getDet(matriks, n)
    if det == 0:
        return None  # Invers tidak ada
    kofaktor = getKofaktor(matriks, n)
    adjoint = transpose(kofaktor, n)
    invers = [[adjoint[i][j] / det for j in range(n)] for i in range(n)]
    return invers

# Program utama
print("Kalkulator Invers Matriks")
baris = kolom = 3  # Sesuaikan ukuran matriks persegi sesuai kebutuhan
matriks = input_matriks(baris, kolom, "A")

invers = getInvers(matriks, baris)

if invers is None:
    print("\nInvers tidak ada (determinannya 0).")
else:
    print("\nInvers matriksnya adalah:")
    for baris in invers:
        print(" ".join(f"{val:.2f}" for val in baris))

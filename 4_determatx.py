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

# Ukuran matriks (matriks persegi)
ukuran = 3  # Contoh: Untuk matriks 3x3

# Masukkan matriks
matriks = input_matriks(ukuran, ukuran, "A")

# Hitung determinan
determinant = getDet(matriks, ukuran)

# Cetak hasil
print(f"Determinan matriks tersebut adalah: {determinant}") 


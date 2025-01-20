import os

while True:
    # Loop untuk memastikan input operasi matriks valid
    print('Apa operasi matriks yang Anda inginkan?\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Determinan\n5. Invers')
    c = input('Pilihan Anda: ')
    try:
        ch = int(c)  # Ubah input ke tipe integer
        if ch in [1, 2, 3, 4, 5]:
            break  # Jika input sesuai pilihan, keluar dari loop
        else:
            print('Pilihan tidak valid. Masukkan angka antara 1 hingga 5.')
    except ValueError:
        print('Pilihan tidak valid. Harap masukkan angka (1, 2, 3, 4, atau 5).')

# Menjalankan file Python sesuai pilihan pengguna
if ch == 1:
    os.system("py .dist/1_penjumlahan.py")
elif ch == 2:
    os.system("py .dist/2_pengurangan.py")
elif ch == 3:
    os.system("py .dist/3_perkalian.py")
elif ch == 4:
    os.system("py .dist/4_determinan.py")
else:
    os.system("py .dist/5_inverse.py")

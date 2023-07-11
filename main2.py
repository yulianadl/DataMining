import numpy as np

# Data tabel
data = np.array([
    ["excellent", 80, "B"],
    ["fair", 50, "D"],
    ["good", 90, "A"],
    ["excellent", 75, "B"],
    ["fair", 82, "B"],
    ["good", 65, "C"]
])

# Mengubah data keaktifan menjadi atribut ordinal
ordinal_data = {
    "fair": 1,
    "good": 2,
    "excellent": 3
}

def min_max_ordinal(baris, kolom):
    return (ordinal_data[data[baris][kolom]] - 1) / (3-1)

def min_max_numeric(baris, kolom):
    return (int(data[baris][kolom]) - 50) / (90-50)

# Matriks dissimilarity campuran
hasil_matrix_nominal    = np.zeros((len(data), len(data)))
hasil_matrix_ordinal    = np.zeros((len(data), len(data)))
hasil_matrix_numerik    = np.zeros((len(data), len(data)))
hasil_matrix_campuran   = np.zeros((len(data), len(data)))

# Menghitung dissimilarity untuk setiap pasangan data
for i in range(len(data)):
    for j in range(len(data)):
        # Menghitung dissimilarity untuk atribut Indeks (nominal)
        hasil_matrix_nominal[i][j] = 0 if data[i][2] == data[j][2] else 1

        # Menghitung dissimilarity untuk atribut keaktifan (ordinal)
        hasil_matrix_ordinal[i][j] = abs(min_max_ordinal(i, 0) - min_max_ordinal(j, 0))

        # Menghitung dissimilarity untuk atribut nilai UAS (numerik)
        hasil_matrix_numerik[i][j] = abs(min_max_numeric(i, 1) - min_max_numeric(j, 1))

        # Menggabungkan dissimilarity dari ketiga atribut menggunakan Euclidean distance
        dissimilarity = (hasil_matrix_nominal[i][j]+hasil_matrix_ordinal[i][j]+hasil_matrix_numerik[i][j])/3

        # Membulatkan nilai dissimilarity menjadi dua digit desimal
        hasil_matrix_campuran[i][j] = (round(dissimilarity, 3))

# Cetak Hasil
print('-- Hasil Matriks Nominal --')
print(hasil_matrix_nominal)
print('\n')
print('-- Hasil Matriks Ordinal --')
print(hasil_matrix_ordinal)
print('\n')
print('-- Hasil Matriks Numerik --')
print(hasil_matrix_numerik)
print('\n')
print('-- Hasil Matriks Campuran --')
print(hasil_matrix_campuran)
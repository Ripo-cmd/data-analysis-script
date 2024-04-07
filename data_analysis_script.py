# Import library yang diperlukan
import numpy as np  # numpy untuk operasi numerik
import pandas as pd  # pandas untuk manipulasi data
import matplotlib.pyplot as plt  # matplotlib untuk visualisasi

# Generate dataset kategorikal
data_kategorikal = ['Kategori_A', 'Kategori_B', 'Kategori_C', 'Kategori_D', 'Kategori_E',
                    'Kategori_F', 'Kategori_G', 'Kategori_H', 'Kategori_I', 'Kategori_J',
                    'Kategori_K', 'Kategori_L', 'Kategori_M', 'Kategori_N', 'Kategori_O',
                    'Kategori_P', 'Kategori_Q', 'Kategori_R', 'Kategori_S', 'Kategori_T', 'Kategori_U']

# Generate dataset numerikal (menghasilkan bilangan bulat acak antara 1 dan 100)
data_numerikal = np.random.randint(1, 100, size=21)

# Konversi data numerikal ke DataFrame
df_numerikal = pd.DataFrame(data_numerikal, columns=['Numerikal'])

# Konversi data kategorikal ke DataFrame
df_kategorikal = pd.DataFrame(data_kategorikal, columns=['Kategorikal'])

# Menghitung Measures of Central Tendency
tendency_numerikal = {
    'Mean': np.mean(data_numerikal),
    'Median': np.median(data_numerikal),
    'Mode': int(pd.Series(data_numerikal).mode())  # Mode mengembalikan Series, diubah ke int
}
tendency_kategorikal = {
    'Mode': df_kategorikal['Kategorikal'].mode()[0]  # Mode untuk data kategorikal
}

# Menghitung Measures of Variability
variability_numerikal = {
    'Variansi': np.var(data_numerikal),
    'Standar Deviasi': np.std(data_numerikal),
    'Rentang': np.ptp(data_numerikal),
    'Jangkauan Interkuartil (IQR)': np.percentile(data_numerikal, 75) - np.percentile(data_numerikal, 25)
}

# Summary of Descriptive Statistics
summary_numerikal = df_numerikal.describe()
summary_kategorikal = df_kategorikal.describe()

# Visualisasi Data
# Box plot untuk data numerikal
plt.figure(figsize=(8, 6))
plt.boxplot(data_numerikal)
plt.title('Box plot Data Numerikal')
plt.xlabel('Data Numerikal')
plt.ylabel('Nilai')
plt.show()

# Histogram untuk data numerikal
plt.figure(figsize=(8, 6))
plt.hist(data_numerikal, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram Data Numerikal')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.show()

# Pie chart untuk data kategorikal
plt.figure(figsize=(8, 8))
summary_kategorikal['Kategorikal'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie chart Data Kategorikal')
plt.show()

# Bar chart untuk data kategorikal
plt.figure(figsize=(10, 6))
summary_kategorikal['Kategorikal'].value_counts().plot(kind='bar', color='salmon')
plt.title('Bar chart Data Kategorikal')
plt.xlabel('Kategori')
plt.ylabel('Frekuensi')
plt.xticks(rotation=45)
plt.show()

# Generate dataset numerikal kedua
data_numerikal2 = np.random.randint(1, 100, size=21)
df_numerikal2 = pd.DataFrame(data_numerikal2, columns=['Numerikal2'])

# Urutkan kedua dataset numerikal
data_numerikal_urut_asc = np.sort(data_numerikal)
data_numerikal_urut_desc = np.sort(data_numerikal)[::-1]
data_numerikal2_urut_asc = np.sort(data_numerikal2)
data_numerikal2_urut_desc = np.sort(data_numerikal2)[::-1]

# Hitung Korelasi antara pasangan data
korelasi = np.corrcoef(data_numerikal, data_numerikal2)

# Visualisasi data menggunakan X-Y plots
plt.figure(figsize=(8, 6))
plt.scatter(data_numerikal, data_numerikal2)
plt.title('X-Y plot Data Numerikal')
plt.xlabel('Data Numerikal 1')
plt.ylabel('Data Numerikal 2')
plt.show()

# Heatmap untuk korelasi antara pasangan data
plt.figure(figsize=(6, 4))
plt.imshow(korelasi, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap Korelasi')
plt.show()

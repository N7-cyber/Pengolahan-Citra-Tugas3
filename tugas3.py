import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. BACA GAMBAR (ASET TUGAS 2)
# ==========================================
image_path = 'Jake.jpg'
# Langsung baca dalam format Grayscale karena materi keabuan
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Gambar '{image_path}' tidak ditemukan di folder ini.")
    exit()

# Ubah ke float32 agar perhitungan matematika (pangkat/logaritma) lebih presisi
img_float = img.astype(np.float32)
L = 256 # Jumlah level keabuan (8-bit)

# ==========================================
# 2. PROSES 4 JENIS TRANSFORMASI (TUGAS 3)
# ==========================================

# A. Transformasi Negative: G = L - 1 - F
negative_img = (L - 1) - img

# B. Transformasi Logaritmik: G = c * log(F + 1)
c_log = 255 / np.log1p(np.max(img_float)) # Hitung c otomatis agar pas
log_img = np.clip(c_log * np.log1p(img_float), 0, 255).astype(np.uint8)

# C. Transformasi Inverse Logaritmik (Menggunakan c=50 dari eksperimenmu)
c_inv = 50
inv_log_img = np.clip(c_inv * np.log1p((L - 1) - img_float), 0, 255).astype(np.uint8)

# D. Transformasi Power-Law / n-th power (Menggunakan y=0.7, c=1.5 dari eksperimenmu)
gamma = 0.7
c_power = 1.5
power_img = np.clip(c_power * np.power(img_float, gamma), 0, 255).astype(np.uint8)


# ==========================================
# 3. TAMPILKAN HASIL DENGAN MATPLOTLIB
# ==========================================
# Siapkan list judul dan gambar untuk di-looping
titles = [
    "Citra Asal (Grayscale)", 
    "1. Negative Image", 
    "2. Transformasi Logaritmik", 
    "3. Inverse Log (c=50)", 
    "4. Power-Law (y=0.7, c=1.5)"
]
images = [img, negative_img, log_img, inv_log_img, power_img]

# Buat canvas figure
plt.figure(figsize=(15, 8))
plt.suptitle("Hasil Tugas Pengolahan Citra: Transformasi Tingkat Keabuan", fontsize=16, fontweight='bold', y=0.95)

# Looping untuk menampilkan 5 gambar (kita susun dalam 2 baris, 3 kolom)
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.title(titles[i], fontsize=11, pad=10)
    plt.axis('off')

plt.tight_layout(pad=2.0)
plt.show() # Gambar akan muncul di window baru, siap di-screenshot!
# Tugas 3 Pengolahan Citra Digital: Transformasi Tingkat Keabuan
Repositori ini berisi implementasi kode Python untuk menyelesaikan Tugas 3 mata kuliah Pengolahan Citra Digital. Tugas ini berfokus pada **Transformasi Tingkat Keabuan (Gray Level Transformation)**, yaitu teknik pemrosesan citra yang bekerja pada wilayah spasial (piksel tunggal/titik tetangga) untuk memanipulasi kontras dan intensitas gambar.

📌 Deskripsi Tugas
Program ini membaca sebuah citra digital (warna), mengubahnya menjadi *Grayscale* (keabuan) sebagai matriks awal 
F(x,y), kemudian menerapkan empat (4) jenis fungsi transformasi untuk menghasilkan citra baru G(x,y), yaitu:

1. **Negative Image:** Mengubah citra menjadi bentuk negatifnya, di mana area gelap menjadi terang dan sebaliknya.
2. **Transformasi Logaritmik:** Menerangkan detail pada area gambar yang memiliki intensitas rendah (gelap).
3. **Transformasi Inverse Logaritmik:** Efek kebalikan dari logaritmik, yaitu menggelapkan area yang terang. Pada eksperimen ini menggunakan konstanta c=50.
4. **Transformasi Power-Law:** Manipulasi gambar menggunakan fungsi pangkat. Pada eksperimen ini diatur dengan nilai gamma y=0.7 dan c=1.5.

*Catatan: Objek gambar yang digunakan adalah aset dari tugas sebelumnya (Tugas 2: Sampling dan Kuantisasi) untuk melihat kelanjutan efek pemrosesan pada gambar yang sama.*

## ⚙️ Persyaratan Sistem (Dependencies)

Pastikan *library* Python berikut telah terinstal sebelum menjalankan kode:

* **OpenCV (`cv2`):** Untuk membaca, mengonversi (ke *Grayscale*), dan memproses matriks citra digital.
* **NumPy (`numpy`):** Untuk operasi komputasi matematis tingkat lanjut pada susunan array (piksel), seperti logaritma dan bilangan berpangkat.
* **Matplotlib (`matplotlib.pyplot`):** Untuk melakukan *plotting* dan menampilkan perbandingan visual kelima gambar (asli dan hasil transformasi) dalam satu bidang layar (*figure*).

Install:
pip install opencv-python numpy matplotlib

🚀 Cara Menjalankan Program
1. Pastikan file script tugas3.py dan aset gambar Jake.jpg berada di dalam satu folder direktori yang sama.
2. Buka terminal atau IDE pilihan Anda (seperti VS Code).
3. Arahkan terminal ke folder tempat file tersebut berada.
4. Eksekusi perintah berikut:
Nama file:
python tugas3.py
5. Akan muncul sebuah window Matplotlib baru yang menampilkan perbandingan Citra Asal dengan keempat hasil transformasinya.

📝 Kesimpulan Analisis
Dari eksperimen terhadap gambar Jake.jpg didapatkan bahwa:
1. Rumus matematis dapat secara instan mengubah distribusi cahaya/intensitas piksel.
2. Penggunaan tipe data float32 selama komputasi numerik sangat penting sebelum dikembalikan ke uint8, guna mencegah kebocoran presisi atau hilangnya nilai saat operasi logaritma/pangkat berjalan.


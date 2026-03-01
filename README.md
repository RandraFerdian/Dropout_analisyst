# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang memiliki visi untuk mencetak sumber daya manusia unggul dan berdaya saing. Namun, institusi menghadapi tantangan serius berupa tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout).

Fenomena dropout tidak hanya berdampak pada reputasi institusi, tetapi juga menunjukkan adanya hambatan sistemik yang dialami mahasiswa, baik dari sisi akademik maupun finansial. Oleh karena itu, diperlukan pendekatan berbasis data untuk mengidentifikasi risiko sejak dini dan membantu manajemen dalam mengambil keputusan strategis.

### Permasalahan Bisnis

- **Tingginya Angka Dropout**: Institusi kesulitan mengidentifikasi mahasiswa berisiko secara dini.
- **Intervensi yang Reaktif**: Penanganan sering dilakukan setelah mahasiswa tidak aktif, sehingga terlambat untuk dicegah.
- **Kurangnya Insight Strategis**: Belum tersedia alat visualisasi data yang mampu memantau performa mahasiswa secara real-time dan komprehensif.

### Cakupan Proyek

- **Analisis Data & Dashboarding**  
  Membangun dashboard bisnis menggunakan Google Looker Studio untuk pemantauan menyeluruh performa mahasiswa.

- **Pemodelan Predictive**  
  Mengembangkan model machine learning berbasis XGBoost untuk memprediksi risiko dropout mahasiswa.

- **Prototype Testing**  
  Membangun aplikasi berbasis Streamlit untuk menguji performa model terhadap data mahasiswa baru secara langsung.

### Persiapan

### Dataset Source

- **Source:** [Dicoding Dataset - Students Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)
- **Context:** Data used for predicting student dropout and academic success.

**Setup environment:**

```bash
# Untuk menjalankan Prototype Streamlit:
pip install -r requirements.txt
```

---

## Business Dashboard

Business dashboard dikembangkan menggunakan **Google Looker Studio** sebagai pusat informasi bagi manajemen Jaya Jaya Institut. Dashboard ini berfungsi untuk:

- **Monitoring Status**  
  Memantau perbandingan jumlah mahasiswa Graduate, Enrolled, dan Dropout secara visual.

- **Identifikasi Faktor Risiko**  
  Menampilkan hubungan antara status ekonomi (pembayaran SPP) dengan keberhasilan akademik mahasiswa.

- **Evaluasi Strategis**  
  Memberikan dasar pengambilan keputusan berbasis data bagi pimpinan untuk merancang program bantuan finansial maupun akademik.

* **Interactive Dashboard:** [Jaya Jaya Institut - Retention Analytics Dashboard](https://lookerstudio.google.com/reporting/840780fd-1bc0-4132-a066-61e39521f738)

---

## Menjalankan Sistem Machine Learning

Prototype dibuat menggunakan **Streamlit** untuk memungkinkan staf akademik melakukan pengujian prediksi risiko mahasiswa secara langsung.

### Langkah Menjalankan Prototype

1. Pastikan folder `models/` berisi file `model_student_dropout.pkl`.
2. Jalankan perintah berikut di terminal:

```bash
streamlit run app.py
```

3. Masukkan data pada tab yang tersedia (Data Pribadi, Akademik, Semester) untuk melakukan pengujian prediksi.

**Akses Prototype:**  
[Link Prototype Streamlit Kamu di Sini](https://siswadropout.streamlit.app/)

---

## Conclusion

Proyek ini menghasilkan solusi terintegrasi yang terdiri dari dua pendekatan utama:

1. **Pendekatan Strategis** melalui dashboard Looker Studio untuk pemantauan tingkat institusi.
2. **Pendekatan Taktis** melalui prototype Streamlit untuk pengujian risiko mahasiswa secara individual.

Model XGBoost yang diimplementasikan menunjukkan performa yang baik dengan skor **F1-Macro sebesar 0.7109**, sehingga dapat digunakan sebagai alat bantu pengambilan keputusan dalam mengidentifikasi mahasiswa berisiko dropout secara lebih dini dan akurat.

### Rekomendasi Action Items

- **Program Bantuan SPP**  
  Memberikan peringatan dini dan bantuan finansial kepada mahasiswa yang menunggak biaya kuliah.

- **Early Warning System**  
  Mengintegrasikan model ke dalam sistem akademik untuk melakukan pengecekan risiko mahasiswa secara berkala setiap semester.

- **Evaluasi Kurikulum dan Akademik**  
  Meninjau kembali program studi atau mata kuliah dengan tingkat kegagalan tertinggi berdasarkan hasil analisis dashboard.

- **Pendampingan Akademik Terstruktur**  
  Menyediakan program mentoring atau bimbingan belajar khusus bagi mahasiswa dengan performa akademik rendah.

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institute

## Business Understanding
Jaya Jaya Institute adalah sebuah perusahaan yang bergerak di bidang pendidikan (Edutech). Sebagai institusi pendidikan, salah satu tantangan utama yang dihadapi adalah memastikan keberhasilan akademis mahasiswa. Keberhasilan ini diukur, salah satunya, dari tingkat kelulusan dan upaya meminimalkan angka *dropout*. Tingginya angka *dropout* tidak hanya berdampak negatif pada reputasi institusi, tetapi juga mempengaruhi efisiensi operasional dan potensi pendapatan. Oleh karena itu, Jaya Jaya Institute berinisiatif untuk memahami faktor-faktor yang mempengaruhi performa akademis mahasiswa dan mengembangkan strategi proaktif guna meningkatkan tingkat kelulusan serta mengurangi angka *dropout*.

### Permasalahan Bisnis
Permasalahan bisnis utama yang ingin diselesaikan oleh Jaya Jaya Institute adalah:
1.  **Tingginya Angka Dropout Mahasiswa:** Institusi bertujuan untuk mengurangi jumlah mahasiswa yang tidak menyelesaikan studinya.
2.  **Kesulitan Mengidentifikasi Mahasiswa Berisiko:** Institusi memerlukan metode yang efektif untuk mengidentifikasi mahasiswa yang berpotensi *dropout* secara dini, sehingga intervensi yang tepat dapat segera dilakukan.
3.  **Optimalisasi Sumber Daya untuk Intervensi:** Dengan pemahaman mendalam mengenai faktor-faktor kunci dan identifikasi mahasiswa berisiko, institusi dapat mengalokasikan sumber daya (seperti bimbingan akademis, konseling, atau bantuan finansial) secara lebih efisien dan efektif.

### Cakupan Proyek
Cakupan proyek ini meliputi:
1.  **Analisis Data Historis Mahasiswa:** Melakukan eksplorasi data untuk mengidentifikasi pola dan faktor-faktor yang berkorelasi kuat dengan status kelulusan atau *dropout* mahasiswa.
2.  **Pengembangan Model Machine Learning:** Membangun model prediktif yang mampu mengklasifikasikan apakah seorang mahasiswa berpotensi untuk *Graduate* (Lulus) atau *Dropout* berdasarkan fitur-fitur akademis dan demografis tertentu.
3.  **Pembuatan Prototipe Sistem Prediksi:** Mengembangkan antarmuka pengguna yang sederhana (menggunakan Streamlit) yang memungkinkan pengguna (staf akademik, konselor) untuk memasukkan data mahasiswa dan mendapatkan prediksi status akademisnya secara instan.
4.  **Penyajian Business Dashboard:** Membuat visualisasi data interaktif (dashboard) yang merangkum temuan-temuan kunci dari analisis data, khususnya terkait karakteristik mahasiswa yang mengalami *dropout*.

### Persiapan

**Sumber data:**

Dataset yang digunakan dalam proyek ini adalah "Predict students' dropout and academic success". Dataset ini berisi berbagai atribut demografis, sosio-ekonomi, dan akademik mahasiswa dari sebuah institusi pendidikan tinggi di Portugal. Tujuan utama penggunaan dataset ini adalah untuk membangun model yang dapat memprediksi apakah seorang mahasiswa akan lulus (Graduate) atau putus kuliah (Dropout).
Dataset ini tersedia secara publik dan dapat diakses melalui:
-   Sumber Asli (UCI Machine Learning Repository): [https://doi.org/10.24432/C5MC89](https://doi.org/10.24432/C5MC89)
-   Sumber Lainnya (Dicoding Academy): [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Setup environment:**

Untuk memastikan proyek ini dapat berjalan dengan baik dan dependensi terkelola dengan baik, disarankan menggunakan virtual environment.
```bash
# 1. Buat environment virtual bernama 'student_performance_env'
python -m venv student_performance_env

# 2. Aktifkan environment virtual
# Untuk Windows (Command Prompt/PowerShell):
student_performance_env\Scripts\activate
# Untuk macOS/Linux (bash/zsh):
source student_performance_env/bin/activate

# 3. Upgrade pip di dalam environment (opsional namun direkomendasikan)
python -m pip install --upgrade pip

# 4. Install semua library yang dibutuhkan
pip install -r requirements.txt
```

**Komponen Inti Sistem Prediksi:**
Sistem prediksi ini mengandalkan beberapa komponen kunci:
*   `logistic_regression_best_model.joblib`: File model Machine Learning (Logistic Regression) yang sudah dilatih dan dioptimalkan, siap untuk melakukan prediksi.
*   `prediction.py`: Skrip Python yang berisi logika untuk memuat model, menerima input data mahasiswa, dan menghasilkan prediksi.
*   `data_preprocessing.py`: Skrip Python yang berisi fungsi-fungsi untuk pra-pemrosesan data input agar sesuai dengan format yang dibutuhkan oleh model.

## Business Dashboard
![Business Dashboard Preview](https://raw.githubusercontent.com/rahadianMs/Github-MyPortfolio/refs/heads/main/Dasboard.jpg)

Business dashboard telah dibuat menggunakan Looker Studio untuk menyediakan visualisasi data yang interaktif dan *insight* cepat mengenai profil mahasiswa, khususnya yang mengalami *dropout*. Dashboard ini bertujuan membantu manajemen dalam memahami karakteristik mahasiswa *dropout* dan mengidentifikasi area potensial untuk intervensi.

Anda dapat mengakses dashboard tersebut melalui tautan berikut:
[Lihat Business Dashboard di Looker Studio](https://lookerstudio.google.com/reporting/4e2e74d2-7e34-401f-9c31-665fc771299a)

Dashboard ini menyajikan berbagai metrik dan visualisasi kunci, antara lain:

*   **KPI Utama:**
    *   **Jumlah Dropout:** Menampilkan total mahasiswa yang teridentifikasi sebagai *dropout* (1.421 mahasiswa dari dataset yang dianalisis).
    *   **Dropout Rate:** Mengindikasikan persentase mahasiswa yang *dropout* (32,12%), memberikan gambaran skala permasalahan.
    *   **Nilai rata-rata (Curricular units 1st/2nd sem grade):** Rata-rata nilai mahasiswa yang *dropout* adalah 124,96 (interpretasi nilai ini mungkin memerlukan konteks skala penilaian spesifik, namun dashboard menampilkan perbandingan).

*   **Analisis Profil Mahasiswa Dropout:**
    *   **Beasiswa:** Hanya **9,4%** mahasiswa *dropout* yang merupakan penerima beasiswa, menunjukkan mayoritas (**90,6%**) yang *dropout* tidak menerima beasiswa. Ini mengindikasikan bahwa faktor finansial atau dukungan yang datang bersama beasiswa mungkin berperan dalam retensi.
    *   **Displaced (Pindahan/Terlantar):** Distribusi mahasiswa *dropout* yang berstatus *displaced* (**52,9% Ya** vs **47,1% Tidak**) cukup seimbang, menunjukkan bahwa status ini mungkin menjadi salah satu faktor risiko, meskipun tidak dominan secara absolut.
    *   **Gender:** Distribusi gender mahasiswa *dropout* juga relatif seimbang (**50,7% Perempuan** vs **49,3% Laki-laki**), mengindikasikan bahwa gender mungkin bukan pembeda utama dalam risiko *dropout* pada populasi ini.
    *   **Waktu Hadir (Daytime/Evening):** Mayoritas mahasiswa *dropout* (**85,4%**) berasal dari kelas siang (*daytime*), sementara hanya **14,6%** dari kelas malam (*evening*). Ini adalah temuan signifikan yang mungkin memerlukan investigasi lebih lanjut terkait tantangan spesifik mahasiswa kelas siang.
    *   **Debtor (Memiliki Hutang):** Hanya **22%** mahasiswa *dropout* yang tercatat sebagai *debtor* (memiliki hutang biaya kuliah), sementara mayoritas (**78%**) tidak. Ini menunjukkan bahwa status hutang langsung mungkin bukan pemicu utama *dropout* bagi sebagian besar kasus.
    *   **Tuition Fee up to date (Biaya Kuliah Lunas):** Sebagian besar mahasiswa *dropout* (**67,8%**) membayar biaya kuliah tepat waktu (*Yes*), sementara **32,2%** tidak (*No*). Meskipun mayoritas membayar tepat waktu, sepertiga yang tidak membayar tetap menjadi kelompok yang signifikan.
    *   **Status Marital:** Mahasiswa *dropout* didominasi oleh mereka yang berstatus *single*. Angka spesifik tidak disebutkan di sini, namun ini adalah observasi penting yang mengarah pada potensi kurangnya sistem pendukung personal.

*   **Perbandingan Akademis:**
    *   **Units Approved vs Enrolled Semester 1 & 2:** Visualisasi ini secara jelas membandingkan rata-rata jumlah unit (SKS) yang disetujui (lulus) dengan jumlah unit yang diambil (terdaftar) oleh mahasiswa yang *Graduate* dan *Dropout* pada semester 1 dan 2. Terlihat pola konsisten bahwa mahasiswa yang *Graduate* cenderung memiliki jumlah unit yang disetujui lebih tinggi dan lebih mendekati (atau sama dengan) jumlah unit yang mereka ambil, dibandingkan dengan mahasiswa yang *Dropout*. Mahasiswa *Dropout* seringkali menunjukkan selisih yang lebih besar antara unit yang diambil dan yang berhasil disetujui, menandakan kesulitan akademis sejak awal.

Dashboard ini sangat berguna bagi manajemen untuk memahami secara cepat dan mendalam karakteristik umum mahasiswa yang *dropout*, mengidentifikasi segmen mahasiswa yang paling berisiko, dan sebagai dasar untuk merumuskan strategi intervensi yang lebih terarah.

## Menjalankan Sistem Machine Learning
![Streamlit App Preview](https://raw.githubusercontent.com/rahadianMs/Github-MyPortfolio/refs/heads/main/Streamlit.jpg)

Prototipe sistem prediksi performa mahasiswa telah dikembangkan sebagai aplikasi web interaktif menggunakan Streamlit. Aplikasi ini dirancang untuk memudahkan staf akademik atau konselor dalam mendapatkan prediksi potensi *dropout* seorang mahasiswa secara cepat berdasarkan data akademis mereka.

**Cara Menjalankan dan Menggunakan Prototipe Sistem Prediksi:**

1.  **Akses Aplikasi Web:**
    Buka peramban web Anda (seperti Chrome, Firefox, atau Edge) dan kunjungi tautan berikut untuk mengakses prototipe:
    ```
    https://predict-student.streamlit.app/
    ```

2.  **Pahami Antarmuka Pengguna:**
    Setelah halaman dimuat, Anda akan melihat antarmuka sederhana berjudul "🎓 Jaya Jaya Institute - Student Performance Prediction". Terdapat beberapa kolom input yang perlu diisi.

3.  **Masukkan Data Akademis Mahasiswa:**
    Isi informasi akademis mahasiswa pada kolom-kolom yang tersedia. Data yang dibutuhkan adalah:
    *   **Data Semester 1:**
        *   `Curricular units 1st sem (approved)`: Jumlah SKS yang disetujui/lulus pada semester 1.
        *   `Curricular units 1st sem (grade)`: Rata-rata nilai pada semester 1.
        *   `Curricular units 1st sem (enrolled)`: Jumlah SKS yang diambil pada semester 1.
    *   **Data Semester 2:**
        *   `Curricular units 2nd sem (approved)`: Jumlah SKS yang disetujui/lulus pada semester 2.
        *   `Curricular units 2nd sem (grade)`: Rata-rata nilai pada semester 2.
        *   `Curricular units 2nd sem (enrolled)`: Jumlah SKS yang diambil pada semester 2.

    Pastikan untuk memasukkan nilai numerik yang valid untuk setiap kolom.

4.  **Lakukan Prediksi:**
    Setelah semua data dimasukkan dengan benar, klik tombol "**✨ Predict Performance**" yang terletak di bawah kolom input.

5.  **Lihat Hasil Prediksi:**
    Sistem akan memproses data yang Anda masukkan menggunakan model machine learning yang telah dilatih. Hasil prediksi akan ditampilkan secara langsung di bawah tombol, memberitahukan apakah mahasiswa tersebut diprediksi akan "**Graduate**" (Lulus) atau "**Dropout**".

Fitur-fitur yang digunakan untuk prediksi adalah 6 fitur numerik di atas, yang dipilih karena memiliki korelasi tertinggi dengan status kelulusan dan relatif mudah diperoleh dari catatan akademik mahasiswa.

## Conclusion
Proyek ini berhasil menjawab tantangan yang dihadapi Jaya Jaya Institute dalam upaya memahami dan mengurangi angka *dropout* mahasiswa serta mengoptimalkan sumber daya intervensi. Pencapaian ini diwujudkan melalui dua output utama: **Business Dashboard** yang informatif dan **Sistem Prediksi Machine Learning** yang fungsional.

**Dari Business Dashboard, dapat disimpulkan bahwa:**
Profil mahasiswa *dropout* memiliki karakteristik yang cukup spesifik. Mayoritas dari mereka **tidak menerima beasiswa (90,6%)**, cenderung berasal dari **kelas siang (85,4%)**, dan berstatus **single**. Meskipun status hutang (*debtor*) tidak dominan (hanya 22%), namun sekitar sepertiga mahasiswa *dropout* memiliki tunggakan biaya kuliah. Secara akademis, mahasiswa *dropout* secara konsisten menunjukkan **kesenjangan yang lebih besar antara SKS yang diambil dengan SKS yang berhasil disetujui** di semester awal, menandakan kesulitan akademis yang muncul dini. Temuan ini secara langsung membantu **mengidentifikasi segmen mahasiswa yang memerlukan perhatian lebih**, sehingga intervensi dapat dirancang lebih spesifik. Misalnya, program dukungan finansial dan non-finansial bagi non-penerima beasiswa, atau investigasi lebih lanjut terhadap tantangan unik mahasiswa kelas siang.

**Sistem Prediksi Machine Learning** yang dikembangkan menggunakan model Logistic Regression dengan 6 fitur akademis utama menunjukkan performa yang solid (**Accuracy: 89%, Precision: 89%, Recall: 87%, F1-score: 89%**). Ini berarti model tersebut cukup andal dalam **mengidentifikasi mahasiswa berisiko *dropout* secara dini**, yang merupakan inti dari permasalahan kedua. Dengan adanya prototipe aplikasi Streamlit, staf akademik memiliki alat praktis untuk melakukan skrining awal, memungkinkan intervensi proaktif sebelum mahasiswa benar-benar keluar.

**Secara keseluruhan, proyek ini berkontribusi pada penyelesaian permasalahan bisnis sebagai berikut:**
1.  **Mengurangi Tingginya Angka Dropout Mahasiswa:** Dengan pemahaman mendalam dari dashboard mengenai faktor risiko dan kemampuan prediksi dari model, institusi dapat merancang strategi intervensi yang lebih efektif dan tepat sasaran, yang pada gilirannya berpotensi menurunkan angka *dropout*.
2.  **Memudahkan Identifikasi Mahasiswa Berisiko:** Prototipe sistem prediksi menyediakan alat langsung untuk identifikasi dini. Dashboard juga membantu mengenali pola karakteristik mahasiswa yang rentan *dropout*.
3.  **Mengoptimalkan Sumber Daya untuk Intervensi:** Dengan mengetahui siapa yang berisiko dan mengapa (berdasarkan profil dari dashboard), Jaya Jaya Institute dapat mengalokasikan sumber daya (konseling, bantuan akademis, finansial) secara lebih efisien kepada mahasiswa yang paling membutuhkan, menghindari pendekatan "satu untuk semua" yang kurang efektif.

Pemilihan 6 fitur akademis untuk model prediksi juga selaras dengan kebutuhan bisnis akan data yang mudah diakses dan dapat ditindaklanjuti. Keberhasilan proyek ini meletakkan dasar yang kuat bagi Jaya Jaya Institute untuk mengambil keputusan berbasis data dalam meningkatkan keberhasilan akademis mahasiswa.

### Rekomendasi Action Items
Berdasarkan hasil analisis, *insight* dari dashboard, dan fungsionalitas sistem prediksi, berikut adalah beberapa rekomendasi *action items* untuk Jaya Jaya Institute:

-   **Implementasi Sistem Deteksi Dini Secara Terintegrasi:** Integrasikan prototipe sistem prediksi ke dalam sistem informasi akademik yang sudah ada atau jadikan alat standar bagi dosen wali/konselor akademik untuk melakukan pemantauan mahasiswa secara berkala, khususnya setelah evaluasi semester pertama dan kedua.
-   **Pengembangan Program Dukungan Tertarget:**
    -   Tingkatkan aksesibilitas dan promosi program beasiswa atau bantuan finansial, mengingat mayoritas mahasiswa *dropout* tidak menerima beasiswa.
    -   Lakukan analisis lebih mendalam terhadap faktor penyebab tingginya angka *dropout* pada mahasiswa kelas siang (*daytime*) dan rancang intervensi spesifik, seperti sesi bimbingan tambahan, fleksibilitas jadwal, atau dukungan komunitas khusus.
    -   Sediakan layanan konseling keuangan yang proaktif dan mudah diakses, serta program pendampingan bagi mahasiswa yang menunjukkan kesulitan akademis awal (gap besar antara SKS diambil dan disetujui).
-   **Penguatan Keterlibatan dan Komunitas Mahasiswa:** Mengingat dominasi mahasiswa berstatus *single* dalam kelompok *dropout*, perkuat program-program yang bertujuan meningkatkan keterlibatan sosial, rasa memiliki terhadap komunitas kampus, dan dukungan *peer-to-peer* (misalnya, klub, organisasi mahasiswa, program mentoring).
-   **Evaluasi dan Iterasi Model Prediksi Secara Berkelanjutan:** Lakukan pemantauan performa model secara periodik. Kumpulkan data mahasiswa baru secara kontinu untuk melakukan *retraining* model (misalnya, setiap akhir tahun ajaran) guna menjaga akurasi dan relevansinya. Pertimbangkan eksplorasi fitur tambahan (misalnya, data kehadiran, aktivitas ekstrakurikuler) atau algoritma machine learning alternatif di masa depan.
-   **Pemanfaatan Aktif Business Dashboard untuk Keputusan Strategis:** Gunakan *business dashboard* sebagai alat bantu utama dalam rapat evaluasi manajemen untuk memonitor tren *dropout*, memahami dinamika profil mahasiswa, serta mengukur efektivitas intervensi yang telah diimplementasikan.

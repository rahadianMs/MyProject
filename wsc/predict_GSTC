import streamlit as st
import time

# --- Konfigurasi Aplikasi ---
st.set_page_config(
    page_title="Konsultasi Keberlanjutan | Analisis Kebutuhan Anda",
    layout="centered"
)

# --- Database Pertanyaan & Opsi ---
# Semua pertanyaan dan pilihan jawaban kita simpan di sini agar mudah diubah.
questions = {
    "q1": {
        "question": "Tipe Usaha Anda",
        "options": [
            "Hotel Bintang 4-5", "Hotel Bintang 3 atau di bawahnya", "Homestay / Guesthouse",
            "Resort / Luxury Villa", "Tour Operator", "Lainnya"
        ]
    },
    "q2": {
        "question": "Ukuran Usaha Anda",
        "options": [
            "Sangat kecil (1–5 karyawan)", "Kecil (6–20 karyawan)",
            "Menengah (21–100 karyawan)", "Besar (lebih dari 100 karyawan)"
        ]
    },
    "q3": {
        "question": "Di tahap manakah perjalanan keberlanjutan perusahaan Anda saat ini?",
        "options": [
            "Baru Memulai: Kami butuh arahan untuk langkah pertama.",
            "Sudah Berjalan: Inisiatif kami belum terstruktur dan terukur.",
            "Tingkat Lanjut: Kami ingin sertifikasi atau optimalisasi pelaporan."
        ]
    },
    "q4": {
        "question": "Apa tujuan utama yang ingin Anda capai dalam 1-2 tahun ke depan?",
        "options": [
            "Membuat perencanaan dan peta jalan (roadmap) strategis.",
            "Meningkatkan pengetahuan dan kapasitas tim internal.",
            "Mengukur dan memonitor kinerja sustainability secara efektif.",
            "Mengelola masalah spesifik seperti limbah makanan (food waste).",
            "Mendapatkan sertifikasi keberlanjutan tingkat internasional.",
            "Mengkomunikasikan upaya kami untuk memperkuat citra merek (branding).",
            "Menyusun laporan (report) untuk kebutuhan stakeholder."
        ]
    },
    "q5": {
        "question": "Apa tantangan operasional terbesar yang Anda hadapi saat ini?",
        "options": [
            "Biaya operasional tinggi (listrik, air).",
            "Biaya bahan makanan (food cost) dan jumlah sisa makanan yang besar.",
            "Kesulitan melacak data dan progres inisiatif keberlanjutan.",
            "Tuntutan dari investor atau korporasi induk untuk pelaporan ESG.",
            "Tim belum memiliki pemahaman yang cukup tentang praktik keberlanjutan.",
            "Belum tahu cara 'menjual' program hijau kami ke pasar."
        ]
    },
    "q6": {
        "question": "Siapa target pasar utama yang menjadi fokus bisnis Anda?",
        "options": [
            "Wisatawan domestik & grup (Cenderung sensitif terhadap harga)",
            "Wisatawan internasional & keluarga (Mulai mencari opsi berkelanjutan)",
            "Wisatawan mewah & korporat (Memiliki ekspektasi tinggi terhadap keberlanjutan)",
            "Pasar atau minat khusus (Ekowisata, MICE, Wellness, dll.)"
        ]
    }
}

# --- Logika Diagnosis & Rekomendasi ---
def analyze_needs(answers):
    """
    Fungsi ini adalah "otak" dari Akinator.
    Ini menganalisis jawaban dan merekomendasikan paket yang sesuai.
    """
    # Inisialisasi skor kelemahan untuk setiap aspek GSTC
    weakness_scores = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'Branding': 0}

    # Analisis berdasarkan jawaban
    # q3: Tahap Perjalanan
    if answers['q3'] == "Baru Memulai: Kami butuh arahan untuk langkah pertama.":
        weakness_scores['A'] += 3
        weakness_scores['D'] += 1
    elif answers['q3'] == "Sudah Berjalan: Inisiatif kami belum terstruktur dan terukur.":
        weakness_scores['A'] += 2
        
    # q4: Tujuan Utama
    if "roadmap" in answers['q4']: weakness_scores['A'] += 2
    if "kapasitas tim" in answers['q4']: weakness_scores['A'] += 2
    if "Mengukur dan memonitor" in answers['q4']: weakness_scores['A'] += 2
    if "limbah makanan" in answers['q4']: weakness_scores['D'] += 3
    if "sertifikasi" in answers['q4']: weakness_scores['A'] += 3
    if "branding" in answers['q4']: weakness_scores['Branding'] += 3
    if "laporan" in answers['q4']: weakness_scores['A'] += 2

    # q5: Tantangan Terbesar
    if "Biaya operasional tinggi" in answers['q5']: weakness_scores['D'] += 3
    if "Biaya bahan makanan" in answers['q5']: weakness_scores['D'] += 3
    if "Kesulitan melacak data" in answers['q5']: weakness_scores['A'] += 2
    if "Tuntutan dari investor" in answers['q5']: weakness_scores['A'] += 2
    if "Tim belum memiliki pemahaman" in answers['q5']: weakness_scores['A'] += 3
    if "menjual" in answers['q5']: weakness_scores['Branding'] += 3

    # Tentukan area terlemah
    primary_weakness = max(weakness_scores, key=weakness_scores.get)

    # Siapkan Rekomendasi
    recommendation = {
        "primary_focus_area": "",
        "primary_package_name": "",
        "primary_package_desc": "",
        "secondary_package_name": "",
        "secondary_package_desc": ""
    }

    # Aturan Rekomendasi Paket
    if primary_weakness == 'A':
        recommendation['primary_focus_area'] = "Manajemen & Strategi Keberlanjutan (Aspek A)"
        recommendation['primary_package_name'] = "Paket Pondasi & Peta Jalan Strategis"
        recommendation['primary_package_desc'] = "Kami akan membantu Anda membangun sistem manajemen yang kokoh, menetapkan tujuan yang jelas, melatih tim Anda, dan membuat roadmap keberlanjutan yang terukur dan sesuai dengan standar GSTC."
    elif primary_weakness == 'D':
        recommendation['primary_focus_area'] = "Efisiensi Sumber Daya & Lingkungan (Aspek D)"
        recommendation['primary_package_name'] = "Paket Efisiensi Operasional & Penghematan Biaya"
        recommendation['primary_package_desc'] = "Fokus kami adalah mengurangi biaya operasional Anda secara signifikan melalui audit energi dan air, program manajemen limbah (termasuk food waste), dan implementasi teknologi hijau yang efisien."
    elif primary_weakness == 'Branding':
        recommendation['primary_focus_area'] = "Komunikasi & Pemasaran Hijau"
        recommendation['primary_package_name'] = "Paket Branding & Komunikasi Keberlanjutan"
        recommendation['primary_package_desc'] = "Jangan biarkan upaya baik Anda tidak terlihat. Kami akan membantu Anda menyusun narasi yang kuat, membuat materi pemasaran yang menarik, dan mengkomunikasikan komitmen Anda kepada pasar untuk meningkatkan citra merek dan loyalitas pelanggan."
    else: # Default jika tidak ada yang menonjol
        recommendation['primary_focus_area'] = "Manajemen & Strategi Keberlanjutan (Aspek A)"
        recommendation['primary_package_name'] = "Paket Pondasi & Peta Jalan Strategis"
        recommendation['primary_package_desc'] = "Kami akan membantu Anda membangun sistem manajemen yang kokoh, menetapkan tujuan yang jelas, melatih tim Anda, dan membuat roadmap keberlanjutan yang terukur dan sesuai dengan standar GSTC."

    # Rekomendasi sekunder
    if "sertifikasi" in answers['q4'] and primary_weakness != 'A':
        recommendation['secondary_package_name'] = "Pendampingan Sertifikasi Internasional"
        recommendation['secondary_package_desc'] = "Sebagai langkah lanjutan, kami bisa mendampingi Anda melalui proses kompleks untuk mendapatkan sertifikasi GSTC atau standar internasional lainnya."

    return recommendation


# --- Antarmuka Aplikasi Streamlit ---
def main():
    st.image("https://storage.googleapis.com/gweb-cloud-think-process-website-share-v2-screenshots/gstc-logo.2.png", width=200)
    st.title("Analisis Kebutuhan Keberlanjutan Anda")
    st.markdown("Jawab 6 pertanyaan singkat ini untuk menemukan solusi dan paket pendampingan yang paling tepat untuk bisnis Anda. **Hanya 2 menit!**")

    # Form untuk menampung semua pertanyaan
    with st.form("consulting_form"):
        answers = {}
        for key, q_data in questions.items():
            answers[key] = st.selectbox(q_data["question"], options=q_data["options"], key=key)
        
        submitted = st.form_submit_button("Analisis Kebutuhan Saya!", type="primary")

    # Logika setelah form disubmit
    if submitted:
        with st.spinner("Menganalisis jawaban Anda dan menyiapkan rekomendasi personal..."):
            time.sleep(2)
            result = analyze_needs(answers)
        
        st.success("Analisis Selesai!")
        st.balloons()
        
        st.header("Diagnosis & Rekomendasi Untuk Anda")
        
        st.markdown(f"Berdasarkan jawaban Anda, kami mengidentifikasi bahwa **prioritas utama** Anda saat ini adalah pada area **{result['primary_focus_area']}**.")
        
        # Tampilkan rekomendasi paket utama
        st.subheader(f"✅ Rekomendasi Utama: {result['primary_package_name']}")
        st.info(result['primary_package_desc'])

        # Tampilkan rekomendasi paket sekunder jika ada
        if result['secondary_package_name']:
            st.subheader(f"➡️ Langkah Selanjutnya: {result['secondary_package_name']}")
            st.info(result['secondary_package_desc'])
            
        # Call to Action (Ajakan Bertindak)
        st.divider()
        st.header("Siap Mengambil Langkah Selanjutnya?")
        st.markdown(
            "Tim kami siap membantu Anda. Jadwalkan sesi konsultasi gratis untuk membahas hasil ini lebih lanjut dan bagaimana kami bisa membantu Anda mencapai tujuan."
        )
        st.link_button("Hubungi Kami Sekarang", "mailto:konsultan@keberlanjutan.com")

if __name__ == "__main__":
    main()

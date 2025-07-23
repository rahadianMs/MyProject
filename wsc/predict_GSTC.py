import streamlit as st
import time

# --- Konfigurasi Aplikasi ---
st.set_page_config(
    page_title="Rekomendasi Solusi Wisata Berkelanjutan",
    layout="centered"
)

# --- 1. Database Layanan Anda ---
# Menyimpan semua deskripsi layanan di satu tempat agar mudah dikelola.
services = {
    "Tourism Master Plan & Destination Development": "Pendampingan rencana pengembangan destinasi berbasis potensi lokal dan tren pasar.",
    "Feasibility Study & Financial Projection": "Analisis kelayakan pasar, operasional, dan finansial untuk memastikan proyek wisata realistis.",
    "Sustainability Roadmap & Action Plan": "Menyusun peta jalan keberlanjutan dengan langkah konkret sesuai kapasitas organisasi.",
    "ESG & Sustainability Reporting": "Membantu organisasi menyusun laporan ESG sesuai standar global dan strategi bisnis.",
    "Sustainability Performance Dashboard": "Dashboard visual memantau kinerja keberlanjutan untuk pengambilan keputusan cepat.",
    "Sustainability Certification Assistance": "Pendampingan lengkap proses sertifikasi keberlanjutan hingga implementasi perbaikan.",
    "Event Planning": "Merancang event bermakna dan berkelanjutan dari konsep hingga pelaksanaan teknis.",
    "Integrated Marketing Strategy": "Strategi pemasaran terpadu berbasis data untuk menjangkau audiens tepat dengan efektif.",
    "Tourism Impact and Carrying Capacity Assessment": "Mengukur dampak pariwisata dan kapasitas destinasi demi kelestarian jangka panjang.",
    "Customer Experience Feedback Analysis": "Evaluasi kualitas layanan via mystery shopper dan ulasan digital untuk peningkatan bisnis.",
    "Tourist Behaviour and Perception Analysis": "Memahami motivasi, ekspektasi, dan persepsi wisatawan untuk desain pengalaman optimal.",
    "GSTC Sustainable Tourism Course (STC)": "Pelatihan standar GSTC untuk praktik pariwisata berkelanjutan dengan sertifikasi resmi.",
    "Sustainability Action Plan Workshop": "Workshop kolaboratif menyusun rencana aksi keberlanjutan yang terukur dan realistis.",
    "Customized In-House Training (CIHT)": "Pelatihan khusus sesuai kebutuhan organisasi di bidang pariwisata dan keberlanjutan."
}

# --- 2. Pertanyaan Diagnostik ---
questions = {
    "q1_tipe": {"question": "Tipe Usaha Anda", "options": ["Hotel Bintang 4-5", "Hotel Bintang 3 atau di bawahnya", "Homestay / Guesthouse", "Resort / Luxury Villa", "Tour Operator", "Lainnya"]},
    "q2_ukuran": {"question": "Ukuran Usaha Anda", "options": ["Sangat kecil (1–5 karyawan)", "Kecil (6–20 karyawan)", "Menengah (21–100 karyawan)", "Besar (lebih dari 100 karyawan)"]},
    "q3_tahap": {"question": "Di tahap manakah perjalanan keberlanjutan Anda saat ini?", "options": ["Baru Memulai: Butuh arahan untuk langkah pertama.", "Sudah Berjalan: Inisiatif belum terstruktur dan terukur.", "Tingkat Lanjut: Ingin sertifikasi atau optimalisasi pelaporan."]},
    "q4_tujuan": {"question": "Apa tujuan utama Anda dalam 1-2 tahun ke depan?", "options": list(services.keys())[2:8]}, # Mengambil dari daftar layanan
    "q5_tantangan": {"question": "Apa tantangan operasional terbesar Anda saat ini?", "options": ["Biaya operasional tinggi (listrik, air).", "Biaya bahan makanan (food cost) dan jumlah sisa makanan yang besar.", "Kesulitan melacak data dan progres keberlanjutan.", "Tuntutan dari investor untuk pelaporan ESG.", "Tim belum memiliki pemahaman yang cukup.", "Belum tahu cara 'menjual' program hijau ke pasar."]},
    "q6_pasar": {"question": "Siapa target pasar utama Anda?", "options": ["Wisatawan domestik & grup (Sensitif harga)", "Wisatawan internasional & keluarga (Mulai mencari opsi berkelanjutan)", "Wisatawan mewah & korporat (Ekspektasi tinggi terhadap keberlanjutan)", "Pasar khusus (Ekowisata, MICE, Wellness, dll.)"]},
}

# --- 3. Otak Analisis & Rekomendasi ---
def get_recommendations(answers):
    """
    Menganalisis jawaban dan memberikan skor pada setiap layanan.
    Mengembalikan 3 layanan dengan skor tertinggi.
    """
    scores = {service: 0 for service in services}

    # Aturan Skoring Berdasarkan Jawaban
    # q3: Tahap Perjalanan
    if "Baru Memulai" in answers["q3_tahap"]:
        scores["Sustainability Roadmap & Action Plan"] += 3
        scores["GSTC Sustainable Tourism Course (STC)"] += 2
        scores["Sustainability Action Plan Workshop"] += 2
    elif "Sudah Berjalan" in answers["q3_tahap"]:
        scores["Sustainability Performance Dashboard"] += 3
        scores["Sustainability Roadmap & Action Plan"] += 2
        scores["ESG & Sustainability Reporting"] += 1
    elif "Tingkat Lanjut" in answers["q3_tahap"]:
        scores["Sustainability Certification Assistance"] += 3
        scores["ESG & Sustainability Reporting"] += 3
        scores["Tourism Impact and Carrying Capacity Assessment"] += 2

    # q4: Tujuan Utama (Sangat Relevan)
    if "roadmap" in answers["q4_tujuan"]: scores["Sustainability Roadmap & Action Plan"] += 5
    if "kapasitas tim" in answers["q4_tujuan"]: 
        scores["Customized In-House Training (CIHT)"] += 5
        scores["GSTC Sustainable Tourism Course (STC)"] += 3
    if "Mengukur dan memonitor" in answers["q4_tujuan"]: scores["Sustainability Performance Dashboard"] += 5
    if "sertifikasi" in answers["q4_tujuan"]: scores["Sustainability Certification Assistance"] += 5
    if "branding" in answers["q4_tujuan"]: scores["Integrated Marketing Strategy"] += 5
    if "report" in answers["q4_tujuan"]: scores["ESG & Sustainability Reporting"] += 5

    # q5: Tantangan Terbesar
    if "Biaya operasional" in answers["q5_tantangan"]: scores["Sustainability Roadmap & Action Plan"] += 3
    if "Kesulitan melacak data" in answers["q5_tantangan"]: scores["Sustainability Performance Dashboard"] += 3
    if "Tuntutan dari investor" in answers["q5_tantangan"]: scores["ESG & Sustainability Reporting"] += 3
    if "Tim belum memiliki pemahaman" in answers["q5_tantangan"]:
        scores["GSTC Sustainable Tourism Course (STC)"] += 3
        scores["Customized In-House Training (CIHT)"] += 2
    if "menjual" in answers["q5_tantangan"]:
        scores["Integrated Marketing Strategy"] += 3
        scores["Customer Experience Feedback Analysis"] += 1

    # q6: Target Pasar
    if "mewah & korporat" in answers["q6_pasar"]:
        scores["Sustainability Certification Assistance"] += 2
        scores["ESG & Sustainability Reporting"] += 2
        scores["Customer Experience Feedback Analysis"] += 1
    if "Ekowisata" in answers["q6_pasar"]: scores["Tourism Impact and Carrying Capacity Assessment"] += 2
    if "MICE" in answers["q6_pasar"]: scores["Event Planning"] += 2

    # Urutkan layanan berdasarkan skor tertinggi dan ambil 3 teratas
    sorted_services = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return sorted_services[:3]

# --- 4. Antarmuka Aplikasi Streamlit ---
def main():
    st.image("https://storage.googleapis.com/gweb-cloud-think-process-website-share-v2-screenshots/gstc-logo.2.png", width=200)
    st.title("Temukan Solusi Keberlanjutan Untuk Anda")
    st.markdown("Hanya dalam **2 menit**, jawab 6 pertanyaan ini dan dapatkan **3 rekomendasi layanan** yang paling sesuai untuk bisnis Anda.")

    with st.form("solution_finder_form"):
        answers = {}
        # Menampilkan pertanyaan dari q1 hingga q6
        for key, q_data in questions.items():
            answers[key] = st.selectbox(q_data["question"], options=q_data["options"], key=key)
        
        submitted = st.form_submit_button("Lihat Rekomendasi Saya", type="primary", use_container_width=True)

    if submitted:
        with st.spinner("Menganalisis kebutuhan Anda..."):
            time.sleep(1.5)
            recommendations = get_recommendations(answers)
        
        st.success("Analisis Selesai! Berikut adalah solusi yang kami rekomendasikan untuk Anda.")
        st.balloons()
        
        st.header("Top 3 Rekomendasi Solusi")

        # Menampilkan 3 rekomendasi teratas
        for i, (service_name, score) in enumerate(recommendations):
            if score > 0: # Hanya tampilkan jika relevan (skor > 0)
                st.subheader(f"#{i+1} {service_name}")
                st.write(services[service_name])
                st.divider()

        # Call to Action
        st.header("Siap untuk Bertumbuh?")
        st.markdown(
            "Rekomendasi di atas adalah titik awal yang kuat. Mari diskusikan lebih lanjut bagaimana kami dapat membantu Anda dalam sesi konsultasi gratis."
        )
        st.link_button("Jadwalkan Konsultasi Gratis Sekarang", "mailto:info@konsultanpariwisata.com?subject=Konsultasi%20Hasil%20Analisis%20Kebutuhan")

if __name__ == "__main__":
    main()```

# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit v4.0: Akinator Konsultan dengan Machine Learning
Model: Multi-Label Classification untuk rekomendasi yang lebih akurat.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
import time

# =============================================================================
# KONFIGURASI APLIKASI
# =============================================================================
st.set_page_config(
    page_title="Analisis Kebutuhan Berbasis AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# DATABASE LAYANAN & PERTANYAAN (Tetap sama)
# =============================================================================

SERVICES = {
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

QUESTIONS = {
    "q1_tipe": {"question": "Tipe Usaha Anda", "options": ["Hotel Bintang 4-5", "Hotel Bintang 3 atau di bawahnya", "Homestay / Guesthouse", "Resort / Luxury Villa", "Tour Operator", "Lainnya"]},
    "q2_tahap": {"question": "Di tahap manakah perjalanan keberlanjutan Anda saat ini?", "options": ["Baru Memulai: Butuh arahan untuk langkah pertama.", "Sudah Berjalan: Inisiatif belum terstruktur dan terukur.", "Tingkat Lanjut: Ingin sertifikasi atau optimalisasi pelaporan."]},
    "q3_aset": {"question": "Apa aset utama yang menjadi kekuatan bisnis Anda?", "options": ["Lokasi strategis & pemandangan alam", "Bangunan ikonik & fasilitas mewah", "Pengalaman budaya & interaksi komunitas otentik", "Layanan personal & reputasi brand yang kuat"]},
    "q4_tujuan": {"question": "Apa tujuan utama Anda dalam 1-2 tahun ke depan?", "options": ["Membuat perencanaan strategis (roadmap)", "Meningkatkan kapasitas tim internal", "Mengukur & memonitor kinerja", "Mendapatkan sertifikasi internasional", "Memperkuat citra merek (branding)", "Menyusun laporan ESG/keberlanjutan"]},
    "q5_tantangan": {"question": "Apa tantangan operasional terbesar Anda saat ini?", "options": ["Biaya operasional tinggi (listrik, air)", "Kesulitan melacak data dan progres keberlanjutan", "Tuntutan dari investor untuk pelaporan ESG", "Tim belum memiliki pemahaman yang cukup", "Belum tahu cara 'menjual' program hijau ke pasar"]},
    "q6_pasar": {"question": "Siapa target pasar utama Anda?", "options": ["Wisatawan domestik & grup (Sensitif harga)", "Wisatawan internasional & keluarga (Mencari opsi berkelanjutan)", "Wisatawan mewah & korporat (Ekspektasi tinggi)", "Pasar khusus (Ekowisata, MICE, Wellness)"]},
    "q7_pemasaran": {"question": "Bagaimana fokus pemasaran Anda saat ini?", "options": ["Meningkatkan jumlah tamu baru", "Meningkatkan loyalitas tamu yang sudah ada", "Memasuki segmen pasar baru", "Memperkuat reputasi online (review & media sosial)"]},
    "q8_ukuran": {"question": "Ukuran Usaha Anda", "options": ["Sangat kecil (1–5 karyawan)", "Kecil (6–20 karyawan)", "Menengah (21–100 karyawan)", "Besar (lebih dari 100 karyawan)"]},
}

# =============================================================================
# LOGIKA MACHINE LEARNING
# =============================================================================

@st.cache_resource
def train_model():
    """
    Melatih model Machine Learning menggunakan data sintetis.
    Fungsi ini hanya dijalankan sekali.
    """
    # 1. Buat Data Sintetis (Fitur / X)
    num_samples = 2000
    synthetic_answers = []
    for _ in range(num_samples):
        answer_set = {key: np.random.choice(q_data["options"]) for key, q_data in QUESTIONS.items()}
        synthetic_answers.append(answer_set)
    X_df = pd.DataFrame(synthetic_answers)

    # 2. Buat Label "Ground Truth" (Target / y) berdasarkan aturan
    y_labels = []
    for index, row in X_df.iterrows():
        scores = {service: 0 for service in SERVICES}
        # (Logika skoring dari versi sebelumnya kita gunakan untuk membuat label)
        if "Baru Memulai" in row["q2_tahap"]:
            scores["Sustainability Roadmap & Action Plan"] += 5
            scores["Sustainability Action Plan Workshop"] += 3
        if "Tingkat Lanjut" in row["q2_tahap"]:
            scores["Sustainability Certification Assistance"] += 5
            scores["ESG & Sustainability Reporting"] += 4
        if "roadmap" in row["q4_tujuan"]: scores["Sustainability Roadmap & Action Plan"] += 5
        if "kapasitas tim" in row["q4_tujuan"]: scores["Customized In-House Training (CIHT)"] += 5
        if "sertifikasi" in row["q4_tujuan"]: scores["Sustainability Certification Assistance"] += 5
        if "branding" in row["q4_tujuan"]: scores["Integrated Marketing Strategy"] += 5
        if "laporan ESG" in row["q4_tujuan"]: scores["ESG & Sustainability Reporting"] += 5
        # ... (Anda bisa menambahkan lebih banyak aturan di sini)
        
        # Konversi skor menjadi label biner (0 atau 1)
        labels = {service: 1 if score >= 3 else 0 for service, score in scores.items()}
        y_labels.append(labels)
    y_df = pd.DataFrame(y_labels)

    # 3. Preprocessing Fitur (Mengubah Teks menjadi Angka)
    preprocessor = OneHotEncoder(handle_unknown='ignore')
    preprocessor.fit(X_df)
    X_processed = preprocessor.transform(X_df)

    # 4. Latih Model Multi-Label
    # Menggunakan RandomForest yang kuat, dibungkus MultiOutputClassifier
    forest = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model = MultiOutputClassifier(estimator=forest)
    model.fit(X_processed, y_df)
    
    return model, preprocessor

# =============================================================================
# ANTARMUKA PENGGUNA (TAMPILAN STREAMLIT)
# =============================================================================

def run_app():
    """Menjalankan seluruh alur aplikasi Streamlit."""
    
    # Latih atau muat model dan preprocessor dari cache
    model, preprocessor = train_model()
    
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnhT0JDtx12DjHca05hurtVr0QkmP4eNbsDw&s",
        use_container_width=True
    )
    st.title("Temukan Solusi Tepat Untuk Bisnis Anda")
    st.markdown("Hanya dalam **2 menit**, jawab 8 pertanyaan ini dan biarkan **AI** kami menganalisis kebutuhan Anda.")
    st.divider()

    with st.form("solution_finder_form"):
        answers = {}
        for key, q_data in QUESTIONS.items():
            answers[key] = st.selectbox(q_data["question"], options=q_data["options"], key=key)
        
        submitted = st.form_submit_button("ANALISIS & TEMUKAN SOLUSI SAYA", type="primary", use_container_width=True)

    if submitted:
        with st.spinner("Model Machine Learning sedang menganalisis jawaban Anda..."):
            # Siapkan input pengguna untuk model
            user_input_df = pd.DataFrame([answers])
            user_input_processed = preprocessor.transform(user_input_df)

            # Prediksi probabilitas untuk setiap layanan
            prediction_proba = model.predict_proba(user_input_processed)
            
            # Ekstrak probabilitas 'Yes' (kelas 1) untuk setiap layanan
            recommendation_scores = {}
            for i, service_name in enumerate(SERVICES.keys()):
                 # Probabilitas kelas 1 (Yes)
                recommendation_scores[service_name] = prediction_proba[i][0][1]

        st.success("Analisis Selesai! Berikut adalah rekomendasi berbasis AI untuk Anda.")
        st.balloons()

        # Urutkan rekomendasi berdasarkan probabilitas tertinggi
        sorted_recommendations = sorted(recommendation_scores.items(), key=lambda item: item[1], reverse=True)
        
        # Ambil rekomendasi utama
        primary_rec_name, primary_rec_score = sorted_recommendations[0]

        # Filter untuk rekomendasi pendukung (yang probabilitasnya di atas ambang batas tertentu)
        supporting_recs = [(name, score) for name, score in sorted_recommendations[1:] if score > 0.35]
        
        # Tampilkan Rekomendasi Utama
        st.header("⭐ Rekomendasi Utama Untuk Anda")
        with st.container(border=True):
            st.subheader(f"{primary_rec_name}")
            st.write(SERVICES[primary_rec_name])
            # st.caption(f"Tingkat Keyakinan Model: {primary_rec_score:.0%}") # Opsional: tampilkan keyakinan

        # Tampilkan Rekomendasi Pendukung
        if supporting_recs:
            st.header("💡 Solusi Pendukung yang Relevan")
            for service_name, score in supporting_recs[:2]: # Batasi maks 2 pendukung
                with st.container(border=True):
                    st.subheader(f"{service_name}")
                    st.write(SERVICES[service_name])
                    # st.caption(f"Tingkat Keyakinan Model: {score:.0%}") # Opsional
        
        # Call to Action
        st.divider()
        st.header("Siap Mengambil Langkah Berikutnya?")
        st.markdown(
            "Rekomendasi di atas adalah titik awal yang kuat. Mari diskusikan lebih lanjut bagaimana kami dapat membantu Anda dalam sesi **konsultasi gratis**."
        )
        whatsapp_number = "628114862525"
        whatsapp_message = "Halo, saya tertarik untuk konsultasi lebih lanjut mengenai hasil analisis kebutuhan dari aplikasi Anda."
        whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={whatsapp_message.replace(' ', '%20')}"
        st.link_button("💬 Hubungi Kami via WhatsApp", whatsapp_url)

if __name__ == "__main__":
    run_app()

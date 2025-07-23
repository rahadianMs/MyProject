# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit v4.1: Akinator Konsultan dengan Machine Learning (Stabil & Cerdas)
Fokus: Rekomendasi yang relevan, bebas error, dan berbasis pada pola kompleks.
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
# DATABASE LAYANAN & PERTANYAAN
# =============================================================================
SERVICES = {
    "Sustainability Roadmap & Action Plan": "Menyusun peta jalan keberlanjutan dengan langkah konkret sesuai kapasitas organisasi.",
    "GSTC Sustainable Tourism Course (STC)": "Pelatihan standar GSTC untuk praktik pariwisata berkelanjutan dengan sertifikasi resmi.",
    "Customized In-House Training (CIHT)": "Pelatihan khusus sesuai kebutuhan organisasi di bidang pariwisata dan keberlanjutan.",
    "Sustainability Performance Dashboard": "Dashboard visual memantau kinerja keberlanjutan untuk pengambilan keputusan cepat.",
    "Sustainability Certification Assistance": "Pendampingan lengkap proses sertifikasi keberlanjutan hingga implementasi perbaikan.",
    "ESG & Sustainability Reporting": "Membantu organisasi menyusun laporan ESG sesuai standar global dan strategi bisnis.",
    "Integrated Marketing Strategy": "Strategi pemasaran terpadu berbasis data untuk menjangkau audiens tepat dengan efektif.",
    "Customer Experience Feedback Analysis": "Evaluasi kualitas layanan via mystery shopper dan ulasan digital untuk peningkatan bisnis.",
    "Tourism Impact and Carrying Capacity Assessment": "Mengukur dampak pariwisata dan kapasitas destinasi demi kelestarian jangka panjang.",
    # ... (Tambahkan layanan lain jika ada)
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
    Melatih model Machine Learning menggunakan data sintetis yang lebih cerdas.
    """
    num_samples = 2500
    synthetic_answers = [{key: np.random.choice(q_data["options"]) for key, q_data in QUESTIONS.items()} for _ in range(num_samples)]
    X_df = pd.DataFrame(synthetic_answers)

    # Membuat label 'ground truth' dengan aturan yang lebih kompleks dan relevan
    y_labels = []
    for _, row in X_df.iterrows():
        scores = {service: 0 for service in SERVICES}
        
        # Aturan Kombinasi Cerdas
        if "Baru Memulai" in row["q2_tahap"]:
            scores["Sustainability Roadmap & Action Plan"] += 5
            if "Tim belum memiliki pemahaman" in row["q5_tantangan"]:
                scores["GSTC Sustainable Tourism Course (STC)"] += 4
                scores["Customized In-House Training (CIHT)"] += 3
            if "roadmap" in row["q4_tujuan"]:
                scores["Sustainability Action Plan Workshop"] += 4

        if "Sudah Berjalan" in row["q2_tahap"]:
            scores["Sustainability Performance Dashboard"] += 5
            if "Kesulitan melacak data" in row["q5_tantangan"]:
                 scores["Sustainability Performance Dashboard"] += 3
            if "branding" in row["q4_tujuan"]:
                scores["Integrated Marketing Strategy"] += 4

        if "Tingkat Lanjut" in row["q2_tahap"]:
            scores["Sustainability Certification Assistance"] += 5
            if "Tuntutan dari investor" in row["q5_tantangan"] or "laporan ESG" in row["q4_tujuan"]:
                scores["ESG & Sustainability Reporting"] += 5
        
        if "menjual" in row["q5_tantangan"] and "reputasi online" in row["q7_pemasaran"]:
             scores["Integrated Marketing Strategy"] += 5
             scores["Customer Experience Feedback Analysis"] += 3
             
        if "mewah & korporat" in row["q6_pasar"] and "sertifikasi" in row["q4_tujuan"]:
            scores["Sustainability Certification Assistance"] += 4

        # Konversi skor menjadi label biner (0 atau 1)
        # Layanan direkomendasikan jika skornya cukup tinggi
        labels = {service: 1 if score >= 4 else 0 for service, score in scores.items()}
        y_labels.append(labels)
    y_df = pd.DataFrame(y_labels)

    preprocessor = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    X_processed = preprocessor.fit_transform(X_df)

    forest = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model = MultiOutputClassifier(estimator=forest)
    model.fit(X_processed, y_df)
    
    return model, preprocessor

# =============================================================================
# ANTARMUKA PENGGUNA (TAMPILAN STREAMLIT)
# =============================================================================

def run_app():
    """Menjalankan seluruh alur aplikasi Streamlit."""
    
    model, preprocessor = train_model()
    
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnhT0JDtx12DjHca05hurtVr0QkmP4eNbsDw&s",
        use_container_width=True
    )
    st.title("Temukan Solusi Tepat Untuk Bisnis Anda")
    st.markdown("Hanya dalam **2 menit**, jawab 8 pertanyaan ini dan biarkan **AI** kami menganalisis kebutuhan Anda.")
    st.divider()

    with st.form("solution_finder_form"):
        answers = {key: st.selectbox(q_data["question"], options=q_data["options"], key=key) for key, q_data in QUESTIONS.items()}
        submitted = st.form_submit_button("ANALISIS & TEMUKAN SOLUSI SAYA", type="primary", use_container_width=True)

    if submitted:
        with st.spinner("Model AI sedang menganalisis pola dari jawaban Anda..."):
            user_input_df = pd.DataFrame([answers])
            user_input_processed = preprocessor.transform(user_input_df)

            # Prediksi probabilitas
            prediction_proba = model.predict_proba(user_input_processed)
            
            # --- PERBAIKAN BUG INDEXERROR DI SINI ---
            recommendation_scores = {}
            for i, service_name in enumerate(SERVICES.keys()):
                prob_array = prediction_proba[i]
                # Cek apakah model bisa memprediksi kelas 1 (Yes)
                if 1 in model.estimators_[i].classes_:
                    # Temukan indeks dari kelas 1
                    class_1_index = np.where(model.estimators_[i].classes_ == 1)[0][0]
                    # Ambil probabilitasnya
                    prob = prob_array[0, class_1_index]
                else:
                    # Jika kelas 1 tidak pernah terlihat saat training, probabilitasnya 0
                    prob = 0.0
                recommendation_scores[service_name] = prob

        st.success("Analisis Selesai! Berikut adalah rekomendasi berbasis AI untuk Anda.")
        st.balloons()

        sorted_recommendations = sorted(recommendation_scores.items(), key=lambda item: item[1], reverse=True)
        
        primary_rec_name, primary_rec_score = sorted_recommendations[0]
        supporting_recs = [(name, score) for name, score in sorted_recommendations[1:] if score > 0.30]
        
        st.header("⭐ Rekomendasi Utama Untuk Anda")
        with st.container(border=True):
            st.subheader(f"{primary_rec_name}")
            st.write(SERVICES[primary_rec_name])

        if supporting_recs:
            st.header("💡 Solusi Pendukung yang Relevan")
            for service_name, score in supporting_recs[:2]:
                with st.container(border=True):
                    st.subheader(f"{service_name}")
                    st.write(SERVICES[service_name])
        
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

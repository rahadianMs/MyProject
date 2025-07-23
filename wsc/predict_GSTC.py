# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit v5.2: Final Stable Release
Perbaikan: Mengatasi TypeError dengan memisahkan UI (pertanyaan) dari logika model.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from io import BytesIO

# =============================================================================
# KONFIGURASI APLIKASI
# =============================================================================
st.set_page_config(
    page_title="Analisis Kebutuhan Berbasis AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# DATABASE PENGETAHUAN (PERTANYAAN & LAYANAN)
# Ini adalah "resep" atau "script" yang akan ditampilkan ke pengguna.
# =============================================================================

QUESTIONS = {
    'Q1_Visi': {"question": "Apa visi utama yang ingin Anda wujudkan dalam 2-3 tahun ke depan?", "options": ['Menjadi pemimpin pasar', 'Menciptakan destinasi ikonik', 'Diakui sebagai bisnis berkelanjutan', 'Memiliki operasional efisien & profitabel', 'Memberikan dampak sosial-ekonomi']},
    'Q2_Dorongan': {"question": "Dari mana Anda merasakan dorongan terbesar untuk berubah saat ini?", "options": ['Investor/Kantor Pusat', 'Klien Korporat/Mitra Internasional', 'Perubahan Perilaku Pasar/Konsumen', 'Inisiatif Internal', 'Regulasi Pemerintah/Isu Lokal']},
    'Q3_Tahap': {"question": "Seberapa terstruktur program keberlanjutan Anda saat ini?", "options": ['Belum ada sama sekali', 'Sporadis, belum terukur', 'Cukup terstruktur', 'Sangat matang']},
    'Q4_PemahamanTim': {"question": "Bagaimana tingkat pemahaman dan keterlibatan tim Anda terkait keberlanjutan?", "options": ['Rendah', 'Sedang', 'Tinggi']},
    'Q5_TantanganData': {"question": "Jika berbicara tentang 'data', apa tantangan terbesar Anda?", "options": ['Sulit mengumpulkan data operasional', 'Sulit memahami data pasar', 'Sulit menyajikan laporan', 'Sulit justifikasi proyek baru', 'Tidak punya data sama sekali']},
    'Q6_KekhawatiranFinansial': {"question": "Dalam hal keuangan, apa yang paling mengkhawatirkan Anda?", "options": ['Biaya operasional meningkat', 'Risiko investasi proyek baru', 'Pemasaran kurang efektif', 'Sulit menunjukkan ROI keberlanjutan']},
    'Q7_PeningkatanPemasaran': {"question": "Dari sisi pemasaran dan brand, apa yang paling ingin Anda tingkatkan?", "options": ['Diferensiasi dari kompetitor', 'Meningkatkan reputasi online', 'Menjual cerita keberlanjutan', 'Menjangkau segmen pasar baru']},
    'Q8_Audiens': {"question": "Siapa audiens utama yang ingin Anda pengaruhi dengan tindakan Anda?", "options": ['Pelanggan/Tamu', 'Investor/Dewan Direksi', 'Komunitas Lokal/Pemerintah', 'Karyawan/Tim Internal']},
    'Q9_Aset': {"question": "Jenis aset apa yang paling menonjol dari bisnis Anda?", "options": ['Aset Fisik & Alam', 'Aset Tak Berwujud (Brand, reputasi)', 'Aset Manusia & Komunitas']},
    'Q10_Skala': {"question": "Gambarkan skala operasi Anda saat ini.", "options": ['Mikro/Kecil', 'Menengah', 'Besar/Korporat']}
}

SERVICES = {
    "Tourism Master Plan & Destination Development": "Pendampingan rencana pengembangan destinasi berbasis potensi lokal dan tren pasar.", "Feasibility Study & Financial Projection": "Analisis kelayakan pasar, operasional, dan finansial untuk memastikan proyek wisata realistis.", "Sustainability Roadmap & Action Plan": "Menyusun peta jalan keberlanjutan dengan langkah konkret sesuai kapasitas organisasi.",
    "ESG & Sustainability Reporting": "Membantu organisasi menyusun laporan ESG sesuai standar global dan strategi bisnis.", "Sustainability Performance Dashboard": "Dashboard visual memantau kinerja keberlanjutan untuk pengambilan keputusan cepat.", "Sustainability Certification Assistance": "Pendampingan lengkap proses sertifikasi keberlanjutan hingga implementasi perbaikan.", "Event Planning": "Merancang event bermakna dan berkelanjutan dari konsep hingga pelaksanaan teknis.",
    "Integrated Marketing Strategy": "Strategi pemasaran terpadu berbasis data untuk menjangkau audiens tepat dengan efektif.", "Tourism Impact and Carrying Capacity Assessment": "Mengukur dampak pariwisata dan kapasitas destinasi demi kelestarian jangka panjang.", "Customer Experience Feedback Analysis": "Evaluasi kualitas layanan via mystery shopper dan ulasan digital untuk peningkatan bisnis.",
    "Tourist Behaviour and Perception Analysis": "Memahami motivasi, ekspektasi, dan persepsi wisatawan untuk desain pengalaman optimal.", "Market Demand Analysis": "Analisis mendalam perilaku dan preferensi wisatawan untuk strategi pemasaran efektif.", "Tourism Assets Mapping": "Inventarisasi dan pemetaan aset wisata untuk perencanaan dan promosi berbasis data.", "Event Impact Measurement": "Analisis dampak ekonomi, sosial, lingkungan, dan brand dari penyelenggaraan event.",
    "Competitor Intelligence": "Pemetaan pesaing dan rekomendasi strategi diferensiasi bisnis pariwisata.", "GSTC Sustainable Tourism Course (STC)": "Pelatihan standar GSTC untuk praktik pariwisata berkelanjutan dengan sertifikasi resmi.", "Sustainability Action Plan Workshop": "Workshop kolaboratif menyusun rencana aksi keberlanjutan yang terukur dan realistis.", "Customized In-House Training (CIHT)": "Pelatihan khusus sesuai kebutuhan organisasi di bidang pariwisata dan keberlanjutan."
}

# =============================================================================
# FUNGSI PEMUATAN MODEL (OVEN AI)
# =============================================================================

@st.cache_resource
def load_model_from_github():
    """Mengunduh dan memuat file model .joblib dari URL mentah GitHub."""
    MODEL_URL = "https://raw.githubusercontent.com/rahadianMs/MyProject/main/wsc/recommendation_model.joblib"
    
    try:
        with st.spinner("Mengunduh dan menyiapkan model AI... Harap tunggu sebentar."):
            response = requests.get(MODEL_URL)
            response.raise_for_status()
            model_file = BytesIO(response.content)
            artifacts = joblib.load(model_file)
        return artifacts
    except Exception as e:
        st.error(f"Gagal memuat model. Pastikan URL Raw di kode benar dan file model ada di GitHub. Error: {e}")
        return None

# =============================================================================
# ANTARMUKA PENGGUNA (TAMPILAN STREAMLIT)
# =============================================================================

def run_app():
    """Menjalankan seluruh alur aplikasi Streamlit."""

    artifacts = load_model_from_github()
    if artifacts is None: return

    model = artifacts['model']
    encoder = artifacts['encoder']
    labels = artifacts['labels']
    
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnhT0JDtx12DjHca05hurtVr0QkmP4eNbsDw&s", use_container_width=True)
    st.title("Temukan Solusi Tepat Untuk Bisnis Anda")
    st.markdown("Hanya dalam **2 menit**, jawab 10 pertanyaan ini dan biarkan **AI** kami menganalisis kebutuhan Anda.")
    st.divider()

    with st.form("prediction_form"):
        user_answers = {}
        # --- PERBAIKAN DARI TYPEERROR ADA DI SINI ---
        # Kita sekarang me-loop melalui kamus QUESTIONS, bukan dari file model.
        for key, q_data in QUESTIONS.items():
            user_answers[key] = st.selectbox(q_data['question'], options=q_data['options'], key=key)
        
        submitted = st.form_submit_button("ANALISIS & DAPATKAN REKOMENDASI", type="primary", use_container_width=True)

    if submitted:
        with st.spinner("Model AI sedang memproses jawaban Anda..."):
            input_df = pd.DataFrame([user_answers])
            input_processed = encoder.transform(input_df)
            prediction = model.predict(input_processed)[0]

        st.success("Analisis Selesai!")
        st.balloons()
        
        st.header("✅ Rekomendasi Layanan Untuk Anda:")
        recommended_services = [service for service, is_recommended in zip(labels, prediction) if is_recommended == 1]
        
        if recommended_services:
            for service in recommended_services:
                # Menambahkan border untuk tampilan yang lebih rapi
                with st.container(border=True):
                    st.success(f"**{service}**")
                    # Menampilkan deskripsi layanan di bawah namanya
                    if service in SERVICES:
                        st.write(SERVICES[service])
        else:
            st.warning("Berdasarkan jawaban Anda, model tidak menemukan rekomendasi yang sangat cocok saat ini. Coba ubah beberapa jawaban Anda untuk eksplorasi, atau hubungi kami untuk diskusi lebih lanjut.")
            
        st.divider()
        st.header("Siap Mengambil Langkah Berikutnya?")
        st.markdown(
            "Rekomendasi di atas adalah titik awal yang kuat. Mari diskusikan lebih lanjut bagaimana kami dapat membantu Anda dalam sesi **konsultasi gratis**."
        )
        whatsapp_number = "628114862525"
        whatsapp_message = "Halo, saya tertarik untuk konsultasi lebih lanjut mengenai hasil analisis kebutuhan dari aplikasi AI Anda."
        whatsapp_url = f"https.api.whatsapp.com/send?phone={whatsapp_number}&text={whatsapp_message.replace(' ', '%20')}"
        st.link_button("💬 Hubungi Kami via WhatsApp", whatsapp_url)

if __name__ == "__main__":
    run_app()

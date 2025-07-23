# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit v5.1: Aplikasi Prediksi dengan Model Pre-trained (URL Fix)
Tujuan: Memuat model dari URL Raw GitHub yang benar dan menggunakannya untuk prediksi.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests # Untuk mengunduh model dari GitHub
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
# FUNGSI PEMUATAN MODEL DARI GITHUB
# =============================================================================

@st.cache_resource
def load_model_from_github():
    """
    Mengunduh dan memuat file model .joblib dari URL mentah GitHub.
    Fungsi ini hanya dijalankan sekali berkat cache.
    """
    # --- PERBAIKAN PALING PENTING ADA DI SINI ---
    # URL ini telah diubah menjadi URL "Raw" yang benar, yang menunjuk langsung ke file.
    MODEL_URL = "https://raw.githubusercontent.com/rahadianMs/MyProject/main/wsc/recommendation_model.joblib"
    # Catatan: Jika Anda menggunakan Git LFS, URL yang benar mungkin adalah:
    # MODEL_URL = "https://media.githubusercontent.com/media/rahadianMs/MyProject/main/wsc/recommendation_model.joblib"
    # Coba URL pertama dulu, jika masih gagal, ganti dengan URL kedua.
    
    try:
        with st.spinner("Mengunduh dan menyiapkan model AI... Harap tunggu sebentar."):
            response = requests.get(MODEL_URL)
            response.raise_for_status()  # Cek jika ada error saat mengunduh
            
            # Memuat model dari konten biner
            model_file = BytesIO(response.content)
            artifacts = joblib.load(model_file)
        
        return artifacts
    except requests.exceptions.RequestException as e:
        st.error(f"Gagal mengunduh model dari GitHub: {e}")
        st.error(f"Pastikan URL ini benar dan dapat diakses: {MODEL_URL}")
        st.error("Pastikan repositori Anda bersifat 'Public' dan Anda menggunakan URL 'Raw'.")
        return None
    except Exception as e:
        # Menampilkan error yang lebih spesifik
        st.error(f"Gagal memuat file model. Kemungkinan file corrupt atau bukan file joblib yang valid. Detail: {e}")
        return None

# =============================================================================
# ANTARMUKA PENGGUNA (TAMPILAN STREAMLIT)
# =============================================================================

def run_app():
    """Menjalankan seluruh alur aplikasi Streamlit."""

    artifacts = load_model_from_github()

    if artifacts is None:
        st.error("Aplikasi tidak dapat berjalan karena model gagal dimuat. Silakan periksa URL di kode atau hubungi pengembang.")
        return

    model = artifacts['model']
    encoder = artifacts['encoder']
    labels = artifacts['labels']
    features_map = artifacts['features_map']
    
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnhT0JDtx12DjHca05hurtVr0QkmP4eNbsDw&s",
        use_container_width=True
    )
    st.title("Temukan Solusi Tepat Untuk Bisnis Anda")
    st.markdown("Hanya dalam **2 menit**, jawab 10 pertanyaan ini dan biarkan **AI** kami menganalisis kebutuhan Anda.")
    st.divider()

    with st.form("prediction_form"):
        user_answers = {}
        for key, q_data in features_map.items():
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
                st.success(f"**{service}**")
        else:
            st.warning("Berdasarkan jawaban Anda, model tidak menemukan rekomendasi yang sangat cocok saat ini. Coba ubah beberapa jawaban Anda untuk eksplorasi.")
            
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

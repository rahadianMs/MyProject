# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit v5.0: Aplikasi Prediksi dengan Model Pre-trained
Tujuan: Memuat model dari GitHub dan menggunakannya untuk prediksi real-time.
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
    # PENTING: Ganti URL ini dengan URL mentah file .joblib Anda di GitHub
    # Cara mendapatkan URL mentah: Buka file di GitHub > Klik tombol "Raw" > Salin URL dari browser
    MODEL_URL = "https://media.githubusercontent.com/media/USERNAME/NAMA_REPO/main/recommendation_model.joblib"
    
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
        st.error("Pastikan Anda menggunakan Git LFS dan URL yang benar adalah URL 'Raw'.")
        return None
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None

# =============================================================================
# ANTARMUKA PENGGUNA (TAMPILAN STREAMLIT)
# =============================================================================

def run_app():
    """Menjalankan seluruh alur aplikasi Streamlit."""

    # Muat artefak (model, encoder, dll.)
    artifacts = load_model_from_github()

    # Jika model gagal dimuat, hentikan aplikasi
    if artifacts is None:
        return

    # Ekstrak komponen dari artefak
    model = artifacts['model']
    encoder = artifacts['encoder']
    labels = artifacts['labels']
    features_map = artifacts['features_map']
    
    # Tampilan utama
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
            # 1. Ubah input pengguna menjadi DataFrame
            input_df = pd.DataFrame([user_answers])
            
            # 2. Transformasi input menggunakan encoder yang sudah dilatih
            input_processed = encoder.transform(input_df)
            
            # 3. Lakukan prediksi
            prediction = model.predict(input_processed)[0]

        st.success("Analisis Selesai!")
        st.balloons()
        
        # 4. Tampilkan hasil
        st.header("✅ Rekomendasi Layanan Untuk Anda:")
        recommended_services = [service for service, is_recommended in zip(labels, prediction) if is_recommended == 1]
        
        if recommended_services:
            for service in recommended_services:
                st.success(f"**{service}**")
        else:
            st.warning("Berdasarkan jawaban Anda, model tidak menemukan rekomendasi yang sangat cocok saat ini. Coba ubah beberapa jawaban Anda untuk eksplorasi.")
            
        # Call to Action
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

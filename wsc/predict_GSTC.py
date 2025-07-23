# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit: Laboratorium Pelatihan & Uji Coba Model Rekomendasi
Versi: 1.0
Tujuan: Melatih, mengevaluasi, dan mencoba model ML secara interaktif.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score, classification_report

# =============================================================================
# KONFIGURASI APLIKASI & DATABASE PENGETAHUAN
# =============================================================================
st.set_page_config(
    page_title="Lab Pelatihan Model Rekomendasi",
    layout="wide",
    initial_sidebar_state="expanded"
)

# "Kamus" ini sangat penting untuk menerjemahkan angka di dataset menjadi teks yang bisa dibaca
FEATURES_MAP = {
    'Q1_Visi': ['Menjadi pemimpin pasar', 'Menciptakan destinasi ikonik', 'Diakui sebagai bisnis berkelanjutan', 'Memiliki operasional efisien & profitabel', 'Memberikan dampak sosial-ekonomi'],
    'Q2_Dorongan': ['Investor/Kantor Pusat', 'Klien Korporat/Mitra Internasional', 'Perubahan Perilaku Pasar/Konsumen', 'Inisiatif Internal', 'Regulasi Pemerintah/Isu Lokal'],
    'Q3_Tahap': ['Belum ada sama sekali', 'Sporadis, belum terukur', 'Cukup terstruktur', 'Sangat matang'],
    'Q4_PemahamanTim': ['Rendah', 'Sedang', 'Tinggi'],
    'Q5_TantanganData': ['Sulit mengumpulkan data operasional', 'Sulit memahami data pasar', 'Sulit menyajikan laporan', 'Sulit justifikasi proyek baru', 'Tidak punya data sama sekali'],
    'Q6_KekhawatiranFinansial': ['Biaya operasional meningkat', 'Risiko investasi proyek baru', 'Pemasaran kurang efektif', 'Sulit menunjukkan ROI keberlanjutan'],
    'Q7_PeningkatanPemasaran': ['Diferensiasi dari kompetitor', 'Meningkatkan reputasi online', 'Menjual cerita keberlanjutan', 'Menjangkau segmen pasar baru'],
    'Q8_Audiens': ['Pelanggan/Tamu', 'Investor/Dewan Direksi', 'Komunitas Lokal/Pemerintah', 'Karyawan/Tim Internal'],
    'Q9_Aset': ['Aset Fisik & Alam', 'Aset Tak Berwujud (Brand, reputasi)', 'Aset Manusia & Komunitas'],
    'Q10_Skala': ['Mikro/Kecil', 'Menengah', 'Besar/Korporat']
}

LABELS_LIST = [
    "Tourism Master Plan & Destination Development", "Feasibility Study & Financial Projection", "Sustainability Roadmap & Action Plan",
    "ESG & Sustainability Reporting", "Sustainability Performance Dashboard", "Sustainability Certification Assistance", "Event Planning",
    "Integrated Marketing Strategy", "Tourism Impact and Carrying Capacity Assessment", "Customer Experience Feedback Analysis",
    "Tourist Behaviour and Perception Analysis", "Market Demand Analysis", "Tourism Assets Mapping", "Event Impact Measurement",
    "Competitor Intelligence", "GSTC Sustainable Tourism Course (STC)", "Sustainability Action Plan Workshop", "Customized In-House Training (CIHT)"
]

# =============================================================================
# FUNGSI-FUNGSI UTAMA
# =============================================================================

@st.cache_data
def load_data(uploaded_file):
    """Memuat data dari file CSV yang diunggah."""
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error memuat file: {e}")
            return None
    return None

def train_and_evaluate(df):
    """Fungsi untuk melatih model dan mengembalikan model, akurasi, dan laporan."""
    X = df[FEATURES_MAP.keys()]
    y = df[LABELS_LIST]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # Menggunakan RandomForest yang kuat, dibungkus MultiOutputClassifier untuk multi-label
    forest = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model = MultiOutputClassifier(estimator=forest)
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Hitung metrik
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=LABELS_LIST, zero_division=0)

    return model, accuracy, report

# =============================================================================
# TAMPILAN APLIKASI STREAMLIT
# =============================================================================

st.title("🧪 Lab Pelatihan Model Rekomendasi")
st.markdown("Unggah dataset Anda, latih model, evaluasi kinerjanya, dan coba langsung secara interaktif.")

# --- Langkah 1: Unggah Dataset ---
st.header("Langkah 1: Unggah Dataset Sintetis Anda")
uploaded_file = st.file_uploader(
    "Pilih file `synthetic_consultant_dataset.csv`",
    type="csv"
)

# Simpan model dan status di session_state agar tidak hilang
if 'model_trained' not in st.session_state:
    st.session_state.model_trained = False

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.success("Dataset berhasil dimuat!")
    with st.expander("Lihat 5 baris pertama dari dataset"):
        st.dataframe(df.head())

    # --- Langkah 2: Latih Model ---
    st.header("Langkah 2: Latih & Evaluasi Model")
    if st.button("Latih Model Machine Learning Sekarang", type="primary"):
        with st.spinner("Model sedang dilatih... Ini mungkin memakan waktu beberapa saat."):
            model, accuracy, report = train_and_evaluate(df)
            st.session_state.model = model
            st.session_state.accuracy = accuracy
            st.session_state.report = report
            st.session_state.model_trained = True
        
        st.success("Model berhasil dilatih!")

    # Tampilkan hasil jika model sudah dilatih
    if st.session_state.model_trained:
        st.subheader("Hasil Evaluasi Model")
        st.metric(label="Akurasi Model (Subset Accuracy)", value=f"{st.session_state.accuracy:.2%}")
        st.info("Subset Accuracy mengukur persentase prediksi di mana SEMUA label untuk satu sampel benar. Ini adalah metrik yang sangat ketat.")
        
        with st.expander("Lihat Laporan Klasifikasi Rinci (Precision, Recall, F1-Score)"):
            st.text_area("Laporan:", st.session_state.report, height=400)

    # --- Langkah 3: Playground Model ---
    st.header("Langkah 3: Coba Model (Playground)")
    if st.session_state.model_trained:
        st.markdown("Jawab pertanyaan di bawah ini untuk mendapatkan rekomendasi dari model AI yang baru saja Anda latih.")
        
        with st.form("playground_form"):
            user_answers = {}
            for key, q_data in FEATURES_MAP.items():
                user_answers[key] = st.selectbox(q_data['question'], options=q_data['options'], key=key)
            
            predict_button = st.form_submit_button("Dapatkan Rekomendasi AI")

        if predict_button:
            # Ubah jawaban teks menjadi angka (indeks)
            numeric_answers = [FEATURES_MAP[key].index(answer) for key, answer in user_answers.items()]
            
            # Buat DataFrame untuk input model
            input_df = pd.DataFrame([numeric_answers], columns=FEATURES_MAP.keys())
            
            # Lakukan prediksi
            with st.spinner("AI sedang memproses jawaban Anda..."):
                prediction = st.session_state.model.predict(input_df)[0]
            
            # Tampilkan hasil
            st.subheader("✅ Rekomendasi Layanan Untuk Anda:")
            recommended_services = [service for service, is_recommended in zip(LABELS_LIST, prediction) if is_recommended == 1]
            
            if recommended_services:
                for service in recommended_services:
                    st.success(f"**{service}**")
            else:
                st.warning("Berdasarkan jawaban Anda, model tidak menemukan rekomendasi layanan yang sangat cocok saat ini. Coba ubah beberapa jawaban Anda.")
    else:
        st.warning("Harap latih model terlebih dahulu untuk menggunakan playground ini.")

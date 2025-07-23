# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit v6.0: Expert System dengan Penyimpanan Prospek ke Google Sheets
"""
import streamlit as st
import gspread
from datetime import datetime
import pandas as pd

# =============================================================================
# KONFIGURASI APLIKASI
# =============================================================================
st.set_page_config(page_title="Wise Steps | Analisis Kebutuhan", layout="centered")

# =============================================================================
# KONEKSI KE GOOGLE SHEETS (MENGGUNAKAN STREAMLIT SECRETS)
# =============================================================================
@st.cache_resource
def connect_to_sheet():
    """Menghubungkan ke Google Sheet menggunakan kredensial dari st.secrets."""
    try:
        # Menggunakan kunci dari st.secrets yang sudah Anda konfigurasikan
        creds = st.secrets["gcp_service_account"]
        sa = gspread.service_account_from_dict(creds)
        # Buka spreadsheet berdasarkan namanya. Pastikan nama ini sama persis.
        sh = sa.open("Database Prospek Klien") 
        # Buka worksheet (tab) pertama.
        worksheet = sh.get_worksheet(0)
        return worksheet
    except Exception as e:
        st.error(f"Gagal terhubung ke Google Sheets. Pastikan 'secrets.toml' sudah benar. Error: {e}")
        return None

# =============================================================================
# DATABASE LAYANAN & PERTANYAAN (TETAP SAMA)
# =============================================================================
# (Saya singkat di sini untuk kejelasan, gunakan daftar lengkap Anda)
SERVICES = {"Tourism Master Plan & Destination Development": "...", "Feasibility Study & Financial Projection": "...", "Sustainability Roadmap & Action Plan": "...", "ESG & Sustainability Reporting": "...", "Sustainability Performance Dashboard": "...", "Sustainability Certification Assistance": "...", "Event Planning": "...", "Integrated Marketing Strategy": "...", "Tourism Impact and Carrying Capacity Assessment": "...", "Customer Experience Feedback Analysis": "...", "Tourist Behaviour and Perception Analysis": "...", "Market Demand Analysis": "...", "Tourism Assets Mapping": "...", "Event Impact Measurement": "...", "Competitor Intelligence": "...", "GSTC Sustainable Tourism Course (STC)": "...", "Sustainability Action Plan Workshop": "...", "Customized In-House Training (CIHT)": "..."}
QUESTIONS = {"q1_visi": {"question": "...", "options": [...]}, "q2_dorongan": {"question": "...", "options": [...]}, "q3_tahap_keberlanjutan": {"question": "...", "options": [...]}, "q4_kapasitas_tim": {"question": "...", "options": [...]}, "q5_data": {"question": "...", "options": [...]}, "q6_keuangan": {"question": "...", "options": [...]}, "q7_pemasaran": {"question": "...", "options": [...]}, "q8_audiens": {"question": "...", "options": [...]}, "q9_aset": {"question": "...", "options": [...]}, "q10_skala": {"question": "...", "options": [...]}}

# =============================================================================
# LOGIKA REKOMENDASI (TETAP SAMA)
# =============================================================================
def get_recommendations(answers):
    scores = {service: 0 for service in SERVICES}
    # (Logika skoring Anda yang sudah ada ditempatkan di sini)
    if "pemimpin pasar" in answers["q1_visi"]: scores["Integrated Marketing Strategy"] += 10; scores["Competitor Intelligence"] += 8
    if "destinasi" in answers["q1_visi"]: scores["Tourism Master Plan & Destination Development"] += 10; scores["Tourism Assets Mapping"] += 7
    # ...dan seterusnya...
    
    relevant_scores = {k: v for k, v in scores.items() if v > 0}
    if not relevant_scores: return ["Sustainability Roadmap & Action Plan"], []
    sorted_services = sorted(relevant_scores.items(), key=lambda item: item[1], reverse=True)
    primary_recommendation = sorted_services[0][0]
    supporting_recommendations = [s[0] for s in sorted_services[1:3]]
    return [primary_recommendation], supporting_recommendations

# =============================================================================
# ANTARMUKA PENGGUNA DENGAN FITUR BARU
# =============================================================================
def run_app():
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnhT0JDtx12DjHca05hurtVr0QkmP4eNbsDw&s", use_container_width=True)
    st.title("Temukan Solusi Tepat Untuk Bisnis Anda")
    st.markdown("Jawab 10 pertanyaan ini untuk mendapatkan rekomendasi layanan yang dipersonalisasi.")
    
    # Inisialisasi session state untuk menyimpan data antar render
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
        st.session_state.answers = {}
        st.session_state.recommendations = []
        st.session_state.checked_solutions = []

    with st.form("solution_finder_form"):
        answers = {key: st.selectbox(q_data["question"], options=q_data["options"], key=key) for key, q_data in QUESTIONS.items()}
        submitted = st.form_submit_button("ANALISIS & TEMUKAN SOLUSI SAYA", type="primary", use_container_width=True)

        if submitted:
            st.session_state.submitted = True
            st.session_state.answers = answers
            primary_rec, supporting_recs = get_recommendations(answers)
            st.session_state.recommendations = primary_rec + supporting_recs

    if st.session_state.submitted:
        st.success("Analisis Selesai! Berikut adalah solusi yang paling relevan untuk Anda.")
        
        st.header("Pilih Solusi yang Paling Menarik Untuk Anda:")
        
        checked_solutions = []
        # Tampilkan rekomendasi dengan checkbox
        for service_name in st.session_state.recommendations:
            is_checked = st.checkbox(f"**{service_name}**", value=True)
            if is_checked:
                checked_solutions.append(service_name)
            st.caption(SERVICES[service_name])
            st.divider()
        
        st.session_state.checked_solutions = checked_solutions
        
        # Tombol untuk menyimpan ke spreadsheet
        if st.button("Simpan Minat Saya & Hubungi Konsultan", type="primary", use_container_width=True):
            worksheet = connect_to_sheet()
            if worksheet:
                with st.spinner("Menyimpan data Anda..."):
                    # Siapkan data untuk baris baru
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # Gabungkan semua jawaban menjadi satu string
                    all_answers_str = " | ".join(st.session_state.answers.values())
                    # Gabungkan solusi yang dicentang
                    checked_solutions_str = ", ".join(st.session_state.checked_solutions)
                    
                    # Header (pastikan sama dengan header di GSheet Anda)
                    header = ["Timestamp", "Jawaban Kuesioner", "Solusi yang Dipilih"]
                    
                    # Data baris baru
                    new_row = [timestamp, all_answers_str, checked_solutions_str]
                    
                    # Cek apakah header sudah ada
                    if worksheet.get("A1").first() != "Timestamp":
                         worksheet.append_row(header, value_input_option='USER_ENTERED')
                    
                    # Tambahkan baris baru
                    worksheet.append_row(new_row, value_input_option='USER_ENTERED')
                    
                st.success("Terima kasih! Data minat Anda telah kami terima. Tim kami akan segera menghubungi Anda.")
                # Tambahkan link WhatsApp sebagai konfirmasi akhir
                whatsapp_number = "628114862525"
                whatsapp_message = "Halo, saya baru saja menyimpan minat saya dari aplikasi analisis kebutuhan dan ingin berdiskusi lebih lanjut."
                whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={whatsapp_message.replace(' ', '%20')}"
                st.markdown(f"[Atau, Anda bisa langsung menghubungi kami via WhatsApp di sini]({whatsapp_url})")

if __name__ == "__main__":
    # Salin-tempel deskripsi lengkap ke dalam kamus SERVICES dan QUESTIONS sebelum menjalankan
    # Contoh: SERVICES["Tourism Master Plan & Destination Development"] = "Pendampingan rencana pengembangan..."
    run_app()

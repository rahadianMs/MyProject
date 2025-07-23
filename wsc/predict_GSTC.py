# -*- coding: utf-8 -*-
"""
Fokus: Memberikan 1 rekomendasi utama + solusi relevan lainnya.
"""

import streamlit as st
import time

# =============================================================================
# KONFIGURASI APLIKASI
# =============================================================================
st.set_page_config(
    page_title="Analisis Kebutuhan Keberlanjutan",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# DATABASE LAYANAN & PERTANYAAN
# =============================================================================

# Kamus (dictionary) yang berisi semua layanan yang Anda tawarkan
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

# Pertanyaan diagnostik yang diperbarui (Total 8 Pertanyaan)
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
# LOGIKA ANALISIS (OTAK DARI APLIKASI)
# =============================================================================

def get_recommendations(answers):
    """
    Menganalisis jawaban dan memberikan rekomendasi utama + solusi pendukung.
    """
    scores = {service: 0 for service in SERVICES}

    # Aturan Skoring Berdasarkan Jawaban
    if "Baru Memulai" in answers["q2_tahap"]:
        scores["Sustainability Roadmap & Action Plan"] += 5
        scores["Sustainability Action Plan Workshop"] += 3
        scores["GSTC Sustainable Tourism Course (STC)"] += 2
    elif "Sudah Berjalan" in answers["q2_tahap"]:
        scores["Sustainability Performance Dashboard"] += 5
        scores["Sustainability Roadmap & Action Plan"] += 2
    elif "Tingkat Lanjut" in answers["q2_tahap"]:
        scores["Sustainability Certification Assistance"] += 5
        scores["ESG & Sustainability Reporting"] += 4

    if "roadmap" in answers["q4_tujuan"]: scores["Sustainability Roadmap & Action Plan"] += 5
    if "kapasitas tim" in answers["q4_tujuan"]:
        scores["Customized In-House Training (CIHT)"] += 5
        scores["GSTC Sustainable Tourism Course (STC)"] += 3
    if "Mengukur & memonitor" in answers["q4_tujuan"]: scores["Sustainability Performance Dashboard"] += 5
    if "sertifikasi" in answers["q4_tujuan"]: scores["Sustainability Certification Assistance"] += 5
    if "branding" in answers["q4_tujuan"]: scores["Integrated Marketing Strategy"] += 5
    if "laporan ESG" in answers["q4_tujuan"]: scores["ESG & Sustainability Reporting"] += 5

    if "Biaya operasional" in answers["q5_tantangan"]: scores["Feasibility Study & Financial Projection"] += 2
    if "Kesulitan melacak data" in answers["q5_tantangan"]: scores["Sustainability Performance Dashboard"] += 3
    if "Tuntutan dari investor" in answers["q5_tantangan"]: scores["ESG & Sustainability Reporting"] += 3
    if "Tim belum memiliki pemahaman" in answers["q5_tantangan"]:
        scores["GSTC Sustainable Tourism Course (STC)"] += 3
        scores["Customized In-House Training (CIHT)"] += 2
    if "menjual" in answers["q5_tantangan"]:
        scores["Integrated Marketing Strategy"] += 3
        scores["Customer Experience Feedback Analysis"] += 2
    
    if "pemandangan alam" in answers["q3_aset"]: scores["Tourism Impact and Carrying Capacity Assessment"] += 2
    if "layanan personal" in answers["q3_aset"]: scores["Customer Experience Feedback Analysis"] += 2
    
    if "loyalitas tamu" in answers["q7_pemasaran"]: scores["Customer Experience Feedback Analysis"] += 3
    if "reputasi online" in answers["q7_pemasaran"]:
        scores["Integrated Marketing Strategy"] += 2
        scores["Customer Experience Feedback Analysis"] += 2

    relevant_scores = {k: v for k, v in scores.items() if v > 0}
    
    if not relevant_scores:
        return ["Sustainability Roadmap & Action Plan"], []

    sorted_services = sorted(relevant_scores.items(), key=lambda item: item[1], reverse=True)
    
    primary_recommendation = sorted_services[0][0]
    supporting_recommendations = [s[0] for s in sorted_services[1:3]]
    
    return [primary_recommendation], supporting_recommendations

# =============================================================================
# ANTARMUKA PENGGUNA (TAMPILAN STREAMLIT)
# =============================================================================

def run_app():
    """Menjalankan seluruh alur aplikasi Streamlit."""
    
    # KODE YANG DIPERBAIKI ADA DI SINI:
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnhT0JDtx12DjHca05hurtVr0QkmP4eNbsDw&s",
        use_container_width=True # Menggunakan parameter baru yang benar
    )
    
    st.title("Temukan Solusi Tepat Untuk Bisnis Anda")
    st.markdown("Hanya dalam **2 menit**, jawab 8 pertanyaan ini untuk mendapatkan **rekomendasi layanan yang dipersonalisasi**.")
    st.divider()

    with st.form("solution_finder_form"):
        answers = {}
        for key, q_data in QUESTIONS.items():
            answers[key] = st.selectbox(q_data["question"], options=q_data["options"], key=key)
        
        submitted = st.form_submit_button("ANALISIS & TEMUKAN SOLUSI SAYA", type="primary", use_container_width=True)

    if submitted:
        with st.spinner("Menganalisis kebutuhan Anda..."):
            time.sleep(1.5)
            primary_rec, supporting_recs = get_recommendations(answers)
        
        st.success("Analisis Selesai! Berikut adalah solusi yang paling relevan untuk Anda.")
        st.balloons()
        
        st.header("⭐ Rekomendasi Utama Untuk Anda")
        primary_service_name = primary_rec[0]
        with st.container(border=True):
            st.subheader(f"{primary_service_name}")
            st.write(SERVICES[primary_service_name])

        if supporting_recs:
            st.header("💡 Solusi Pendukung yang Relevan")
            for service_name in supporting_recs:
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

# =============================================================================
# JALANKAN APLIKASI
# =============================================================================

if __name__ == "__main__":
    run_app()

# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit v5.1: Expert System Consultant
Model: Menerjemahkan product knowledge mendalam menjadi rekomendasi AI yang relevan dan akurat.
"""

import streamlit as st
import time

# =============================================================================
# KONFIGURASI APLIKASI
# =============================================================================
st.set_page_config(
    page_title="Wise Steps Consulting | Analisis Kebutuhan",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# KNOWLEDGE BASE: DATABASE LAYANAN & PERTANYAAN
# Ini adalah "otak" dari konsultan. Semua detail produk dan pertanyaan ada di sini.
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
    "Market Demand Analysis": "Analisis mendalam perilaku dan preferensi wisatawan untuk strategi pemasaran efektif.",
    "Tourism Assets Mapping": "Inventarisasi dan pemetaan aset wisata untuk perencanaan dan promosi berbasis data.",
    "Event Impact Measurement": "Analisis dampak ekonomi, sosial, lingkungan, dan brand dari penyelenggaraan event.",
    "Competitor Intelligence": "Pemetaan pesaing dan rekomendasi strategi diferensiasi bisnis pariwisata.",
    "GSTC Sustainable Tourism Course (STC)": "Pelatihan standar GSTC untuk praktik pariwisata berkelanjutan dengan sertifikasi resmi.",
    "Sustainability Action Plan Workshop": "Workshop kolaboratif menyusun rencana aksi keberlanjutan yang terukur dan realistis.",
    "Customized In-House Training (CIHT)": "Pelatihan khusus sesuai kebutuhan organisasi di bidang pariwisata dan keberlanjutan."
}

QUESTIONS = {
    "q1_visi": {"question": "Apa visi utama yang ingin Anda wujudkan dalam 2-3 tahun ke depan?", "options": ["Menjadi pemimpin pasar (market leader) di wilayah kami.", "Menciptakan sebuah destinasi atau kawasan wisata yang ikonik.", "Diakui secara global sebagai bisnis yang bertanggung jawab dan berkelanjutan.", "Memiliki operasional yang sangat efisien dan profitabel.", "Memberikan dampak sosial-ekonomi yang signifikan bagi komunitas lokal."]},
    "q2_dorongan": {"question": "Dari mana Anda merasakan dorongan terbesar untuk berubah saat ini?", "options": ["Tekanan dari Investor atau Kantor Pusat.", "Permintaan dari Klien Korporat atau Mitra Internasional.", "Perubahan Perilaku Pasar/Konsumen.", "Inisiatif Internal dari Manajemen atau Tim.", "Regulasi Pemerintah atau Isu Lokal."]},
    "q3_tahap_keberlanjutan": {"question": "Seberapa terstruktur program keberlanjutan Anda saat ini?", "options": ["Belum ada sama sekali; kami mencari titik awal.", "Sporadis; kami melakukan beberapa hal baik, tapi tidak terukur.", "Cukup terstruktur; kami punya program tapi ingin optimasi & pelaporan.", "Sangat matang; kami ingin mengukur dampak jangka panjangnya."]},
    "q4_kapasitas_tim": {"question": "Bagaimana tingkat pemahaman dan keterlibatan tim Anda terkait keberlanjutan?", "options": ["Rendah; banyak yang belum paham konsep dasarnya.", "Sedang; sebagian paham, tapi perlu penyelarasan dan keterampilan praktis.", "Tinggi; tim sudah paham, tapi kami butuh panduan untuk implementasi tingkat lanjut."]},
    "q5_data": {"question": "Jika berbicara tentang 'data', apa tantangan terbesar Anda?", "options": ["Sulit mengumpulkan data operasional (konsumsi energi, air, limbah).", "Sulit memahami data pasar dan perilaku pelanggan.", "Sulit menyajikan data menjadi laporan yang mudah dipahami stakeholder.", "Sulit mendapatkan data untuk justifikasi proyek baru (kelayakan finansial).", "Kami tidak punya data sama sekali untuk memulai perencanaan."]},
    "q6_keuangan": {"question": "Dalam hal keuangan, apa yang paling mengkhawatirkan Anda?", "options": ["Biaya operasional yang terus meningkat.", "Risiko investasi pada proyek baru yang belum teruji.", "Alokasi budget pemasaran yang terasa kurang efektif.", "Kesulitan menunjukkan ROI dari program keberlanjutan."]},
    "q7_pemasaran": {"question": "Dari sisi pemasaran dan brand, apa yang paling ingin Anda tingkatkan?", "options": ["Diferensiasi; kami ingin tampil beda dari kompetitor.", "Reputasi; kami ingin meningkatkan ulasan positif dan citra online.", "Komunikasi; kami ingin 'menjual' cerita keberlanjutan kami dengan lebih baik.", "Jangkauan; kami ingin menjangkau segmen pasar baru yang potensial."]},
    "q8_audiens": {"question": "Siapa audiens utama yang ingin Anda pengaruhi dengan tindakan Anda?", "options": ["Pelanggan/Tamu.", "Investor/Dewan Direksi.", "Komunitas Lokal/Pemerintah.", "Karyawan/Tim Internal."]},
    "q9_aset": {"question": "Jenis aset apa yang paling menonjol dari bisnis Anda?", "options": ["Aset Fisik & Alam (Lokasi, bangunan, bentang alam).", "Aset Tak Berwujud (Brand, reputasi, budaya layanan).", "Aset Manusia & Komunitas (Tim yang solid, hubungan baik dengan masyarakat)."]},
    "q10_skala": {"question": "Gambarkan skala operasi Anda saat ini.", "options": ["Skala Mikro/Kecil (Operasi sederhana, sumber daya terbatas).", "Skala Menengah (Struktur mulai kompleks, butuh sistematisasi).", "Skala Besar/Korporat (Operasi kompleks, standar tinggi)."]}
}

# =============================================================================
# INFERENCE ENGINE: LOGIKA REKOMENDASI "EXPERT SYSTEM"
# =============================================================================
def get_recommendations(answers):
    """Menganalisis jawaban untuk memberikan rekomendasi yang paling relevan."""
    scores = {service: 0 for service in SERVICES}

    # --- Logika Pemberian Skor Berdasarkan Jawaban ---
    # Aturan dibuat berdasarkan pemahaman mendalam terhadap setiap layanan.

    # Pertanyaan 1: Visi Utama
    if "pemimpin pasar" in answers["q1_visi"]:
        scores["Integrated Marketing Strategy"] += 10
        scores["Competitor Intelligence"] += 8
    elif "destinasi" in answers["q1_visi"]:
        scores["Tourism Master Plan & Destination Development"] += 10
        scores["Tourism Assets Mapping"] += 7
    elif "Diakui secara global" in answers["q1_visi"]:
        scores["Sustainability Certification Assistance"] += 10
        scores["ESG & Sustainability Reporting"] += 8
    elif "efisien dan profitabel" in answers["q1_visi"]:
        scores["Feasibility Study & Financial Projection"] += 8
        scores["Sustainability Performance Dashboard"] += 7
    elif "dampak sosial" in answers["q1_visi"]:
        scores["Tourism Impact and Carrying Capacity Assessment"] += 9

    # Pertanyaan 3 & 4: Kesiapan Internal
    if "Belum ada sama sekali" in answers["q3_tahap_keberlanjutan"]:
        scores["Sustainability Roadmap & Action Plan"] += 7
    if "Rendah" in answers["q4_kapasitas_tim"]:
        scores["GSTC Sustainable Tourism Course (STC)"] += 7
        scores["Sustainability Action Plan Workshop"] += 5
    elif "Sedang" in answers["q4_kapasitas_tim"]:
        scores["Customized In-House Training (CIHT)"] += 6
    
    # Pertanyaan 5: Tantangan Data
    if "Sulit mengumpulkan data" in answers["q5_data"]:
        scores["Sustainability Performance Dashboard"] += 8
    elif "Sulit memahami data pasar" in answers["q5_data"]:
        scores["Market Demand Analysis"] += 8
        scores["Tourist Behaviour and Perception Analysis"] += 7
    elif "Sulit menyajikan data" in answers["q5_data"]:
        scores["ESG & Sustainability Reporting"] += 8
    elif "justifikasi proyek" in answers["q5_data"]:
        scores["Feasibility Study & Financial Projection"] += 8
    elif "tidak punya data sama sekali" in answers["q5_data"]:
        scores["Tourism Assets Mapping"] += 6
    
    # Pertanyaan 6: Kekhawatiran Finansial
    if "Biaya operasional" in answers["q6_keuangan"]:
        scores["Sustainability Roadmap & Action Plan"] += 5
    if "Risiko investasi" in answers["q6_keuangan"]:
        scores["Feasibility Study & Financial Projection"] += 10
    if "pemasaran" in answers["q6_keuangan"]:
        scores["Integrated Marketing Strategy"] += 7

    # Pertanyaan 7: Peningkatan Pemasaran
    if "Diferensiasi" in answers["q7_pemasaran"]:
        scores["Competitor Intelligence"] += 8
    if "Reputasi" in answers["q7_pemasaran"]:
        scores["Customer Experience Feedback Analysis"] += 8
    if "Komunikasi" in answers["q7_pemasaran"]:
        scores["Integrated Marketing Strategy"] += 7

    # Pertanyaan 2 & 8: Pengaruh Eksternal & Audiens
    if "Investor" in answers["q2_dorongan"] or "Investor" in answers["q8_audiens"]:
        scores["ESG & Sustainability Reporting"] += 6
    if "Klien Korporat" in answers["q2_dorongan"]:
        scores["Sustainability Certification Assistance"] += 6
    if "Pemerintah" in answers["q2_dorongan"] or "Pemerintah" in answers["q8_audiens"]:
        scores["Tourism Master Plan & Destination Development"] += 5

    # --- Filter dan Urutkan Rekomendasi ---
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
    
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnhT0JDtx12DjHca05hurtVr0QkmP4eNbsDw&s", use_container_width=True)
    st.title("Temukan Solusi Tepat Untuk Bisnis Anda")
    st.markdown("Jawab 10 pertanyaan ini dan biarkan **Sistem Pakar** kami menganalisis kebutuhan Anda secara akurat.")
    st.divider()

    with st.form("solution_finder_form"):
        answers = {key: st.selectbox(q_data["question"], options=q_data["options"], key=key) for key, q_data in QUESTIONS.items()}
        submitted = st.form_submit_button("ANALISIS & TEMUKAN SOLUSI SAYA", type="primary", use_container_width=True)

    if submitted:
        with st.spinner("Menganalisis jawaban Anda berdasarkan Knowledge Base kami..."):
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
        st.markdown("Rekomendasi di atas adalah titik awal yang kuat. Mari diskusikan lebih lanjut bagaimana kami dapat membantu Anda dalam sesi **konsultasi gratis**.")
        whatsapp_number = "628114862525"
        whatsapp_message = "Halo, saya tertarik untuk konsultasi lebih lanjut mengenai hasil analisis kebutuhan dari aplikasi Anda."
        whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={whatsapp_message.replace(' ', '%20')}"
        st.link_button("💬 Hubungi Kami via WhatsApp", whatsapp_url)

if __name__ == "__main__":
    run_app()

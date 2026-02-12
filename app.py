import streamlit as st
import pandas as pd
import joblib

# --- KONFIGURASI & TEMA ---
st.set_page_config(
    page_title="Jaya Jaya Institut - Check Drop Out", 
    layout="wide", 
    page_icon="🎓"
)

@st.cache_resource
def load_model():
    return joblib.load("Models/model_student_dropout.pkl")

model = load_model()

# --- MAPPING DATA (Agar Input Lebih Mudah) ---
course_dict = {
    33: "Biofuel Production Technologies(33)",
    171: "Animation and Multimedia Design(171)",
    8014: "Social Service - evening attendance(8014)",
    9003: "Agronomy(9003)",
    9070: "Communication Design(9070)",
    9085: "Veterinary Nursing(9085)",
    9119: "Informatics Engineering(9119)",
    9130: "Equinculture(9130)",
    9147: "Management(9147)",
    9238: "Social Service(9238)",
    9254: "Tourism(9254)",
    9500: "Nursing(9500)",
    9556: "Oral Hygiene(9556)",
    9670: "Advertising and Marketing Management(9670)",
    9773: "Journalism and Communication(9773)",
    9853: "Basic Education(9853)",
    9991: "Management - evening attendance (9991)"
}

app_mode_dict = {
    1: "1st phase - general contingent (1)",
    2: "Ordinance No. 612/93 (2)",
    5: "1st phase - special contingent (Azores Island) (5)",
    7: "Holders of other higher courses (7)",
    10: "Ordinance No. 854-B/99 (10)",
    15: "International student (bachelor) (15)",
    16: "1st phase - special contingent (Madeira Island) (16)",
    17: "2nd phase - general contingent (17)",
    18: "3rd phase - general contingent (18)",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan) (26)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution) (27)",
    39: "Over 23 years old (39)",
    42: "Transfer (42)",
    43: "Change of course (43)",
    44: "Technological specialization diploma holders (44)",
    51: "Change of institution/course (51)",
    53: "Short cycle diploma holders (53)",
    57: "Change of institution/course (International) (57)" 
}

prev_qual_dict = {
    1: "Secondary education (1)",
    2: "Higher education - bachelor's degree (2)",
    3: "Higher education - degree (3)",
    4: "Higher education - master's (4)",
    5: "Higher education - doctorate (5)",
    6: "Frequency of higher education (6)",
    9: "12th year of schooling - not completed (9)",
    10: "11th year of schooling - not completed (10)",
    12: "Other - 11th year of schooling (12)",
    14: "10th year of schooling (14)",
    15: "10th year of schooling - not completed (15)",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv. (19)",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv. (38)",
    39: "Technological specialization course (39)",
    40: "Higher education - degree (1st cycle) (40)",
    42: "Professional higher technical course (42)",
    43: "Higher education - master (2nd cycle) (43)"
}

mother_occup_dict = {
    0: "Student (0)",
    1: "Legislative Power/Executive Bodies, Directors, Managers (1)",
    2: "Specialists in Intellectual and Scientific Activities (2)",
    3: "Intermediate Level Technicians and Professions (3)",
    4: "Administrative staff (4)",
    5: "Personal Services, Security and Safety Workers and Sellers (5)",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry (6)",
    7: "Skilled Workers in Industry, Construction and Craftsmen (7)",
    8: "Installation and Machine Operators and Assembly Workers (8)",
    9: "Unskilled Workers (9)",
    10: "Armed Forces Professions (10)",
    90: "Other Situation (90)",
    99: "(blank) (99)",
    122: "Health professionals (122)",
    123: "Teachers (123)",
    125: "Specialists in ICT (125)",
    131: "Intermediate level science and engineering technicians (131)",
    132: "Technicians and professionals, intermediate level of health (132)",
    134: "Intermediate level technicians from legal, social, sports, cultural (134)",
    141: "Office workers, secretaries and data processing operators (141)",
    143: "Data, accounting, statistical, financial and registry operators (143)",
    144: "Other administrative support staff (144)",
    151: "Personal service workers (151)",
    152: "Sellers (152)",
    153: "Personal care workers and the like (153)",
    171: "Skilled construction workers (except electricians) (171)",
    173: "Skilled workers in printing, precision instruments, jewelers (173)",
    175: "Workers in food processing, woodworking, clothing (175)",
    191: "Cleaning workers (191)",
    192: "Unskilled workers in agriculture, animal production, fisheries (192)",
    193: "Unskilled workers in extractive industry, construction, transport (193)",
    194: "Meal preparation assistants (194)"
}

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3413/3413535.png", width=100)
    st.title("Sistem Prediksi")
    st.info("Aplikasi ini membantu institusi mendeteksi risiko dropout mahasiswa lebih awal.")
    st.divider()
    st.caption("Dikembangkan untuk Jaya Jaya Institut") 

# --- HEADER ---
st.title("🎓 Student Success Predictor")
st.write("Silakan isi data mahasiswa di bawah ini untuk memprediksi status akademik.")
st.divider()

# --- INPUT FORM DENGAN TABS ---
tab1, tab2, tab3 = st.tabs(["👤 Data Pribadi", "📚 Riwayat Akademik", "📈 Progress Semester"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        Gender = st.selectbox("Jenis Kelamin", [0, 1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
        Age_at_enrollment = st.number_input("Usia saat Daftar", 17, 60, 20)
        Displaced = st.selectbox("Pindahan (Displaced)?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
    with col2:
        Scholarship_holder = st.selectbox("Penerima Beasiswa?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        Debtor = st.selectbox("Punya Hutang?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        Tuition_fees_up_to_date = st.selectbox("SPP Lunas?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
    
    GDP = st.number_input("GDP (Kondisi Ekonomi Wilayah)", -5.0, 5.0, 0.0)

with tab2:
    Course = st.selectbox("Program Studi", options=list(course_dict.keys()), format_func=lambda x: course_dict[x])
    Application_mode = st.selectbox("Mode Pendaftaran", options=list(app_mode_dict.keys()), format_func=lambda x: app_mode_dict[x])
    Previous_qualification = st.selectbox("ID Kualifikasi Sebelumnya (1-20)", options=list(prev_qual_dict.keys()), format_func=lambda x: prev_qual_dict[x])
    Previous_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 120.0)
    Admission_grade = st.number_input("Nilai Penerimaan (Admission)", 0.0, 200.0, 120.0)
    Mothers_occupation = st.selectbox("Pekerjaan Ibu (ID)", options=list(mother_occup_dict.keys()), format_func=lambda x: mother_occup_dict[x])

with tab3:
    st.info("Masukkan nilai rata-rata dari Semester 1 & 2")
    c1, c2 = st.columns(2)
    with c1:
        Curricular_units_credited_avg = st.number_input("Unit Dikreditkan (Avg)", 0.0, 20.0, 0.0)
        Curricular_units_enrolled_avg = st.number_input("Unit Terdaftar (Avg)", 0.0, 25.0, 6.0)
        Curricular_units_evaluations_avg = st.number_input("Unit Evaluasi (Avg)", 0.0, 25.0, 6.0)
    with c2:
        Curricular_units_approved_avg = st.number_input("Unit Lulus (Avg)", 0.0, 25.0, 5.0)
        Curricular_units_grade_avg = st.number_input("IPK (Avg)", 0.0, 20.0, 12.0)
        Curricular_units_without_evaluations_avg = st.number_input("Unit Tanpa Evaluasi (Avg)", 0.0, 10.0, 0.0)

# --- PROSES PREDIKSI ---
if st.button("🚀 Analisis Status Mahasiswa", use_container_width=True):
    input_data = pd.DataFrame([{
        'Age_at_enrollment': Age_at_enrollment, 'Previous_qualification_grade': Previous_qualification_grade,
        'Admission_grade': Admission_grade, 'GDP': GDP,
        'Curricular_units_credited_avg': Curricular_units_credited_avg, 'Curricular_units_enrolled_avg': Curricular_units_enrolled_avg,
        'Curricular_units_evaluations_avg': Curricular_units_evaluations_avg, 'Curricular_units_approved_avg': Curricular_units_approved_avg,
        'Curricular_units_grade_avg': Curricular_units_grade_avg, 'Curricular_units_without_evaluations_avg': Curricular_units_without_evaluations_avg,
        'Gender': Gender, 'Application_mode': Application_mode, 'Course': Course,
        'Previous_qualification': Previous_qualification, 'Mothers_occupation': Mothers_occupation,
        'Displaced': Displaced, 'Debtor': Debtor, 'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
        'Scholarship_holder': Scholarship_holder
    }])
    numerical_features = [
        'Age_at_enrollment', 'Previous_qualification_grade', 'Admission_grade', 'GDP',
        'Curricular_units_credited_avg', 'Curricular_units_enrolled_avg',
        'Curricular_units_evaluations_avg', 'Curricular_units_approved_avg',
        'Curricular_units_grade_avg', 'Curricular_units_without_evaluations_avg'
    ]
    categorical_features = [
        'Gender', 'Application_mode', 'Course', 
        'Previous_qualification', 'Mothers_occupation', 
        'Displaced', 'Debtor', 'Tuition_fees_up_to_date', 'Scholarship_holder'
    ]
    input_data[numerical_features] = input_data[numerical_features].astype(float)
    input_data[categorical_features] = input_data[categorical_features].astype(int)
    prediction = model.predict(input_data)[0]
    
    labels = ["Dropout", "Enrolled", "Graduate"]
    result = labels[prediction]

    st.subheader("🏁 Hasil Analisis")
    res_col1, res_col2, res_col3 = st.columns(3)
    with res_col2:
        if result == "Graduate":
            st.metric(label="Status Mahasiswa", value=result, delta="Aman", delta_color="normal")
            st.success("Target Terpenuhi: Mahasiswa diprediksi lulus.")
        elif result == "Dropout":
            st.metric(label="Status Mahasiswa", value=result, delta="Berisiko", delta_color="inverse")
            st.error("Peringatan: Mahasiswa memerlukan bimbingan khusus.")
        else:
            st.metric(label="Status Mahasiswa", value=result)
            st.warning("Perhatian: Status mahasiswa saat ini aktif/enrolled.")

# --- TAMBAHAN: ANALISIS ALASAN PREDIKSI ---
    st.divider()
    col_chart, col_insight = st.columns([2, 1])
    importances = model.named_steps['xgb'].feature_importances_
    feature_names = numerical_features + categorical_features
    
    # 2. Buat DataFrame untuk visualisasi
    feat_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    feat_importances = feat_importances.sort_values(by='Importance', ascending=False).head(5)

    with col_chart:
        st.write("📊 **Fitur Paling Berpengaruh dalam Prediksi Ini:**")
        st.bar_chart(feat_importances.set_index('Feature'), horizontal=True)

    with col_insight:
        st.write("💡 **Rekomendasi Strategis:**")
        top_f = feat_importances.iloc[0]['Feature']
        st.write(f"Faktor **{top_f}** adalah pendorong utama hasil ini.")
        st.write("Disarankan untuk meninjau kembali performa mahasiswa pada area tersebut.")
        
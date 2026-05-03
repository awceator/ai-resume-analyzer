import streamlit as st
from utils import *
from report import generate_pdf
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Analyzer Pro", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main-title {
    font-size:42px;
    font-weight:800;
    color:#2E86C1;
}
.card {
    padding:20px;
    border-radius:15px;
    background:linear-gradient(135deg,#f5f7fa,#c3cfe2);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🚀 AI Resume Analyzer PRO</p>', unsafe_allow_html=True)

# ---------- INPUT ----------
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("📄 Upload Resume")

with col2:
    jd_text = st.text_area("🧾 Paste Job Description")

# ---------- ANALYZE ----------
if st.button("Analyze Resume"):

    if resume_file and jd_text:

        resume_text = extract_text(resume_file)
        resume_clean = preprocess(resume_text)
        jd_clean = preprocess(jd_text)

        skills = extract_skills(resume_clean)
        similarity = match_resume_jd(resume_clean, jd_clean)
        ats = ats_score(similarity, skills)
        suggestions = generate_suggestions(resume_clean, jd_clean)

        # ---------- METRICS ----------
        st.subheader("📊 Dashboard")

        c1, c2, c3 = st.columns(3)
        c1.metric("🎯 JD Match", f"{similarity}%")
        c2.metric("📈 ATS Score", f"{ats}%")
        c3.metric("🧠 Skills Found", len(skills))

        st.progress(int(ats))

        # ---------- SKILL GAP CHART ----------
        st.subheader("📉 Skill Gap Analysis")

        jd_skills = [s for s in SKILLS_DB if s in jd_clean]
        missing_skills = list(set(jd_skills) - set(skills))

        labels = ["Matched Skills", "Missing Skills"]
        values = [len(skills), len(missing_skills)]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        st.pyplot(fig)

        # ---------- SKILLS ----------
        st.subheader("🧠 Skills Found")
        st.write(skills)

        # ---------- SUGGESTIONS ----------
        st.subheader("💡 Suggestions")
        for s in suggestions:
            st.write(s)

        # ---------- PDF DOWNLOAD ----------
        pdf_path = generate_pdf(ats, skills, suggestions)

        with open(pdf_path, "rb") as f:
            st.download_button(
                "📥 Download Report",
                f,
                file_name="ATS_Report.pdf"
            )

    else:
        st.warning("⚠ Upload resume and enter job description")


# # import streamlit as st
# # from utils import *

# # st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# # st.title("📄 AI Resume Analyzer")

# # st.write("Upload your resume and paste job description to get ATS score")

# # uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
# # jd_text = st.text_area("Paste Job Description")

# # if uploaded_file and jd_text:
    
# #     # Extract text
# #     if uploaded_file.name.endswith(".pdf"):
# #         resume_text = extract_text_from_pdf(uploaded_file)
# #     else:
# #         resume_text = extract_text_from_docx(uploaded_file)
    
# #     clean_resume = preprocess(resume_text)
# #     clean_jd = preprocess(jd_text)
    
# #     # Analysis
# #     skills = extract_skills(clean_resume)
# #     similarity = match_resume_jd(clean_resume, clean_jd)
# #     ats = ats_score(similarity, skills)
# #     suggestions = generate_suggestions(clean_resume, clean_jd)
    
# #     # Output
# #     st.subheader("📊 Results")
    
# #     st.metric("ATS Score", f"{ats}%")
# #     st.write("### 🔍 Matching Score:", similarity, "%")
    
# #     st.write("### 🧠 Skills Found:")
# #     st.write(skills)
    
# #     st.write("### ⚠️ Suggestions:")
# #     for s in suggestions:
# #         st.write("-", s)

# import streamlit as st
# from utils import *

# st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# # --------- CUSTOM CSS ---------
# st.markdown("""
# <style>
# .big-title {
#     font-size:40px;
#     font-weight:700;
#     color:#4CAF50;
# }
# .card {
#     padding:20px;
#     border-radius:15px;
#     background-color:#f5f5f5;
#     box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
# }
# </style>
# """, unsafe_allow_html=True)

# # --------- HEADER ---------
# st.markdown('<p class="big-title">🚀 AI Resume Analyzer</p>', unsafe_allow_html=True)
# st.write("Upload your resume and compare it with a Job Description")

# # --------- INPUT SECTION ---------
# col1, col2 = st.columns(2)

# with col1:
#     resume_file = st.file_uploader("📄 Upload Resume (PDF/DOCX)")

# with col2:
#     jd_text = st.text_area("🧾 Paste Job Description")

# # --------- PROCESS ---------
# if st.button("Analyze Resume"):

#     if resume_file and jd_text:

#         resume_text = extract_text(resume_file)

#         resume_clean = preprocess(resume_text)
#         jd_clean = preprocess(jd_text)

#         skills = extract_skills(resume_clean)
#         similarity = match_resume_jd(resume_clean, jd_clean)
#         ats = ats_score(similarity, skills)
#         suggestions = generate_suggestions(resume_clean, jd_clean)

#         # --------- RESULTS ---------
#         st.subheader("📊 Analysis Result")

#         col1, col2, col3 = st.columns(3)

#         col1.metric("🎯 JD Match", f"{similarity}%")
#         col2.metric("📈 ATS Score", f"{ats}%")
#         col3.metric("🛠 Skills Found", len(skills))

#         # --------- PROGRESS BAR ---------
#         st.progress(int(ats))

#         # --------- SKILLS ---------
#         st.markdown("### 🧠 Skills Detected")
#         st.write(", ".join(skills) if skills else "No skills found")

#         # --------- SUGGESTIONS ---------
#         st.markdown("### 💡 Suggestions")
#         if suggestions:
#             for s in suggestions:
#                 st.write(s)
#         else:
#             st.success("✅ Your resume is well optimized!")

#     else:
#         st.warning("⚠ Please upload resume and enter job description")
"""Streamlit GUI for Resume Screener"""

import streamlit as st
from screener import ResumeScreener

# Page configuration
st.set_page_config(
    page_title="Resume Screener",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .metric-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        text-align: center;
    }
    .score-excellent {
        color: #27ae60;
        font-size: 48px;
        font-weight: bold;
    }
    .score-good {
        color: #2980b9;
        font-size: 48px;
        font-weight: bold;
    }
    .score-moderate {
        color: #f39c12;
        font-size: 48px;
        font-weight: bold;
    }
    .score-weak {
        color: #e74c3c;
        font-size: 48px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title and header
st.title("📄 Resume Screener")
st.markdown("Compare a resume against a job description and get a matching score")

# Initialize session state
if 'screener' not in st.session_state:
    st.session_state.screener = ResumeScreener()

# Sidebar for model selection
with st.sidebar:
    st.header("⚙️ Settings")
    embedding_model = st.selectbox(
        "Embedding Model",
        ["all-MiniLM-L6-v2", "all-mpnet-base-v2", "sentence-t5-base"],
        help="Select the embedding model for text representation"
    )
    
    st.markdown("---")
    st.markdown("**How it works:**")
    st.markdown("""
    1. Paste or upload a Job Description
    2. Paste or upload a Resume
    3. Click 'Analyze' to get the match score
    """)

# Main content - two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Job Description")
    jd_input_type = st.radio("Input method", ["📝 Text", "📤 Upload"], key="jd_input", horizontal=True)
    
    if jd_input_type == "📝 Text":
        job_description = st.text_area(
            "Paste Job Description",
            height=300,
            placeholder="Paste the job description here...",
            key="jd_text"
        )
    else:
        uploaded_jd = st.file_uploader("Upload Job Description (TXT or PDF)", type=["txt", "pdf"], key="jd_file")
        if uploaded_jd:
            if uploaded_jd.type == "text/plain":
                job_description = uploaded_jd.read().decode("utf-8")
            else:
                job_description = f"[PDF file uploaded: {uploaded_jd.name}]\n\nPlease paste the text content."
                st.info("Please paste the PDF content as text in the text area on the left")
        else:
            job_description = ""

with col2:
    st.subheader("👤 Resume")
    resume_input_type = st.radio("Input method", ["📝 Text", "📤 Upload"], key="resume_input", horizontal=True)
    
    if resume_input_type == "📝 Text":
        resume = st.text_area(
            "Paste Resume",
            height=300,
            placeholder="Paste the resume here...",
            key="resume_text"
        )
    else:
        uploaded_resume = st.file_uploader("Upload Resume (TXT or PDF)", type=["txt", "pdf"], key="resume_file")
        if uploaded_resume:
            if uploaded_resume.type == "text/plain":
                resume = uploaded_resume.read().decode("utf-8")
            else:
                resume = f"[PDF file uploaded: {uploaded_resume.name}]\n\nPlease paste the text content."
                st.info("Please paste the PDF content as text in the text area on the left")
        else:
            resume = ""

# Analyze button
st.markdown("---")
analyze_col1, analyze_col2, analyze_col3 = st.columns([1, 1, 2])

with analyze_col1:
    analyze_button = st.button("🔍 Analyze", use_container_width=True, type="primary")

with analyze_col2:
    clear_button = st.button("🔄 Clear All", use_container_width=True)

if clear_button:
    st.rerun()

# Results section
if analyze_button:
    if not job_description.strip():
        st.error("❌ Please provide a Job Description")
    elif not resume.strip():
        st.error("❌ Please provide a Resume")
    else:
        with st.spinner("Analyzing resume against job description..."):
            try:
                # Get the match result
                result = st.session_state.screener.match_single_resume(resume, job_description)
                
                # Display results
                st.markdown("---")
                st.subheader("📊 Results")
                
                # Score display with color coding
                score = result["score"]
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("### Overall Match Score")
                    if score >= 85:
                        st.markdown(f'<div class="score-excellent">{score:.1f}%</div>', unsafe_allow_html=True)
                    elif score >= 70:
                        st.markdown(f'<div class="score-good">{score:.1f}%</div>', unsafe_allow_html=True)
                    elif score >= 50:
                        st.markdown(f'<div class="score-moderate">{score:.1f}%</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="score-weak">{score:.1f}%</div>', unsafe_allow_html=True)
                
                with col2:
                    st.metric("Cosine Similarity", f"{result['similarity']:.4f}")
                
                with col3:
                    st.metric("Match Status", result["explanation"])
                
                # Details tabs
                st.markdown("---")
                tab1, tab2, tab3 = st.tabs(["📈 Summary", "💼 Job Requirements", "🎯 Resume Skills"])
                
                with tab1:
                    st.write(f"**Job Title:** {result['job_title']}")
                    st.write(f"**Verdict:** {result['explanation']}")
                    
                    # Score interpretation
                    if score >= 85:
                        st.success("✅ Excellent match! Candidate is highly suitable for this position.")
                    elif score >= 70:
                        st.info("ℹ️ Good match. Candidate has most required qualifications.")
                    elif score >= 50:
                        st.warning("⚠️ Moderate match. Candidate has some relevant skills but gaps exist.")
                    else:
                        st.error("❌ Weak match. Candidate may not be suitable for this position.")
                
                with tab2:
                    if result["job_requirements"]:
                        st.write("**Extracted Job Requirements:**")
                        for req in result["job_requirements"][:10]:  # Show first 10
                            st.write(f"• {req}")
                    else:
                        st.info("No specific requirements extracted from job description")
                
                with tab3:
                    if result["resume_skills"]:
                        st.write("**Extracted Resume Skills:**")
                        for skill in result["resume_skills"][:10]:  # Show first 10
                            st.write(f"• {skill}")
                    else:
                        st.info("No specific skills extracted from resume")
                        
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
                st.info("Please check that your resume and job description are properly formatted.")

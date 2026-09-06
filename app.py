import streamlit as st
from pathlib import Path
from preprocessor import processor
from analyser import cvanalyser

#Demo files
DEMO_DIR = Path("demo")

#Page configuration
st.set_page_config(
    page_title='JobSifter',
    page_icon='🎯',
    layout='wide'
)

#Custom CSS
st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 2rem;
    }

    /* Header */
    .hero {
        text-align: center;
        padding: 1rem 0 2rem 0;
    }

    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 0.2rem;
    }

    .hero p {
        font-size: 1.2rem;
        opacity: 0.7;
    }

    /* Section headings */
    .section-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    /* Analyse button */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-size: 1.05rem;
        font-weight: 600;
    }

    /* Privacy note */
    .privacy {
        text-align: center;
        font-size: 0.85rem;
        opacity: 0.6;
        margin-top: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True)

#Header
st.markdown(
    """
    <div class="hero">
        <h1>🎯 JobSifter</h1>
        <p>Know before you apply.</p>
    </div>
    """,
    unsafe_allow_html=True)

#Introduction
st.write(
    'Upload your CV and paste a job description to see how well '
    'your experience matches the role.')

#Mode selection
mode = st.radio(
    "Choose mode",
    ["✨ Try the Demo", "🧪 Live Analysis"],
    horizontal=True)


st.divider()


#============================================================
#DEMO MODE
#============================================================

if mode == "✨ Try the Demo":

    st.info(
        "Demo mode uses a precomputed result. "
        "No API call is made."
    )

    # Load demo CV
    demo_cv = (DEMO_DIR / "demo_cv.txt").read_text(
        encoding="utf-8"
    )

    # Load demo job description
    demo_job = (DEMO_DIR / "demo_job.txt").read_text(
        encoding="utf-8"
    )

    # Input section
    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="section-title">📄 Demo CV</div>',
            unsafe_allow_html=True
        )

        st.text(demo_cv)

    with col2:

        st.markdown(
            '<div class="section-title">💼 Job Description</div>',
            unsafe_allow_html=True
        )

        st.text(demo_job)

    st.write("")

    # Demo analyse button
        # Demo analyse button
    analyse_clicked = st.button(
        "✨ Analyse Match",
        use_container_width=True
    )

    if analyse_clicked:
        # Load the saved LLM result
        demo_result = (DEMO_DIR / "demo_result.md").read_text(
            encoding="utf-8"
        )

        st.divider()
        st.subheader("🎯 JobSifter Assessment")

        with st.container(border=True):
            st.markdown(demo_result)

#============================================================
# LIVE ANALYSIS MODE
#============================================================

else:
    # Input section
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div class="section-title">📄 Your CV</div>',
            unsafe_allow_html=True
        )

        uploaded_cv = st.file_uploader(
            "Upload your CV",
            type=["pdf", "docx"],
            label_visibility="collapsed"
        )

        if uploaded_cv:
            st.success(f"Uploaded: {uploaded_cv.name}")

    with col2:
        st.markdown(
            '<div class="section-title">💼 Job Description</div>',
            unsafe_allow_html=True
        )

        job_description = st.text_area(
            "Paste the job description",
            height=220,
            placeholder="Paste the job description here...",
            label_visibility="collapsed"
        )

    st.write("")

    # Analyse button
    analyse_clicked = st.button(
        "✨ Analyse Match",
        use_container_width=True
    )

    # Analysis
    if analyse_clicked:
        if uploaded_cv is None:
            st.warning(
                "Please upload your CV."
            )

        elif not job_description.strip():
            st.warning(
                "Please paste the job description."
            )

        else:
            try:
                with st.spinner("Analysing your CV..."):

                    # Extract and redact CV text
                    cv_text = processor(uploaded_cv)

                    # Send CV + job description to Gemini
                    result = cvanalyser(
                        cv_text,
                        job_description
                    )

                st.divider()
                st.subheader("🎯 JobSifter Assessment")
                st.markdown(result)

            except Exception as e:
                st.error(
                    f"Something went wrong: {e}"
                )

#Privacy note
st.markdown(
    """
    <div class="privacy">
        🔒 Detected contact details such as email addresses,
        phone numbers and URLs are removed before analysis.
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st
from pathlib import Path

#Demo files
DEMO_DIR = Path('demo')

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
    unsafe_allow_html=True
)

#Header
st.markdown(
    """
    <div class="hero">
        <h1>🎯 JobSifter</h1>
        <p>Know before you apply.</p>
    </div>
    """,
    unsafe_allow_html=True
)

#Introduction
st.write(
    'Upload your CV (.pdf/.docx) and paste a job description to get your analysis!'
)

st.divider()

#Demo mode
st.info('Demo mode displays precomputed results. No API call is made.')

#Demo options
demo_options = {
    'DEMO 1 🟩': {
        'cv': 'green_cv.txt',
        'job': 'datasci_job.txt',
        'result': 'green_result.md'
    },
    'DEMO 2 🟨': {
        'cv': 'yellow_cv.txt',
        'job': 'yellow_job.txt',
        'result': 'yellow_result.md'
    },
    'DEMO 3 🟥': {
        'cv': 'red_cv.txt',
        'job': 'datasci_job.txt',
        'result': 'red_result.md'
    }
}

choose_demo = st.selectbox(
    'Choose a demo',
    options=list(demo_options.keys())
)

demo = demo_options[choose_demo]

#Load selected demo CV
demo_cv = (DEMO_DIR / demo['cv']).read_text(
    encoding="utf-8"
)

#Load selected job description
demo_job = (DEMO_DIR / demo["job"]).read_text(
    encoding="utf-8"
)

#Input section
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

st.write('')

#Demo analyse button
analyse_clicked = st.button(
    "✨ Analyse Match",
    use_container_width=True
)

if analyse_clicked:
    # Load the saved LLM result
    demo_result = (DEMO_DIR / demo['result']).read_text(
        encoding="utf-8"
    )

    st.divider()
    st.subheader('🎯 JobSifter Assessment')

    with st.container(border=True):
        st.markdown(demo_result)

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
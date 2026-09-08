# 🎯 JobSifter - Your friendly decision assistant!

### **Turn job descriptions into decisions.**

Do you spend hours reading lengthy job descriptions? Do you find yourself nitpicking every requirement against your CV, trying to figure out whether you're actually a good fit? Or struggle to decide whether an application is worth your time?

If you answered yes to any of these, **JobSifter might just be the tool for you!**

JobSifter is an **LLM-powered job application assistant** that analyses a candidate's CV against a job description and provides targeted application advice. It assesses the candidate's demonstrated skills and experience against the requirements of the role, highlighting strengths, gaps, and an overall recommendation.

**Rather than simply matching keywords**, JobSifter looks at the evidence in the candidate's CV and considers factors such as required and preferred requirements, relevant experience, transferable skills, and role seniority.

## Try the Demo!
👉 https://jobsifter-ai.streamlit.app/

Demo mode shows precomputed results. No API call is made.

## What it does

JobSifter takes:

* 📄 A candidate CV in PDF or DOCX format
* 💼 A job description

**It then:**

1. Extracts the text from the CV.
2. Redacts personal contact information such as email addresses, phone numbers and URLs.
3. Sends the processed CV and job description to an LLM.
4. Evaluates the candidate against the role requirements.
5. Produces a structured assessment containing:

   * **ADVICE:** One of three actionable labels:
      - 🟢 Go for it — Apply
      - 🟡 Worth a shot — Apply if interested
      - 🔴 Skip this one — Don't apply
   * **Why?:** Reasons for the assessment
   * **Strengths:** Relevant skills and experience demonstrated in the CV
   * **Gaps:** Important requirements with limited or missing evidence
   * **Recommendation:** Suggested next step for the candidate

The goal is to help candidates decide **which roles are worth prioritising before applying**.

## Project Pipeline

![Jobsifter pipeline](images/coding%20pipeline.jpg)

## Tech Stack

* **Python** — core programming language
* **Streamlit** — interactive web interface
* **Google Gemini API** — LLM-based CV and job analysis
* **pypdf** — PDF text extraction
* **python-docx** — DOCX text extraction
* **phonenumbers** — phone number detection and redaction
* **python-dotenv** — environment variable management
* **uv** — Python project and dependency management

## Project Structure

![Project Structure](images/coding%20pipeline%20-%20project%20arch.jpg)

## Demo Mode vs Live Analysis

JobSifter currently has two modes.

### ✨ Demo Mode

Publicly available demo mode which uses synthetic CV and job-description data and displays precomputed LLM assessment results. 

**No API request is made when using Demo Mode.**

This was designed to ensure that the deployed demonstration is safe to use without exposing an API key, generating uncontrolled API usage, or incurring unexpected costs.

### 🧪 Live Analysis

Live Analysis runs the complete pipeline:

```text
Uploaded CV
    ↓
Text extraction + redaction
    ↓
CV + job description
    ↓
Gemini
    ↓
Assessment
```

To test Live Analysis with your own CV and job description, run the application locally and provide your own Gemini API key. **Here's how you can do that!**

## Running Locally

### 1. Clone the repository

Clone the JobSifter repository to your local machine:

```bash
git clone <repository-url>
cd JobSifter
```

### 2. Install dependencies

This project uses `uv` for dependency management.

```bash
uv sync
```

### 3. Add your Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_KEY=your_api_key_here
```

The `.env` file is confidential and should **never be committed to GitHub**.

### 4. Start the application

```bash
uv run streamlit run app.py
```

The Streamlit application will open in your browser. You can then use Live Analysis with your own CV, job description, and Gemini API key.

The Streamlit application will open in your browser.

## Privacy

Before a CV is sent for analysis, JobSifter redacts:

* Email addresses
* Phone numbers
* URLs such as LinkedIn and GitHub profiles

This preprocessing reduces the amount of personally identifying information being passed to the LLM.

**Any other personal or sensitive information should be manually removed by the user before submitting the CV.**

## ⚠️ Challenges & Limitations

One of the challenges was creating a polished user interface while working within Streamlit's built-in components. I used custom HTML and CSS to improve the layout and visual design, with guidance from a friend and AI tools while learning how to implement these customisations.

Another challenge was designing prompts that encouraged the LLM to make grounded recommendations rather than simply matching keywords. Iterating on the system prompt helped make the assessment more focused on the evidence provided in the CV and job description.

### Limitations & Future Improvements

JobSifter is an experimental portfolio project and is intended as decision support, not HR or career advice.

The assessment depends on:
* The information present in the CV
* The wording and completeness of the job description
* The LLM's interpretation of the candidate's CV and job description

The current system has not been evaluated using a large, formally labelled dataset. Its behaviour was tested using a small set of synthetic CV and job-description examples, but a more rigorous evaluation would be a useful next step.

Future work could include both **qualitative and quantitative evaluation** using a larger and more diverse dataset, along with a clearly defined evaluation methodology.

## 💡 Why I Built JobSifter

I built JobSifter based on a problem I personally experienced while applying for jobs. I often found myself spending a lot of time going through lengthy job descriptions, trying to work out whether my background actually aligned with the role.

This was particularly challenging because I was **switching fields**. A job title alone wasn't always enough to tell me whether a role was relevant, and I found it difficult to judge how much weight to give to transferable skills, missing requirements, and differences in experience.

At the same time, after completing my degree, I became increasingly interested in LLM engineering and started exploring the field through online courses and hands-on projects. I wanted to move beyond simply learning concepts and see how I could apply those skills to build something practical and meaningful.

These two things came together in JobSifter. I wanted to build a tool that could help answer a simple question:

**“Is this job worth my time applying to?”**

This became the motivation behind JobSifter, an assistant designed to look beyond simple keyword matches and provide a practical, evidence-based assessment of whether applying for a role is worth considering.

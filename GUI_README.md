# Resume Screener GUI

A web-based GUI for scoring resumes against job descriptions using advanced NLP and semantic similarity.

## Features

- 📄 **Paste or Upload** Job Descriptions and Resumes
- 🎯 **Instant Scoring** with semantic matching
- 📊 **Color-coded Results** (Excellent/Good/Moderate/Weak)
- 💼 **Detailed Analysis** with extracted requirements and skills
- ⚙️ **Multiple Embedding Models** to choose from
- 🚀 **Fast Processing** using Sentence Transformers and FAISS

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the GUI:
```bash
streamlit run gui.py
```

The app will open in your default browser at `http://localhost:8501`

## How to Use

1. **Job Description**: Paste or upload the job description text
2. **Resume**: Paste or upload the resume text
3. **Click Analyze**: Get the matching score instantly
4. **View Results**: See detailed metrics and extracted information

## Score Interpretation

- **85-100%**: Excellent match - candidate is highly suitable
- **70-84%**: Good match - candidate has most required skills
- **50-69%**: Moderate match - candidate has some relevant skills
- **Below 50%**: Weak match - significant skill gaps exist

## Architecture

The GUI uses the `ResumeScreener` class which:
1. Parses both resume and job description
2. Generates embeddings using Sentence Transformers
3. Calculates cosine similarity between embeddings
4. Extracts and displays relevant skills and requirements
5. Provides interpretable scoring and feedback

## Supported Input Formats

- **Text**: Direct paste in the text areas
- **Files**: Upload `.txt` or `.pdf` files (PDF content must be converted to text)

## Customization

Edit `config.py` to change:
- Embedding model
- Default thresholds
- Output preferences

---

Created with ❤️ using Streamlit

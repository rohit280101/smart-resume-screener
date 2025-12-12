# Smart Resume Screener

A model that reads resumes and matches them to job descriptions using embeddings and similarity search with FAISS, providing candidate ranking and score explanations.

## Features

- **Resume Parsing**: Extract structured information from resumes
- **Job Description Matching**: Match resumes against job requirements
- **Similarity Search**: FAISS-based efficient similarity search
- **Candidate Ranking**: Rank candidates with scores
- **Explanation Scores**: Provide explanations for rankings
- **Batch Processing**: Process multiple resumes simultaneously

## Tech Stack

- Python
- FAISS (Facebook AI Similarity Search)
- Embeddings (Sentence Transformers)
- LLM Integration (Optional)
- Scikit-learn

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from screener import ResumeScreener

screener = ResumeScreener()
matches = screener.match_resumes('resumes/', 'job_description.txt')
for candidate in matches:
    print(f"{candidate['name']}: {candidate['score']}")
```

## Project Structure

```
.
├── src/
│   ├── parser/
│   ├── embeddings/
│   ├── similarity/
│   └── ranking/
├── data/
├── tests/
├── requirements.txt
└── README.md
```

## License

MIT

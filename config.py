"""Configuration settings for Smart Resume Screener"""

# Embedding settings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384

# FAISS settings
FAISS_INDEX_TYPE = "flat_l2"  # Can be "flat_l2", "ivf", etc.

# Ranking settings
SCORE_THRESHOLD = 50  # Minimum score to consider as match
TOP_K_RESULTS = 10

# File settings
RESUME_DIR = "data/resumes"
JOB_DESCRIPTIONS_DIR = "data/job_descriptions"
OUTPUT_DIR = "data/output"

# Model cache settings
MODEL_CACHE_DIR = ".model_cache"

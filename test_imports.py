#!/usr/bin/env python
"""Simple test to verify Smart Resume Screener is working"""

import sys
sys.path.insert(0, '/Users/rohitgupta/repositories/smart-resume-screener/smart-resume-screener')

# Just test imports without running the model
try:
    from screener import ResumeScreener
    print("✓ ResumeScreener imported successfully")
    
    from src.parser import ResumeParser, JobDescriptionParser
    print("✓ Parsers imported successfully")
    
    from src.embeddings import EmbeddingGenerator
    print("✓ EmbeddingGenerator imported successfully")
    
    from src.similarity import FAISSSearcher
    print("✓ FAISSSearcher imported successfully")
    
    from src.ranking import CandidateRanker
    print("✓ CandidateRanker imported successfully")
    
    print("\n✓ All modules loaded successfully!")
    print("\nSmart Resume Screener is ready to use.")
    print("\nTo use it, import and instantiate ResumeScreener:")
    print("  from screener import ResumeScreener")
    print("  screener = ResumeScreener()")
    print("  results = screener.match_single(resume_text, job_text)")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

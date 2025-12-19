#!/usr/bin/env python
"""Demo script for Smart Resume Screener"""

import sys
sys.path.insert(0, '/Users/rohitgupta/repositories/smart-resume-screener/smart-resume-screener')

from screener import ResumeScreener

# Example resume
sample_resume = """
John Doe
Software Engineer

SKILLS:
- Python
- JavaScript
- React
- AWS
- Docker
- Machine Learning

EXPERIENCE:
Senior Software Engineer at TechCorp (2020-2024)
- Led development of microservices architecture
- Improved system performance by 40%
- Managed team of 5 engineers

Software Engineer at StartupXYZ (2018-2020)
- Built full-stack web applications
- Implemented CI/CD pipelines
- Mentored junior developers
"""

# Example job description
sample_job = """
Senior Software Engineer - Backend

We are looking for a Senior Backend Engineer to join our team.

REQUIREMENTS:
- 5+ years of software engineering experience
- Strong proficiency in Python
- Experience with cloud platforms (AWS, GCP, Azure)
- Knowledge of containerization (Docker, Kubernetes)
- Experience building scalable systems
- Team leadership experience

RESPONSIBILITIES:
- Design and implement microservices
- Optimize system performance
- Lead technical initiatives
- Mentor junior developers
"""

# Initialize screener
screener = ResumeScreener()

# Match single resume
result = screener.match_single_resume(sample_resume, sample_job)

print("=" * 60)
print("RESUME SCREENING RESULT")
print("=" * 60)
print(f"Job Title: {result['job_title']}")
print(f"Match Score: {result['score']:.1f}%")
print(f"Similarity: {result['similarity']:.3f}")
print(f"Assessment: {result['explanation']}")
print("\nJob Requirements:")
for req in result['job_requirements'][:5]:
    print(f"  - {req}")
print("\nCandidate Skills:")
for skill in result['resume_skills'][:5]:
    print(f"  - {skill}")
print("=" * 60)

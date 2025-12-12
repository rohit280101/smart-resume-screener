"""Tests for the Resume Screener"""

import unittest
from screener import ResumeScreener


class TestResumeScreener(unittest.TestCase):
    """Test cases for ResumeScreener"""

    def setUp(self):
        """Set up test fixtures"""
        self.screener = ResumeScreener()

    def test_single_resume_match(self):
        """Test matching a single resume against a job"""
        resume_text = """
        John Doe
        Senior Software Engineer
        
        Experience:
        - 10 years in software development
        - Python, JavaScript, Rust expertise
        - AWS and Docker experience
        
        Education:
        - Bachelor's in Computer Science
        """
        
        job_text = """
        Job Title: Senior Software Engineer
        
        Requirements:
        - 5+ years experience
        - Python expertise required
        - Cloud platforms (AWS/GCP)
        
        Skills:
        - Python, JavaScript
        - Docker, Kubernetes
        """
        
        result = self.screener.match_single_resume(resume_text, job_text)
        
        self.assertIn("score", result)
        self.assertIn("explanation", result)
        self.assertGreater(result["score"], 0)
        self.assertLess(result["score"], 100)

    def test_parser_integration(self):
        """Test parser integration"""
        resume_text = "Senior Engineer with 5 years experience"
        job_text = "Looking for Senior Engineer"
        
        result = self.screener.match_single_resume(resume_text, job_text)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()

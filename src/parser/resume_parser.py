"""Resume parser for extracting structured information from resumes"""

import re
from typing import Dict, List, Any


class ResumeParser:
    """Parse resume text and extract structured information"""

    def __init__(self):
        self.sections = {}

    def parse(self, resume_text: str) -> Dict[str, Any]:
        """
        Parse resume text and extract structured information.
        
        Args:
            resume_text: Raw resume text
            
        Returns:
            Dictionary containing parsed resume data
        """
        parsed_resume = {
            "text": resume_text,
            "sections": self._extract_sections(resume_text),
            "skills": self._extract_skills(resume_text),
            "experience": self._extract_experience(resume_text),
            "education": self._extract_education(resume_text),
        }
        return parsed_resume

    def _extract_sections(self, text: str) -> Dict[str, str]:
        """Extract major sections from resume"""
        sections = {}
        # Simple section detection based on common headers
        headers = ["experience", "education", "skills", "projects", "certifications"]
        for header in headers:
            pattern = rf"{header}:?(.*?)(?=\n(?:{header}|$))"
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                sections[header] = match.group(1).strip()
        return sections

    def _extract_skills(self, text: str) -> List[str]:
        """Extract skills from resume"""
        # Simple skill extraction - can be enhanced
        skills = []
        skills_patterns = [
            r"skills?:?\s*(.*?)(?=\n\n|\Z)",
        ]
        for pattern in skills_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
            for match in matches:
                skills.extend([s.strip() for s in match.split(",") if s.strip()])
        return list(set(skills))

    def _extract_experience(self, text: str) -> List[Dict[str, str]]:
        """Extract work experience from resume"""
        experience = []
        # Pattern for job titles and companies
        pattern = r"([A-Z][a-z\s]+(?:Engineer|Manager|Developer|Analyst|Designer).*?)(?=\n[A-Z]|\Z)"
        matches = re.findall(pattern, text, re.MULTILINE)
        for match in matches:
            experience.append({"role": match.strip()})
        return experience

    def _extract_education(self, text: str) -> List[Dict[str, str]]:
        """Extract education from resume"""
        education = []
        # Pattern for degrees
        degrees = ["Bachelor", "Master", "PhD", "Diploma", "Associate"]
        for degree in degrees:
            pattern = rf"{degree}[^.\n]+"
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                education.append({"degree": match.strip()})
        return education

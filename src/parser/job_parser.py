"""Job description parser for extracting requirements and qualifications"""

import re
from typing import Dict, List, Any


class JobDescriptionParser:
    """Parse job descriptions and extract requirements"""

    def parse(self, job_text: str) -> Dict[str, Any]:
        """
        Parse job description and extract structured information.
        
        Args:
            job_text: Raw job description text
            
        Returns:
            Dictionary containing parsed job requirements
        """
        parsed_job = {
            "text": job_text,
            "title": self._extract_job_title(job_text),
            "requirements": self._extract_requirements(job_text),
            "skills": self._extract_skills(job_text),
            "experience_level": self._extract_experience_level(job_text),
        }
        return parsed_job

    def _extract_job_title(self, text: str) -> str:
        """Extract job title from description"""
        # Often in format "Position: Title" or first line
        lines = text.split("\n")
        for line in lines[:5]:  # Check first 5 lines
            if "position" in line.lower() or "title" in line.lower():
                return line.split(":")[-1].strip()
        return lines[0].strip() if lines else ""

    def _extract_requirements(self, text: str) -> List[str]:
        """Extract job requirements from description"""
        requirements = []
        # Look for common requirement markers
        lines = text.split("\n")
        capture = False
        for line in lines:
            if "requirement" in line.lower():
                capture = True
                continue
            if capture and line.strip():
                if re.match(r"^[-•*]\s", line):
                    requirements.append(line.strip()[2:])
                elif line.strip() and not line[0].isupper():
                    requirements.append(line.strip())
        return requirements

    def _extract_skills(self, text: str) -> List[str]:
        """Extract required skills from job description"""
        # Common technical skills
        tech_skills = [
            "python", "java", "javascript", "typescript", "c++", "rust",
            "sql", "nosql", "mongodb", "postgres", "mysql",
            "react", "angular", "vue", "node", "django", "flask",
            "aws", "azure", "gcp", "docker", "kubernetes",
            "machine learning", "ai", "nlp", "deep learning",
        ]
        found_skills = []
        text_lower = text.lower()
        for skill in tech_skills:
            if skill in text_lower:
                found_skills.append(skill)
        return found_skills

    def _extract_experience_level(self, text: str) -> str:
        """Determine experience level required"""
        text_lower = text.lower()
        if "senior" in text_lower or "10+ years" in text_lower:
            return "senior"
        elif "junior" in text_lower or "0-2 years" in text_lower:
            return "junior"
        elif "mid" in text_lower or "3-5 years" in text_lower:
            return "mid-level"
        return "entry-level"

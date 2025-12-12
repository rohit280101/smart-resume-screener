"""Main Resume Screener class"""

import os
from typing import List, Dict, Any
from src.parser import ResumeParser, JobDescriptionParser
from src.embeddings import EmbeddingGenerator
from src.similarity import FAISSSearcher
from src.ranking import CandidateRanker


class ResumeScreener:
    """Main class for screening resumes against job descriptions"""

    def __init__(self, embedding_model: str = "all-MiniLM-L6-v2"):
        """
        Initialize the Resume Screener.
        
        Args:
            embedding_model: Name of the Sentence Transformer model
        """
        self.resume_parser = ResumeParser()
        self.job_parser = JobDescriptionParser()
        self.embedder = EmbeddingGenerator(embedding_model)
        self.searcher = FAISSSearcher(self.embedder.get_embedding_dimension())
        self.ranker = CandidateRanker()
        self.resume_embeddings = {}

    def match_resumes(
        self, 
        resume_dir: str, 
        job_description_path: str,
        top_k: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Match resumes against a job description.
        
        Args:
            resume_dir: Directory containing resume files
            job_description_path: Path to job description file
            top_k: Number of top matches to return
            
        Returns:
            List of matched candidates ranked by score
        """
        # Read and parse job description
        with open(job_description_path, 'r') as f:
            job_text = f.read()
        
        job_data = self.job_parser.parse(job_text)
        job_embedding = self.embedder.generate(job_text)
        
        # Process resumes
        resume_files = [f for f in os.listdir(resume_dir) if f.endswith('.txt')]
        
        if not resume_files:
            return []
        
        # Parse and embed all resumes
        for resume_file in resume_files:
            resume_path = os.path.join(resume_dir, resume_file)
            with open(resume_path, 'r') as f:
                resume_text = f.read()
            
            resume_data = self.resume_parser.parse(resume_text)
            resume_embedding = self.embedder.generate(resume_text)
            self.resume_embeddings[resume_file] = resume_embedding
            self.searcher.add_embeddings(resume_embedding)
        
        # Search for similar resumes
        distances, indices = self.searcher.search(job_embedding[0], k=min(top_k, len(resume_files)))
        
        # Rank candidates
        candidate_ids = [resume_files[idx] for idx in indices]
        ranked_candidates = self.ranker.rank_candidates(distances, candidate_ids, job_data.get("title", ""))
        
        return ranked_candidates

    def match_single_resume(self, resume_text: str, job_text: str) -> Dict[str, Any]:
        """
        Match a single resume against a job description.
        
        Args:
            resume_text: Resume text
            job_text: Job description text
            
        Returns:
            Match result with score and explanation
        """
        # Parse texts
        job_data = self.job_parser.parse(job_text)
        resume_data = self.resume_parser.parse(resume_text)
        
        # Generate embeddings
        job_embedding = self.embedder.generate(job_text)
        resume_embedding = self.embedder.generate(resume_text)
        
        # Calculate similarity
        from sklearn.metrics.pairwise import cosine_similarity
        similarity = cosine_similarity(resume_embedding, job_embedding)[0][0]
        score = similarity * 100
        
        return {
            "score": float(score),
            "similarity": float(similarity),
            "explanation": self._generate_explanation(score),
            "job_title": job_data.get("title", ""),
            "job_requirements": job_data.get("requirements", []),
            "resume_skills": resume_data.get("skills", []),
        }

    def _generate_explanation(self, score: float) -> str:
        """Generate explanation for match score"""
        if score >= 85:
            return "Excellent match"
        elif score >= 70:
            return "Good match"
        elif score >= 50:
            return "Moderate match"
        else:
            return "Weak match"

"""Rank candidates based on job-resume similarity"""

import numpy as np
from typing import List, Dict, Any


class CandidateRanker:
    """Rank candidates based on their matching scores"""

    def __init__(self):
        self.candidates = []

    def rank_candidates(
        self, 
        distances: np.ndarray, 
        candidate_ids: List[str],
        job_title: str = ""
    ) -> List[Dict[str, Any]]:
        """
        Rank candidates based on similarity distances.
        
        Args:
            distances: Array of distances from query
            candidate_ids: List of candidate identifiers
            job_title: Job title for context
            
        Returns:
            List of ranked candidates with scores
        """
        # Convert L2 distances to similarity scores (0-100)
        # Normalize distances to scores
        max_distance = np.max(distances) if len(distances) > 0 else 1
        scores = 100 * (1 - distances / (max_distance + 1e-6))
        
        ranked = []
        for candidate_id, score, distance in zip(candidate_ids, scores, distances):
            ranked.append({
                "candidate_id": candidate_id,
                "score": float(score),
                "distance": float(distance),
                "explanation": self._generate_explanation(score)
            })
        
        # Sort by score descending
        ranked.sort(key=lambda x: x["score"], reverse=True)
        return ranked

    def _generate_explanation(self, score: float) -> str:
        """Generate explanation for the score"""
        if score >= 85:
            return "Excellent match"
        elif score >= 70:
            return "Good match"
        elif score >= 50:
            return "Moderate match"
        else:
            return "Weak match"

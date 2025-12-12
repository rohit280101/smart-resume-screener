"""Generate embeddings using Sentence Transformers"""

import numpy as np
from typing import List, Union
from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """Generate embeddings for texts using pre-trained models"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding generator.
        
        Args:
            model_name: Name of the Sentence Transformer model
        """
        self.model = SentenceTransformer(model_name)
        self.embedding_dim = self.model.get_sentence_embedding_dimension()

    def generate(self, texts: Union[str, List[str]]) -> np.ndarray:
        """
        Generate embeddings for input texts.
        
        Args:
            texts: Single text or list of texts
            
        Returns:
            Numpy array of embeddings
        """
        if isinstance(texts, str):
            texts = [texts]
        
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings

    def get_embedding_dimension(self) -> int:
        """Get dimension of embeddings"""
        return self.embedding_dim

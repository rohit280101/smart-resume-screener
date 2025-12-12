"""FAISS-based similarity search"""

import numpy as np
import faiss
from typing import List, Tuple


class FAISSSearcher:
    """Perform similarity search using FAISS"""

    def __init__(self, embedding_dim: int):
        """
        Initialize FAISS searcher.
        
        Args:
            embedding_dim: Dimension of embeddings
        """
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.embeddings_stored = []

    def add_embeddings(self, embeddings: np.ndarray) -> None:
        """
        Add embeddings to the index.
        
        Args:
            embeddings: Numpy array of shape (n, embedding_dim)
        """
        embeddings = np.asarray(embeddings, dtype=np.float32)
        self.index.add(embeddings)
        self.embeddings_stored.extend(embeddings.tolist())

    def search(self, query_embedding: np.ndarray, k: int = 5) -> Tuple[np.ndarray, np.ndarray]:
        """
        Search for similar embeddings.
        
        Args:
            query_embedding: Query embedding of shape (1, embedding_dim)
            k: Number of results to return
            
        Returns:
            Tuple of (distances, indices)
        """
        query_embedding = np.asarray(query_embedding, dtype=np.float32)
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)
        
        distances, indices = self.index.search(query_embedding, k)
        return distances[0], indices[0]

    def reset(self) -> None:
        """Reset the index"""
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.embeddings_stored = []

    def get_index_size(self) -> int:
        """Get number of embeddings in index"""
        return self.index.ntotal

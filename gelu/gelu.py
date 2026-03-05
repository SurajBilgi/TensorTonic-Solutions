import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.array(x, dtype=float)
    return 0.5 * x * (1 + np.vectorize(math.erf)(x / np.sqrt(2)))



"""
Where GELU is Used
	1.	Transformer Models
    	•	Used in the feed-forward layers of modern transformers.
	2.	Large Language Models (LLMs)
    	•	Used in architectures like BERT and GPT.
	3.	Vision Transformers
    	•	Used in Vision Transformer models.
"""
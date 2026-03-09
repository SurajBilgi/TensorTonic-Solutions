import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1 = np.array(x1, dtype=float)
    x2 = np.array(x2, dtype=float)
    
    cos_value = np.dot(x1,x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))

    if label == 1:
        loss = 1 - cos_value
    else:
        loss = max(0,cos_value-margin)

    return loss
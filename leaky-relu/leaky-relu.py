import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    # return np.maximum(alpha * x, x)
    x = np.array(x)
    return np.where(x > 0, x, alpha * x)
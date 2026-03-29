def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    import numpy as np
    img = np.array(image)
    
    # Apply weights: [R, G, B]
    weights = np.array([0.299, 0.587, 0.114])
    
    grayscale = np.dot(img, weights)
    
    return grayscale.tolist()
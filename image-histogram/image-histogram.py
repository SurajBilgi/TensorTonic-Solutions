def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    hist = [0]*256
    for pixel in image:
        for i in pixel:
            hist[i]+=1

    return hist
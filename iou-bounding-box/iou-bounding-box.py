def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    x1_a, y1_a, x2_a, y2_a = box_a
    x1_b, y1_b, x2_b, y2_b = box_b

    # Compute intersection coordinates
    x1 = max(x1_a, x1_b)
    y1 = max(y1_a, y1_b)
    x2 = min(x2_a, x2_b)
    y2 = min(y2_a, y2_b)

    # Compute intersection area
    inter_width = max(0, x2 - x1)
    inter_height = max(0, y2 - y1)
    intersection = inter_width * inter_height

    # Compute areas of both boxes
    area_a = max(0, x2_a - x1_a) * max(0, y2_a - y1_a)
    area_b = max(0, x2_b - x1_b) * max(0, y2_b - y1_b)

    # Compute union
    union = area_a + area_b - intersection

    # Avoid division by zero
    if union == 0:
        return 0.0

    return intersection / union
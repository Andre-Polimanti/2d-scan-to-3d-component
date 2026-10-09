import cv2
import numpy as np

def remove_noise(input_path, output_path, min_area=4000):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    n, lab, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=4)
    out = np.zeros_like(img)
    
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] >= min_area:
            out[lab == i] = 255
            
    cv2.imwrite(output_path, out)
    return out
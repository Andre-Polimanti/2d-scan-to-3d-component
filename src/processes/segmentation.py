import cv2
import numpy as np
import os
import shutil

def segmentation(img_path, output_path):
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    os.makedirs(output_path, exist_ok=True)
    
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_inv = cv2.bitwise_not(img)
    
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img_inv)
    
    part_index = 1
            
    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]
        
        if area >= 500000:
            print(f"Saving part {part_index}: x={x}, y={y}, width={w}, height={h}, area={area}")
            
            part = np.full((h, w), 255, dtype=np.uint8)
            part[labels[y:y+h, x:x+w] == i] = 0
            
            cv2.imwrite(os.path.join(output_path, f"{part_index}.png"), part)
            
            part_index += 1
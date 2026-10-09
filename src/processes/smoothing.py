import cv2

def smooth_silhouette(input_path, output_path, blur_size=21, threshold_value=127):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    blurred = cv2.GaussianBlur(img, (blur_size, blur_size), 0)
    _, out = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY)
    
    cv2.imwrite(output_path, out)
    return out
import cv2

MY_THRESHOLD = 127

def binarize_image(img, output_path):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, out = cv2.threshold(gray_img, MY_THRESHOLD, 255, cv2.THRESH_BINARY)
    
    cv2.imwrite(output_path, out)
    return out
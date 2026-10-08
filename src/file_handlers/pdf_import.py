import pymupdf
import cv2
import numpy as np

def pdf_to_img(pdf_path, page_num, image_index):
    document = pymupdf.open(pdf_path)
    try:
        page = document[page_num]
    except IndexError:
        print(f"Error: The page {page_num + 1} does not exist in the PDF.")
        return
        
    images = page.get_images(full=True)
    
    if not images:
        print("No image found at the indicated page.")
        return
        
    xref = images[image_index][0]
    base_image = document.extract_image(xref)
    image_bytes = base_image["image"]
    
    imagem_np = np.frombuffer(image_bytes, np.uint8)
    img_cv = cv2.imdecode(imagem_np, cv2.IMREAD_COLOR)
    
    if img_cv is None:
        print("Error in decodification.")
        return
    
    return img_cv
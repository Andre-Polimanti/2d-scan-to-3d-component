from file_handlers.pdf_import import pdf_to_img
from file_handlers.dxf_export import img_to_dxf

from processes.binarization import binarize_image
from processes.noise_removal import remove_noise
from processes.smoothing import smooth_silhouette

if __name__ == "__main__":
    INPUT_PDF = "data/input/scan-1.pdf"
    
    OUTPUT_BINARY_PNG = "data/output/png/binary.png" 
    OUTPUT_CLEAN_PNG = "data/output/png/clean.png"
    OUTPUT_SMOOTH_PNG = "data/output/png/smooth.png" 
    
    OUTPUT_DXF = "data/output/dxf/out.dxf"

        
    image = pdf_to_img(INPUT_PDF, 0, 0)
    binary = binarize_image(image, OUTPUT_BINARY_PNG)
    clean = remove_noise(binary, OUTPUT_CLEAN_PNG)
    smooth = smooth_silhouette(clean, OUTPUT_SMOOTH_PNG)
    
    img_to_dxf(OUTPUT_SMOOTH_PNG, 1200, OUTPUT_DXF)
import cv2
import ezdxf

def img_to_dxf(image_path, dpi, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Failed to load image!")
    
    pixel_per_mm = dpi / 25.4
    img = cv2.bitwise_not(img)

    outlines, _ = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)

    doc = ezdxf.new(dxfversion='R2010')
    msp = doc.modelspace()

    h = img.shape[0]
    for c in outlines:
        points_mm = [(p[0][0] / pixel_per_mm, (h - p[0][1]) / pixel_per_mm) for p in c]
        if len(points_mm) > 2:
            msp.add_lwpolyline(points_mm, close=True)

    doc.saveas(output_path)
    print(f"Succes in generating the {output_path} file!")
import cv2
import os

import sys, pymupdf  # import the bindings


def execute(img_path, exam, page):
    print(img_path)

    image = cv2.imread(img_path)

     # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold or edge detection
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Optional: Clean up noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create output directory
    subimage_output_dir = os.path.join("manual_figure_extraction", "opencv", exam[:-4])
    os.makedirs(subimage_output_dir, exist_ok=True)

    # Extract subimages
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 30 and h > 30:  # Filter out tiny boxes
            filename = page[:-4] + "_" + f"subimage_{i}.png"
            subimage_path = os.path.join(subimage_output_dir, filename)
            roi = image[y:y+h, x:x+w]
            cv2.imwrite(subimage_path, roi)

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     if w > 30 and h > 30:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow("Detected Subimages", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if __name__ == "__main__":
    filename = "sp18-final-sol"
    doc = pymupdf.open("data/sp18-final-sol.pdf")  # open document

    pdf_output_dir = os.path.join("manual_figure_extraction", "pdf_to_image", "sp18-final-sol")
    os.makedirs(pdf_output_dir, exist_ok = True)

    for page in doc:  # iterate through the pages
        filename = "page-%i.png" % page.number
        pix = page.get_pixmap()  # render page to an image
        new_path = os.path.join(pdf_output_dir, filename)
        pix.save(new_path)  # store image as a PNG

    input_dir = "manual_figure_extraction/pdf_to_image"

    for exam in os.listdir(input_dir):
        for page in os.listdir(os.path.join(input_dir, exam)):
            # Load the image (from the PDF)
            execute(os.path.join(input_dir, exam, page), exam, page)
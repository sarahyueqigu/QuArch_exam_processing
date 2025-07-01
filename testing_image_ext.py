import fitz
import os
from PIL import Image
import io
import pypdf
import pikepdf

#pike cannot read some of the byte streams in the pdfs,..

def extract_images_as_png(pdf_path, output_folder):
    pdf = fitz.open(pdf_path)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
 
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)  # load the page
        image_list = page.get_images(full=True)  # get images on the page

        if image_list:
            print(f"[+] Found a total of {len(image_list)} images on page {page_num + 1}")
        else:
            print(f"[!] No images found on page {page_num + 1}")
        
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]
            #image_ext = base_image["ext"]
            image = pdf.extract_image(xref)
            pix = fitz.Pixmap(pdf, xref)
            pix.save(os.path.join(output_folder, "%s_p%s-%s.png" % (os.path.splitext(os.path.basename(pdf_path))[0], page_num + 1, image_index)))
            

            # # Convert to PNG using PIL
            # image = Image.open(io.BytesIO(image_bytes))
            # image_name = f"{output_folder}/image{page_num + 1}_{image_index}.png"
            # image.save(image_name, "PNG")
            # print(f"[+] Image saved as {image_name}")

            #saved_images.append(image_name)
        #return saved_images

def pike_extract(pdf_path: str, output_folder: str):
    # 1) ensure output dir
    os.makedirs(output_folder, exist_ok=True)

    # 2) open the PDF
    pdf = pikepdf.Pdf.open(pdf_path)

    # 3) loop over pages & their embedded images
    for page_index, page in enumerate(pdf.pages, start=1):
        for name, img_meta in page.images.items():
            # img_meta.objgen is a (obj_num, gen_num) tuple
            objid = img_meta.objgen

            # grab the raw image-stream object
            stream = pdf.get_object(objid)
            data = stream.read_bytes()
            filt = stream.get("/Filter")

            # decode into a PIL image
            if filt in (pikepdf.Name("/DCTDecode"), pikepdf.Name("/JPXDecode")):
                # JPEG or JPEG2000
                pil_img = Image.open(io.BytesIO(data))
            elif filt == pikepdf.Name("/FlateDecode"):
                # raw bitmap: pick up width/height from the metadata
                w, h = img_meta.width, img_meta.height
                pil_img = Image.frombytes("RGB", (w, h), data, decoder_name="raw")
            else:
                # unsupported filter
                continue

            pil_img.load()  # make sure it's fully decoded

            # write out as a PNG
            clean_name = name.lstrip("/")          # e.g. "/Im0" → "Im0"
            out_name   = f"page{page_index}_{clean_name}.png"
            out_path   = os.path.join(output_folder, out_name)
            pil_img.save(out_path, format="PNG")
            print(f"Saved {out_path}")

    print(f"Done — all images in {output_folder}")

if __name__ == "__main__":
    pdf_path = "/Users/aliceguo/Documents/QuArch_exam_processing/OnurETHZ_exams_test2/exam_ws2012_solutions.pdf"  # replace with your PDF file path
    #pdf_path = "/Users/aliceguo/Documents/QuArch_exam_processing/OnurETHZ_exams_test2/digitaltechnik_s18_final_en-sol (1).pdf"
    #pdf_path = "/Users/aliceguo/Documents/QuArch_exam_processing/OnurETHZ_exams_test2/solution.pdf"
    
    #extract_images_from_pdf(pdf_path)
    #extract_images_as_png(pdf_path, "extracted_images")
    
    #pike_extract(pdf_path, "extracted_images_pike") #no work.
    
    # # Example usage of PIL to open and display an image
    # image_path = "image1_1.png"  # replace with the actual image file name
    # img = Image.open(image_path)
    # img.show()  # This will open the image using the default image viewer
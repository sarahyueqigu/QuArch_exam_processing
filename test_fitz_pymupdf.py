import fitz
import tqdm
import os
from PIL import Image


def execute():
    workdir = "data"
    os.makedirs("manual_figure_extraction/fitz", exist_ok=True)

    for each_path in os.listdir(workdir):
        if ".pdf" in each_path:
            doc = fitz.Document((os.path.join(workdir, each_path)))

            for i in tqdm.tqdm(range(len(doc)), desc="pages"):
                for img in tqdm.tqdm(doc.get_page_images(i), desc="page_images"):
                    xref = img[0]
                    image = doc.extract_image(xref)
                    pix = fitz.Pixmap(doc, xref)
                    pix.save(os.path.join("manual_figure_extraction", "fitz", "%s_p%s-%s.png" % (each_path[:-4], i, xref)))
                    
    print("FITZ: task completed")
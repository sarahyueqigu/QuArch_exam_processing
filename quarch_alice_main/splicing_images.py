import pymupdf
from PIL import Image

# Open the PDF
pdf_path = "/Users/aliceguo/Documents/QuArch_exam_processing/quarch_alice_main/small_sample_exams/CDA 4205 Computer Architecture Exam 2 Practice Solution-3.pdf"
doc = pymupdf.open(pdf_path)

# Select the two pages where the split table appears
page5 = doc.load_page(4)  # Page 5 (0‑indexed)
page6 = doc.load_page(5)  # Page 6

# Render pages to images at 150 dpi for clarity
pix5 = page5.get_pixmap(dpi=150)
pix6 = page6.get_pixmap(dpi=150)

# Convert to PIL Images
img5 = Image.frombuffer("RGB", (pix5.width, pix5.height), pix5.samples, "raw", "RGB", 0, 1)
img6 = Image.frombuffer("RGB", (pix6.width, pix6.height), pix6.samples, "raw", "RGB", 0, 1)

# Determine the split position (horizontal midpoint)
mid_y = img5.height // 2

# Crop the bottom half of page 5 (continuation of the table)
bottom_part = img5.crop((0, mid_y, img5.width, img5.height))

# Crop the top half of page 6 (next part of the table)
top_part = img6.crop((0, 0, img6.width, mid_y))

# Create a new image to splice the two parts vertically
spliced = Image.new("RGB", (img5.width, bottom_part.height + top_part.height))
spliced.paste(bottom_part, (0, 0))
spliced.paste(top_part, (0, bottom_part.height))

# Save and display the spliced table
spliced.save("spliced_q4a_timing_table.png")
spliced
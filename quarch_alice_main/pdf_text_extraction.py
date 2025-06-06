import os
from pathlib import Path
import pymupdf
import pymupdf4llm
from docx import Document

# doc = pymupdf.open("Please Upload Your QAs Here_ (File responses)/CDA 4205 Computer Architecture Exam 2 Practice Solution-3.pdf") # open a document
# out = open("output.txt", "wb") # create a text output
# PDF to plain text
# for page in doc: # iterate the document pages
#     text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
#     # out.write(text) # write text of page
#     # out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
#     one_line_bytes = (text.replace(b"\r", b" ").replace(b"\n", b" "))
#     out.write(one_line_bytes)
# out.close()
# PDF to markdown using pymupdf4llm

def pdf_to_markdown(input_path: Path) -> str:
    """
    Load a PDF with pymupdf4llm and return its contents as Markdown.
    """
    # Doc(...) will load the PDF and make available a .convert_markdown() method
    return pymupdf4llm.to_markdown(str(input_path))

def docx_to_markdown(input_path: Path) -> str:
    """
    Load a .docx file via python-docx, extract all paragraphs, and join them with blank lines.
    """
    document = Document(str(input_path))
    lines = []
    for para in document.paragraphs:
        text = para.text.strip()
        if not text:
            # preserve blank line for paragraph breaks
            lines.append("")
        else:
            lines.append(text)
    # Join by two newlines so that paragraphs stay separated
    return "\n\n".join(lines)

def convert_folder_to_markdown(
    folder_path: str,
    output_folder: str = None
) -> None:
    """
    Given a folder containing .pdf and .docx files, convert each file into Markdown
    and write out a .md file with the same base name. If output_folder is not provided,
    a new folder named "md_outputs" will be created next to the input folder.
    """
    folder = Path(folder_path)
    if output_folder is None:
        output_dir = folder.parent / "md_outputs"
    else:
        output_dir = Path(output_folder)

    output_dir.mkdir(parents=True, exist_ok=True)

    for entry in folder.iterdir():
        if not entry.is_file():
            continue
        ext = entry.suffix.lower()
        base_name = entry.stem  # e.g. "Exam1" from "Exam1.pdf"
        md_filename = output_dir / f"{base_name}.md"
        try:
            if ext == ".pdf":
                print(f"Converting PDF → Markdown: {entry.name}")
                md_text = pdf_to_markdown(entry)
            elif ext == ".docx":
                print(f"Converting DOCX → Markdown: {entry.name}")
                md_text = docx_to_markdown(entry)
            else:
                # skip anything that isn't .pdf or .docx
                continue
            # Write the Markdown out
            with open(md_filename, "w", encoding="utf-8") as out_f:
                out_f.write(md_text)
            print(f"  → Wrote {md_filename.relative_to(folder.parent)}")
        except Exception as e:
            print(f"  [Error converting {entry.name}]: {e}")
            

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python pdf_text_extraction.py /path/to/exams_folder [optional_output_folder]")
        sys.exit(1)

    in_folder = sys.argv[1]
    out_folder = sys.argv[2] if len(sys.argv) > 2 else None
    convert_folder_to_markdown(in_folder, out_folder)

    #convert_folder_to_markdown("/Users/aliceguo/Documents/QuArch_exam_processing/quarch_alice_main/Please Upload Your QAs Here_ (File responses)", "/Users/aliceguo/Documents/QuArch_exam_processing/quarch_alice_main/out_folder")


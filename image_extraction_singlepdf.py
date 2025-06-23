import os
import asyncio

async def process_single_file(fname):
    # Parse just one file
    result = await parser.aparse([fname])  # still returns a list

    result = result[0]  # unpack the single result
    output_dir = fname[:-4] + "_images"

    # Save all images in bulk
    await result.asave_all_images(output_dir)

    # Save each chart image by name
    for page in result.pages:
        for chart in page.charts:
            print("Saving", chart.name, "to", output_dir)
            await result.asave_image(chart.name, output_dir)

def process(filename, input_dir):
    pdf_files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".pdf")
    ]

    print(pdf_files)

    for fname in pdf_files:
        print(f"Processing:", input_dir)
        asyncio.run(process_single_file(fname))

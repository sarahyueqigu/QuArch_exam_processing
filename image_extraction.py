import asyncio
import nest_asyncio

import os
from dotenv import load_dotenv

load_dotenv()
nest_asyncio.apply()


from llama_cloud_services import LlamaParse

parser = LlamaParse(
    api_key=os.getenv("LLAMAPARSE_API_KEY"),
    parse_mode="parse_page_with_llm",
    extract_charts=True,
    num_workers=4,       # if multiple files passed, split in `num_workers` API calls
    verbose=True,
)

# single file example below:
# result = await parser.aparse("/content/CDA 4205 Computer Architecture Exam 2 Practice Solution-3.pdf")

# or we can batch-run for multiple files
# file_batch = [

#     "data/ddca-s23-en-sol.pdf",
#     "data/Culler_mid1-soln.pdf",

# ]
async def process_files(file_batch):
    # parse all the files asynchronously
    results = await parser.aparse(file_batch)

    # Now for each file, save all images to a designated folder
    for i, fname in enumerate(file_batch):
        output_dir = fname[:-4] + "_images"

        # save all images in bulk
        await results[i].asave_all_images(output_dir)

        # then save each chart image by name
        for page in results[i].pages:
            for chart in page.charts:
                print("Saving ", chart.name, "to", output_dir)
                await results[i].asave_image(chart.name, output_dir)

def process(folder):

    file_batch = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".pdf") ]
    
    print(file_batch)

    asyncio.run(process_files(file_batch))

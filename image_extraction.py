import asyncio

# import nest_asyncio
# nest_asyncio.apply()

from llama_cloud_services import LlamaParse

parser = LlamaParse(
    api_key="llx-K1mUygWh37kvgzJbCvvdROrM8N5XBfQFdM3mXfgye1GzYJtZ",
    parse_mode="parse_page_with_llm",
    extract_charts=True,
    num_workers=4,       # if multiple files passed, split in `num_workers` API calls
    verbose=True,
)

# single file example below:
# result = await parser.aparse("/content/CDA 4205 Computer Architecture Exam 2 Practice Solution-3.pdf")

# or we can batch-run for multiple files
file_batch = [

    "data/ddca-s23-en-sol.pdf",
    "data/sp18-final-sol.pdf",

]
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
                await results[i].asave_image(chart.name, output_dir)

if __name__ == "__main__":
    # replace file_batch with your actual list of filenames
    # file_batch = ["report1.pdf", "report2.pdf", ...]
    asyncio.run(process_files(file_batch))

# #NOTE TO TEAM: Run this line during testing to clean up/remove all the
# #created images in a Colab directory!
# !rm -rf "/content/sp18-final-sol.pdf_images"

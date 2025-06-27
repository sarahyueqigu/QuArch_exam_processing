import asyncio
import nest_asyncio

from dotenv import load_dotenv

load_dotenv()
nest_asyncio.apply()


from llama_cloud_services import LlamaParse


parser = LlamaParse(
    api_key="llx-K1mUygWh37kvgzJbCvvdROrM8N5XBfQFdM3mXfgye1GzYJtZ",
    parse_mode="parse_page_with_llm",
    extract_charts=True,
    num_workers=4,       # if multiple files passed, split in `num_workers` API calls
    verbose=True,
)

async def process_files(filename, file_path, output_dir):
    # parse all the files asynchronously
    results = await parser.aparse(file_path)

    # Now for each file, save all images to a designated folder
    await results.asave_all_images(output_dir)

    # then save each chart image by name
    for page in results.pages:
        for chart in page.charts:
            await results.asave_image(chart.name, output_dir)

def process(filename, file_path, output_dir):
    print(file_path)
    asyncio.run(process_files(filename, file_path, output_dir))
    # replace file_batch with your actual list of filenames
    # file_batch = ["report1.pdf", "report2.pdf", ...]

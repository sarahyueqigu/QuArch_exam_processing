from skimage import io, color, filters, measure, morphology
import matplotlib.pyplot as plt
import os

def execute(input_path, exam, page):
    # Load image (grayscale or color)
    image = io.imread(input_path)
    gray = color.rgb2gray(image)  # Convert to grayscale

    # Apply threshold (Otsu)
    thresh = filters.threshold_otsu(gray)
    binary = gray < thresh  # Invert if needed

    # Remove small artifacts
    cleaned = morphology.remove_small_objects(binary, min_size=100)

    # Label connected regions
    labeled = measure.label(cleaned)

    # Create output folder
    os.makedirs("subimages", exist_ok=True)

    output_dir = os.path.join("manual_figure_extraction", "scikit", exam[:-4])
    os.makedirs(output_dir, exist_ok=True)

    # Loop through each region
    for i, region in enumerate(measure.regionprops(labeled)):
        # Extract bounding box
        minr, minc, maxr, maxc = region.bbox
        subimage = image[minr:maxr, minc:maxc]

        filename = page[:-4] + "_" + f"subimage_{i}.png"
        output_path = os.path.join(output_dir, filename)

        print("SCIKIT: saved image to", output_path)
        # Save subimage
        io.imsave(output_path, subimage)

        # # Optional: show
        # plt.imshow(subimage)
        # plt.title(f"Subimage {i}")
        # plt.axis('off')
        # plt.show()
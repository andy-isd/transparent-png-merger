from PIL import Image
import os

# Define the input folder and output file name
input_folder = './input'  # The input folder is set as './input'
output_image_path = 'output.png'  # The output file name

def combine_images_horizontally_with_transparency_sorted(input_folder, output_image_path):
    """
    Combine images horizontally from a given input folder, preserving transparency,
    and sorting the images by name.
    :param input_folder: Folder containing PNG images to combine.
    :param output_image_path: Path for the combined output image.
    """
    # List all PNG files in the input folder and sort them
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.png')])
    images = [Image.open(os.path.join(input_folder, f)).convert('RGBA') for f in image_files]

    # Calculate total width and max height
    total_width = sum(image.size[0] for image in images)
    max_height = max(image.size[1] for image in images)

    # Create a new image with the appropriate size and transparency support
    combined_image = Image.new('RGBA', (total_width, max_height), (0, 0, 0, 0))

    # Paste each image into the combined image
    x_offset = 0
    for image in images:
        combined_image.paste(image, (x_offset, 0), image)
        x_offset += image.size[0]

    # Save the combined image
    combined_image.save(output_image_path)
    print(f'Sorted combined image with transparency saved as {output_image_path}')

# Combine images with transparency support, sorting by name, and print the path to the combined image
combine_images_horizontally_with_transparency_sorted(input_folder, output_image_path)

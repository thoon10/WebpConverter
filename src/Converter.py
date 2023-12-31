import os
from PIL import Image

def convert_webp_in_directory(input_directory, output_directory, quality, outType):
    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    convert_result = None

    # Iterate through files in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(".webp"):
            # Construct full paths
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + "." + outType)
            if (outType == "png"):
                convert_result = convert_webp_to_png(input_path, output_path)
            convert_result = convert_webp_to_jpg(input_path, output_path, quality)

    return convert_result

def convert_webp_to_png(input_path, output_path):
    try:
        # Open the WebP image
        with Image.open(input_path) as img:
            # Save as PNG
            img.save(output_path, 'PNG')
        print(f"Conversion successful: {input_path} -> {output_path}")
        return True
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False


def convert_webp_to_jpg(input_path, output_path, quality):
    try:
        # Open the WebP image
        with Image.open(input_path) as img:
            # Save as JPG with specified quality
            img.convert("RGB").save(output_path, 'JPEG', quality=quality, optimize=True)
        print(f"Conversion successful: {input_path} -> {output_path}")
        return True
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False





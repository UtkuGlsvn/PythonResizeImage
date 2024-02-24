# PythonResizeImage
This code is a versatile Python script designed to resize images effortlessly. The script allows users to specify the desired output size and format for their images, making it a handy tool for quickly adjusting image dimensions for various applications such as web design, graphic design, or data preprocessing in machine learning.

# Image Resizer

This Python script allows you to resize images to a specified size and format.

## Requirements

- Python 3
- Pillow library

## Installation

Before running the script, ensure you have Pillow installed. You can install it using pip:

Code Format: python resize_image.py -i [input_path] -o [output_path] -w [width] -H [height] -f [format]

```bash
pip install Pillow

Usage
Run the script from the command line with the following arguments:

-i or --input: Path to the input image file.
-o or --output: Path for the resized output image file.
-w or --width: Width of the output image in pixels.
-H or --height: Height of the output image in pixels.
-f or --format: Format of the output image (either 'png' or 'jpeg').



python resize_image.py -i "path/to/input/image.jpg" -o "path/to/output/image.png" -w 100 -H 100 -f png
This will resize the input image to 100x100 pixels and save it in PNG format.

Note
Supported formats for output are PNG and JPEG.
The aspect ratio of the image is not maintained. Specify the exact width and height you want.


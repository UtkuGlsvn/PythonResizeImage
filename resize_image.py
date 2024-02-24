import argparse
from PIL import Image

def resize_image(input_path, output_path, size, format):
    img = Image.open(input_path)
    img_resized = img.resize(size, Image.LANCZOS)

    if format.lower() == 'png':
        img_resized.save(output_path, format='PNG')
    elif format.lower() == 'jpeg' or format.lower() == 'jpg':
        img_resized.save(output_path, format='JPEG')
    else:
        raise ValueError("Unsupported format. Only 'png' and 'jpeg' are supported.")

def main():
    parser = argparse.ArgumentParser(description='Resize an image.')
    parser.add_argument('-i', '--input', required=True, help='Input image file path')
    parser.add_argument('-o', '--output', required=True, help='Output image file path')
    parser.add_argument('-w', '--width', type=int, required=True, help='Width of the output image')
    parser.add_argument('-H', '--height', type=int, required=True, help='Height of the output image')
    parser.add_argument('-f', '--format', required=True, help='Output image format (png or jpeg)')


    args = parser.parse_args()
    size = (args.width, args.height)
    resize_image(args.input, args.output, size, args.format)

if __name__ == "__main__":
    main()

import sys
import os
from pdf2image import convert_from_path
from PIL import Image
import subprocess

if len(sys.argv) != 2:
    print("Usage: python3 showpdf.py <path_to_pdf>")
    sys.exit(1)

pdf_path = sys.argv[1]

# Define output filename
bmp_filename = 'output.bmp'

try:
    # Convert PDF to image using pdf2image (first page only)
    pages = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=300)
    if not pages:
        print("Error: Failed to convert PDF to image.")
        sys.exit(1)
    
    # Get first page and rotate it
    image = pages[0].rotate(270, expand=True)
    
    # Save as BMP
    image.save(bmp_filename, 'BMP')
    
    # Execute render_bmp
    result = subprocess.run(['./render_bmp', '0', '0', bmp_filename])
    if result.returncode != 0:
        print("Error: render_bmp failed.")
        sys.exit(1)

finally:
    # Clean up temporary file
    if os.path.exists(bmp_filename):
        os.remove(bmp_filename)

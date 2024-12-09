#!/usr/bin/python3

import sys
import os
import tempfile
from urllib.parse import urlparse
import requests
from pdf2image import convert_from_path
from PIL import Image
import subprocess

if len(sys.argv) != 2:
    print("Usage: python3 showpdf.py <path_to_pdf_or_url>")
    sys.exit(1)

input_path = sys.argv[1]
temp_pdf = None
bmp_filename = 'output.bmp'

try:
    # Check if the input is a URL
    parsed = urlparse(input_path)
    if parsed.scheme in ('http', 'https'):
        # Download the PDF to a temporary file
        response = requests.get(input_path, stream=True)
        if response.status_code != 200:
            print(f"Error: Failed to download PDF. Status code: {response.status_code}")
            sys.exit(1)
        
        # Create a temporary file for the PDF
        temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        with temp_pdf as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        pdf_path = temp_pdf.name
    else:
        # Use local file path
        pdf_path = input_path
        if not os.path.exists(pdf_path):
            print(f"Error: File not found: {pdf_path}")
            sys.exit(1)

    # Convert PDF to image using pdf2image (first page only)
    pages = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=300)
    if not pages:
        print("Error: Failed to convert PDF to image.")
        sys.exit(1)
    
    # Get first page and rotate it
    image = pages[0].rotate(90, expand=True)
    
    # Save as BMP
    image.save(bmp_filename, 'BMP')
    
    # Execute render_bmp
    result = subprocess.run(['./render_bmp', '0', '0', bmp_filename])
    if result.returncode != 0:
        print("Error: render_bmp failed.")
        sys.exit(1)

finally:
    # Clean up temporary files
    if temp_pdf and os.path.exists(temp_pdf.name):
        os.remove(temp_pdf.name)
    if os.path.exists(bmp_filename):
        os.remove(bmp_filename)

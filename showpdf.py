import sys
import subprocess
import os
import tempfile

if len(sys.argv) != 2:
    print("Usage: python3 showpdf.py <path_to_pdf>")
    sys.exit(1)

pdf_path = sys.argv[1]

# Create a temporary BMP file
with tempfile.NamedTemporaryFile(suffix='.bmp', delete=False) as temp_bmp:
    bmp_filename = temp_bmp.name

# Convert PDF to PNG using pdftocairo
png_filename = bmp_filename.replace('.bmp', '.png')
subprocess.run(['pdftocairo', '-png', '-singlefile', '-f', '1', '-l', '1', '-r', '300', pdf_path, png_filename])

# Convert PNG to BMP using ImageMagick's convert command
subprocess.run(['convert', png_filename, bmp_filename])

# Execute render_bmp
subprocess.run(['./render_bmp', '0', '0', bmp_filename])

# Clean up temporary files
os.remove(bmp_filename)
os.remove(png_filename)

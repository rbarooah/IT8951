import sys
import subprocess
import os
import tempfile

if len(sys.argv) != 2:
    print("Usage: python3 showpdf.py <path_to_pdf>")
    sys.exit(1)

pdf_path = sys.argv[1]

# Define output filenames
png_filename = 'output.png'
bmp_filename = 'output.bmp'

# Convert PDF to PNG using pdftocairo
result = subprocess.run(['pdftocairo', '-png', '-singlefile', '-f', '1', '-l', '1', '-r', '300', pdf_path, png_filename], capture_output=True, text=True)
if result.returncode != 0:
    print("Error: pdftocairo failed to generate PNG.")
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    sys.exit(1)

# Convert PNG to BMP using ImageMagick's convert command
result = subprocess.run(['convert', png_filename, bmp_filename], capture_output=True, text=True)
if result.returncode != 0:
    print("Error: convert failed to generate BMP.")
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    sys.exit(1)

# Execute render_bmp
result = subprocess.run(['./render_bmp', '0', '0', bmp_filename])
if result.returncode != 0:
    print("Error: render_bmp failed.")
    sys.exit(1)

# Clean up temporary files
if os.path.exists(png_filename):
    os.remove(png_filename)
if os.path.exists(bmp_filename):
    os.remove(bmp_filename)

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

# Convert PDF to BMP using pdftocairo
subprocess.run(['pdftocairo', '-bmp', '-singlefile', '-scale-to', '1872', '-scale-to-y', '1404', pdf_path, bmp_filename[:-4]])

# Execute render_bmp
subprocess.run(['./render_bmp', '0', '0', bmp_filename])

# Clean up temporary file
os.remove(bmp_filename)

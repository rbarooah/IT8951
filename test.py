import cairo
import os
import subprocess
import tempfile

# Create a temporary BMP file
with tempfile.NamedTemporaryFile(suffix='.bmp', delete=False) as temp_bmp:
    bmp_filename = temp_bmp.name

# Set up Cairo surface
width, height = 1872, 1404
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
context = cairo.Context(surface)

# Fill background with white
context.set_source_rgb(1, 1, 1)
context.paint()

# Draw a circle
circle_diameter = 500
context.set_source_rgb(0, 0, 0)  # Black color
context.arc(width / 2, height / 2, circle_diameter / 2, 0, 2 * 3.14159)
context.fill()

# Write to BMP file
surface.write_to_png(bmp_filename)

# Convert PNG to BMP using ImageMagick's convert command
bmp_converted_filename = bmp_filename.replace('.bmp', '_converted.bmp')
subprocess.run(['convert', bmp_filename, bmp_converted_filename])

# Execute render_bmp
subprocess.run(['./render_bmp', '0', '0', bmp_converted_filename])

# Clean up temporary files
os.remove(bmp_filename)
os.remove(bmp_converted_filename)

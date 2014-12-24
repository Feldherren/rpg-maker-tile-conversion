#! python2.7

# Feldherren's shiny handy script for converting RM2000 format autotiles to VX Ace format.
# Just drop this in the directory containing RM2000 format autotiles (manually cut out from tilesets, I'm afraid) and run it. It'll do all the work.

# Note: requires python 2.7 and the Python Imaging Library (PIL)

from PIL import Image
import os, glob

def convert(infile):
	file, ext = os.path.splitext(infile)
	p = os.path.dirname(os.path.abspath(__file__))
	if not os.path.exists(p + "\\Converted"): os.makedirs(p + "\\Converted")
	im = Image.open(infile)
	converted = Image.new('RGB',(64,96))
	
	# full tile
	converted.paste(im.crop((0,0,288,32)), (0,96,288,128))
	
	# move up-facing poses to the correct position
	converted.paste(im.crop((0,0,288,32)), (0,96,288,128))
	converted.paste(im.crop((0,128,288,160)), (0,224,288,256))
	
	# move right-facing poses to the correct position
	converted.paste(im.crop((0,32,288,64)), (0,64,288,96))
	converted.paste(im.crop((0,160,288,192)), (0,192,288,224))
	
	# move down-facing poses to the correct position
	converted.paste(im.crop((0,64,288,96)), (0,0,288,32))
	converted.paste(im.crop((0,192,288,224)), (0,128,288,160))
	
	# move left-facing poses to the correct position
	converted.paste(im.crop((0,96,288,128)), (0,32,288,64))
	converted.paste(im.crop((0,224,288,256)), (0,160,288,192))
	
	# # Resize converted image
	# converted = converted.resize((576,512))
	
	# Save converted image in PNG format
	converted.resize((64,96)).save("Converted\\[VX] " + file + ".png", 'PNG')

for infile in glob.glob("*.bmp"):
	convert(infile)
for infile in glob.glob("*.png"):
	convert(infile)
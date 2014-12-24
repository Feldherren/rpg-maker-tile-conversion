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
	converted = Image.new('RGB',(32,48))
	
	# full tile
	#converted.paste(im.crop((16,32,32,48)), (8,24,24,40))
	# upper left to lower right
	converted.paste(im.crop((16,32,24,40)), (16,32,24,40))
	# lower right to upper left
	converted.paste(im.crop((24,40,32,48)), (8,24,16,32))
	# upper right to lower left
	converted.paste(im.crop((24,32,32,40)), (8,32,16,40))
	# lower left to upper right
	converted.paste(im.crop((16,40,24,48)), (16,24,24,32))
	
	# inside corners
	converted.paste(im.crop((32,0,48,16)), (16,0,32,16))
	
	# outside corners
	# upper left
	converted.paste(im.crop((0,16,8,24)), (0,16,8,24))
	# lower left
	converted.paste(im.crop((0,56,8,64)), (0,40,8,48))
	# upper right
	converted.paste(im.crop((40,16,48,24)), (24,16,32,24))
	# lower right
	converted.paste(im.crop((40,56,48,64)), (24,40,32,48))
	
	# edges
	# up
	converted.paste(im.crop((16,16,32,24)), (8,16,24,24))
	# right
	converted.paste(im.crop((40,32,48,48)), (24,24,32,40))
	# down
	converted.paste(im.crop((16,56,32,64)), (8,40,24,48))
	# left
	converted.paste(im.crop((0,32,8,48)), (0,24,8,40))
	
	# single tile
	converted.paste(im.crop((16,0,32,16)), (0,0,16,16))
	
	# Save converted image in PNG format
	converted.resize((64,96)).save("Converted\\[VX] " + file + ".png", 'PNG')
	#converted.save("Converted\\[VX] " + file + ".png", 'PNG')

for infile in glob.glob("*.bmp"):
	convert(infile)
for infile in glob.glob("*.png"):
	convert(infile)
import os
import glob
import shutil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Sort pictures by name, get total in list, and get the list number of the last pic
piclist = sorted(glob.glob('*.jpg'))
number_of_files = len(piclist)
lastpic = piclist[(number_of_files - 1)]

# Copy last frame to '00000001.jpg'
print ""
print "---"
print str(number_of_files) + " total files in directory"
print str(lastpic) + " is the last frame, and is being copied to 00000001.jpg"

shutil.copyfile(lastpic, './labeledPhotos/00000001.jpg')

# Label new daily frame
# 'curentfilename' is the original files name, 'datelabel' is the date label for the image
datelabel = lastpic[:-4]
datelabel = datelabel[4] + datelabel[5] + '-' + datelabel[6] + datelabel[7] + '-' + datelabel[:4]


try:
	importimg = Image.open(lastpic)
	draw = ImageDraw.Draw(importimg)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype("./fonts/roboto-medium.ttf", 32)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((10, 0),datelabel,(255,255,255),font=font)
	importimg.save('./labeledPhotos/' + str(lastpic), 'JPEG')
except OSError:
	print ""
	print "[Copying " + str(lastpic) + " to 00000001.jpg failed]"
else:
	print ""
	print "[Copying " + str(lastpic) + " 00000001.jpg was successful]"
print "---"
print ""

import os, glob, shutil, platform
from os import listdir
from os.path import isfile, join
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Ask user if mkdir is okay
print ""
print "---"
print "This program will copy all the current files in the directory to a new subdirectory called labeledPhotos."
print ""
print "Is this okay? (y/n): "
ans1 = str(raw_input()).lower().strip()

if ans1 == 'y':

	# Establish original photo directory
	# mypath = '/home/ack5429/Desktop/testdir'
	mypath = './'

	# Establish list of file names
	onlyfiles = sorted(glob.glob('*.jpg'))

	# Make new directory 'labeledPhotos'
	try:
		os.mkdir('./labeledPhotos')
	except OSError:
		print ""
		print "[Creation of the directory labeledPhotos failed]"
	else:
		print ""
		print "[Creation of the directory labeledPhotos was successful]"
		
	#Copy images to labeledPhotos
	try:
		for f in onlyfiles:
			shutil.copy(f, './labeledPhotos')
	except OSError:
		print ("[Copying of photos to labeledPhotos failed]")
	else:
		print ("[Copying of photos to labeledPhotos was successful]")
	
		#Copy last frame to first frame
		# Ask user if copy last to first is okay
		print ""
		print "This program will now copy the last frame to 00000001.jpg for the Box preview"
		print ""
		print "Is this okay? (y/n): "
		ans2 = str(raw_input()).lower().strip()
		
	if ans2 == 'y':
		number_of_files = len(onlyfiles)
		lastframe = onlyfiles[(number_of_files - 1)]
		shutil.copyfile(lastframe, './labeledPhotos/00000001.jpg')
		
		# Ask user if labeling is okay
		print ""
		print "This program will now label all the images in labeledPhotos with their date in the upper-left hand corner."
		print ""
		print "Is this okay? (y/n): "
		ans3 = str(raw_input()).lower().strip()
		
		if ans3 == 'y':
			# Change to labeledPhotos directory
			os.chdir('./labeledPhotos')
			
			# Establish 'number_of_files' to hold the total number of files in directory
			number_of_files = len(onlyfiles)
			print number_of_files, "total files in directory"

			# Count
			i = 0

			# Start loop
			while i<number_of_files:
				# 'curentfilename' is the original files name, 'datelabel' is the date label for the image
				currentfilename = onlyfiles[i]
				datelabel = currentfilename[:-4]
				datelabel = datelabel[4] + datelabel[5] + '-' + datelabel[6] + datelabel[7] + '-' + datelabel[:4]
				
				importimg = Image.open(onlyfiles[i])
				draw = ImageDraw.Draw(importimg)
				#font = ImageFont.truetype(<font-file>, <font-size>)
				font = ImageFont.truetype("/home/ack5429/Desktop/testdir/fonts/roboto-medium.ttf", 32)
				# draw.text((x, y),"Sample Text",(r,g,b))
				draw.text((10, 0),datelabel,(255,255,255),font=font)
				importimg.save(currentfilename)
				
				print currentfilename
				i += 1
			print "---"
		elif ans3 == 'n':
			print "---"
			exit()
	elif ans2 == 'n':
		print "---"
		exit()
elif ans1 == 'n':
	print "---"
	exit()
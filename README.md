# The Graham Center at Penn State York Contruction Timelapse
**Date:**  August-October 2019  
**Organization:** Penn State University  
**Project Members:** Myself, Dave McLaughlin (resident web developer at Penn State York), and Joe Royer ()

[Link to timelapse video (Working as of October 3rd, 2019)](https://york.psu.edu/academics/graham-fellows-program)  
[Timelapse video download link](https://github.com/alexkoontz/timelapse/blob/master/rdme_src/GrahamConstruction.mp4)

## Problem Description:
At Penn State York, there was a need for a timelapse of the contruction of a new bulding called the "Graham Center for Innovation and Collaboration."  This timelapse would be in the form of a video file **(.mp4)** and would need to be updated on a regular basis.  This video would be hosted on the Penn State York website for users to view and see the current state of the construction project.

## Brainstorming
My approach was to use a combination of the [Python programming language](https://www.python.org/), Unix shell scripting, and [Box file hosting](https://www.box.com/home) to create a system that would create a new timelapse video file daily.  This would allow for an almost real-time look into how far along the project is.

## Steps
1. Generating pictures to be compiled  
A outside webcam was set up to generate and save a picture file **(.jpg)** of the construction every day at noon to a Box file hosting folder.
1. Creating the Python scripts  
-The first python script **(InitialCopyPhotos.py)** was written to copy all of the current daily timelapse photos to a new directory, and then label them in the upper left hand corner with their creation date.  This was done using a Python library called [Pillow](https://pillow.readthedocs.io/en/stable/#),
which allows for image manipulation.  Here is an example of a labeled image.
![Labeled Photo Example](https://raw.githubusercontent.com/alexkoontz/timelapse/master/rdme_src/labelExample1.jpg)
-The second Python script **(DailyLabelNewFrame.py)** was written to run daily and find the most recent image file (i.e. the image that was generated that day).  It would take this file, label it, and save it to the directory with the other labeled photos.
1. Creating the shell script  
The shell script **(timelapse_export.sh)** was created to generate the timelapse video file.  This was done using a program called [FFmpeg](https://www.ffmpeg.org/), which can be run from a Linux terminal.  Using many parameters, the script will generate a video file at 4 frames per second at the video resolution matching the image files.  It saves this file to the current directory as *TimelapseExport.mp4*  

## Final setup
These files were put on a Linux server, which had the Box file hosting mounted to its file system.  This allowed for the server to access the images generated by the webcam, and also save the final timelapse video to the Box directory.  Every day the server would run the daily Python script, and the timelapse export script to generate the video file.  On the [Penn State York website](https://york.psu.edu/academics/graham-fellows-program), a Box preview for the file would be updated for viewing.  

## Conclusion
This project was very beneficial to improving my general programming skills and project management skills.  I was able to work and collaborate with two of my supervisors to get a final product that solved the problem I was presented with.  I made sure to keep them updated on my progress so they knew when they could expect the project to be finished.

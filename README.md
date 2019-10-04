# The Graham Center at Penn State York Contruction Timelapse
**Date:**  August-October 2019  
**Organization:** Penn State University

[Link to timelapse (Working as of October 3rd, 2019)](https://york.psu.edu/academics/graham-fellows-program)

## Problem Description:
At Penn State York, there was a need for a timelapse of the contruction of a new bulding called the "Graham Center for
Innovation and Collaboration."  This timelapse would be in the form of a video file **(.mp4)** and would
need to be updated on a regular basis.  This video would be hosted on the Penn State York website for users to view and 
see the current state of the construction project.

## Brainstorming
My approach was to use a combination of the Python programming language, Unix shell scripting, and Box file hosting to create
a system that would create a new timelapse video file daily.  This would allow for an almost real-time look into how far along the
project is.

## Steps
1. Generating pictures to be compiled  
A outside webcam was set up to generate and save a picture file **(.jpg)** of the construction every day at noon to a Box file hosting folder.
1. Creating the Python scripts
The first python script (InitialCopyPhotos.py) was written to copy all of the current daily timelapse photos to a new directory, and then label them in the upper left hand corner with their creation date.  This was done using a Python library called Pillow,
which allows for image manipulation.  

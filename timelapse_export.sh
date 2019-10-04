#! /bin/bash
# mp4 exported at 4 FPS using glob to sort image files
yes | ffmpeg -r 4 -f image2 -pattern_type glob -i "*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p ../timelapse_export.mp4

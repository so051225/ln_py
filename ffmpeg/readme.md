

# Extract video to images

ffmpeg -i test.mp4 -vf fps=1/60 output%06d.jpg

# Extract video to clips

ffmpeg -ss [start] -i test.mp4 -t [duration] -c copy out.mp4

ffmpeg -ss 4920 -i test.mp4 -t 240 -c copy out.mp4

Here, the options mean the following:

-ss specifies the start time, e.g. 00:01:23.000 or 83 (in seconds)
-t specifies the duration of the clip (same format).
Recent ffmpeg also has a flag to supply the end time with -to.
-c copy copies the first video, audio, and subtitle bitstream from the input to the output file without re-encoding them. This won't harm the quality and make the command run within seconds.

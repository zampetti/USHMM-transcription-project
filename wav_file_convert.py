import os

command2mp3 = "ffmpeg -i RG-50.030.0016.02.03.mp4 RG-50.030.0016.02.03.mp3"
command2wav = "ffmpeg -ss 0 -t 180 -i RG-50.030.0016.02.03.mp3 RG-50.030.0016.02.03.wav"

os.system(command2mp3)
os.system(command2wav)
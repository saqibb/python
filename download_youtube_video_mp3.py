# Download Youtube video in mp3 format
#### pip install pytube 
from pytube import YouTube
import os
# get yotube video url from user
ytv = YouTube(str(input("Please input the url to download: >>\n")))

# get only audio
vid = ytv.streams.filter(only_audio=True).first()

dest_path       = '.'
output_file     = vid.download(output_path=dest_path)
base,ext        = os.path.splitext(output_file)
mp3_file        = base + '.mp3'

os.rename(output_file,mp3_file)

print(ytv.title+" has been successfully downloaded")
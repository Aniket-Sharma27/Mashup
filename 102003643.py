import urllib.request
import re
import pandas as pd
import random
from pytube import YouTube
from pydub import AudioSegment
import sys
import os

if len(sys.argv) == 5:
	A = sys.argv[1]
	B = int(sys.argv[2])
	C = int(sys.argv[3])
else:
	print("Incorrect number of arguements ❌ ")

A=A.lower()
A=A.replace(" ", "")+"videosongs"

html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+A)
video_ids=re.findall(r"watch\?v=(\S{11})" , html.read().decode())

le=len(video_ids)
url = []
for i in range(B):
    url.append("https://www.youtube.com/watch?v=" + video_ids[random.randint(0,le-1)])

final_aud = AudioSegment.empty()
for i in range(B):   
  audio = YouTube(url[i]).streams.filter(only_audio=True).first()
  audio.download(filename='Audio-'+str(i)+'.mp3')
  print("\n\t\t\t\tAudio-"+str(i)+" Downloaded successfully✅")
  aud_file = str(os.getcwd()) + "/Audio-"+str(i)+".mp3"
  file1 = AudioSegment.from_file(aud_file)
  extracted_file = file1[:C*1000]
  final_aud +=extracted_file
  final_aud.export(sys.argv[4], format="mp3")

print("\n\t\t\t\t\tMashup Created ♫♫")


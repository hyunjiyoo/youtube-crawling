import pytube
import subprocess
import os

for i in range(len(videolist)):
  youtube = pytube.YouTube(videolist[i]) # 영상 가져오기
  videos = youtube.streams.filter(file_extension='mp4').all()
  print(i, videolist[i])
  parent_dir = "D:\download" # 저장할 파일 경로
  videos[0].download(parent_dir, titles[i])


default_filename = []
new_filename = []

for i in range(len(videolist)):
  default_filename.append(titles[i] + ".mp4")
  new_filename.append(titles[i] + ".mp3")
  origin_filename = str(default_filename[i])
  mp3_filename = str(new_filename[i])
  origin_path = os.path.join(parent_dir, origin_filename)
  mp3_path = os.path.join(parent_dir, mp3_filename)  
  subprocess.Popen(['ffmpeg', '-i', origin_path, mp3_path]) # mp4를 mp3로 변환
  print(i, mp3_filename)
 
print('done')

import pytube


for i in range(len(videolist)):
# 영상 가져오기
youtube = pytube.YouTube(videolist[i])
videos = youtube.streams.filter(file_extension='mp4').all()
#videos = youtube.streams.all()
print(i, videolist[i])
# 저장할 파일 경로
parent_dir = "D:\KIRBS_PT_2\download"
videos[0].download(parent_dir, titles[i])


# mp4를 mp3로 변환하기
import subprocess
import os
default_filename = []
new_filename = []
for i in range(len(videolist)):
default_filename.append(titles[i] + ".mp4")
new_filename.append(titles[i] + ".mp3")
origin_filename = str(default_filename[i])
mp3_filename = str(new_filename[i])
origin_path = os.path.join(parent_dir, origin_filename)
mp3_path = os.path.join(parent_dir, mp3_filename)
# mp4를 mp3로 변환
subprocess.Popen(['ffmpeg', '-i', origin_path, mp3_path])
print(i, mp3_filename)
print('done')

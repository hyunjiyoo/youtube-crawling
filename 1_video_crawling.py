import requests
from bs4 import BeautifulSoup as bs

html = requests.get("https://www.youtube.com/user/TEDtalksDirector/videos?view=0&sort=p&flow=grid").text
soup = bs(html, 'html.parser')


# 링크와 타이틀 가져오기
videos = soup.select('a.yt-uix-tile-link')
titles = []
for i in range(len(videos)):
  titles.append(videos[i].get_text())
  titles[i] = titles[i].replace('|', '')
  titles[i] = titles[i].replace('?', '')
  titles[i] = titles[i].replace('\'', '')
  titles[i] = titles[i].replace(',', '')
  titles[i] = titles[i].replace('.', '')
  titles[i] = titles[i].replace(' ', '_')
  
# url과 추출한 link 합치기
videolist = []
for v in videos:
  tmp = 'https://www.youtube.com' + v['href']
  videolist.append(tmp)

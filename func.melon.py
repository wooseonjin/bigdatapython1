import requests
from bs4 import BeautifulSoup
import random
import time

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'

# 헤더 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 아티스트를 담을 리스트
songs = []

# 멜론 차트 정보 추출
for entry in soup.select('tr.lst50, tr.lst100'):
    try:
        rank = entry.select_one('span.rank').get_text()
        title = entry.select_one('div.ellipsis.rank01 a').get_text()
        artist = entry.select_one('div.ellipsis.rank02 a').get_text()
        songs.append((rank, title, artist))
    except AttributeError:
        continue  # 요소를 찾지 못하면 무시

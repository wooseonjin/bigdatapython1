import requests
from bs4 import BeautifulSoup
import random
import time

print("==========================")
print("| 1. 멜론 차트 TOP 100곡  |")
print("| 2. 멜론 차트 TOP 50곡   |")
print("| 3. 멜론 차트 TOP 10곡   |")
print("| 4. 멜론 차트 AI 추천곡  |")
print("| 5. 가수 이름 검색       |")
print("| 6. 파일에 저장(멜론 100)|")
print("==========================")

a = "<멜론 차트 TOP 100곡>"
b = "<멜론 차트 TOP 50곡>"
c = "<멜론 차트 TOP 10곡>"
d = "<멜론 차트 AI 추천곡>"
e = "<가수 이름 검색>"

n = input("[원하시는 서비스에 해당하는 번호를 입력하세요.]: ")
if n == "1":
    print("멜론100을 출력하는 기능")

elif n == "2":
    print(b)
    time.sleep(1)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 50:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()

        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')
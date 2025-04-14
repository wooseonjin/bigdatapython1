import requests
from bs4 import BeautifulSoup
import time

def m100(a):
    print(a)
    time.sleep(1)

url = 'https://www.melon.com/chart/index.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.select('tr[data-song-no]')

for index, song in enumerate(songs):
    if index >= 100:  # 원하는 만큼 자를 수 있어요
        break

    rank = song.select_one('span.rank').text.strip()
    title = song.select_one('div.ellipsis.rank01 a').text.strip()
    artist = song.select_one('div.ellipsis.rank02 a').text.strip()

    print(f"{rank}위 | 제목: {title} | 아티스트: {artist}")

def m50(a):
    print(a)
    time.sleep(1)

url = 'https://www.melon.com/chart/index.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.select('tr[data-song-no]')

for index, song in enumerate(songs):
    if index >= 100:  # 원하는 만큼 자를 수 있어요
        break

    rank = song.select_one('span.rank').text.strip()
    title = song.select_one('div.ellipsis.rank01 a').text.strip()
    artist = song.select_one('div.ellipsis.rank02 a').text.strip()

    print(f"{rank}위 | 제목: {title} | 아티스트: {artist}")

def m10(a):
    print(a)
    time.sleep(1)

url = 'https://www.melon.com/chart/index.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.select('tr[data-song-no]')

for index, song in enumerate(songs):
    if index >= 100:  # 원하는 만큼 자를 수 있어요
        break

    rank = song.select_one('span.rank').text.strip()
    title = song.select_one('div.ellipsis.rank01 a').text.strip()
    artist = song.select_one('div.ellipsis.rank02 a').text.strip()

    print(f"{rank}위 | 제목: {title} | 아티스트: {artist}")

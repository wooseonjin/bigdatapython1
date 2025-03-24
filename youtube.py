import requests
from bs4 import BeautifulSoup

# 유튜브 인기 급상승 동영상 페이지 URL
url = 'https://www.youtube.com/feed/trending?hl=ko&gl=KR'

# HTTP 요청을 보내고 페이지 콘텐츠를 가져오기
response = requests.get(url)

# 페이지가 성공적으로 열렸는지 확인
if response.status_code == 200:
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 인기 급상승 동영상의 제목과 링크를 추출하기
    videos = soup.find_all('h3', class_='title-and-badge')
    
    for video in videos:
        title = video.find('a').text.strip()
        link = 'https://www.youtube.com' + video.find('a')['href']
        print(f'제목: {title}, 링크: {link}')
else:
    print('페이지를 열 수 없습니다.')
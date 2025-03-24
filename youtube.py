import requests
from bs4 import BeautifulSoup

# url 설정
url = 'https://www.youtube.com/feed/trending'

# 요청 보내기
response = requests.get(url)
response.raise_for_status()  # 요청이 성공했는지 확인

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 인기 급상승 동영상 가져오기
videos = soup.find_all('ytd-video-renderer')

# 각 동영상의 제목, 링크, 조회수, 업로드 날짜 출력
for video in videos:
    title = video.find('a', {'id': 'video-title'})   # 동영상 제목
    view_count = video.find('span', {'class': 'view-count'})  # 조회수
    upload_date = video.find('div', {'id': 'metadata-line'}).find_all('span')  # 업로드 날짜
    
    if title and view_count and upload_date:
        print(f'제목: {title.get_text().strip()}')
        print(f'링크: {"https://www.youtube.com" + title["href"]}')
        print(f'조회수: {view_count.get_text()}')
        print(f'업로드 날짜: {upload_date[1](https://www.youtube.com/feed/trending?hl=ko&gl=KR "youtube.com").get_text()}')
        print('---')
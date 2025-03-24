
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome 드라이버 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창 없이 실행
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ChromeDriver 경로 (필요시 경로 변경)
service = Service("chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 유튜브 인기 급상승 페이지 접속
url = "https://www.youtube.com/feed/trending"
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)

# 동영상 제목 가져오기
titles = driver.find_elements(By.CSS_SELECTOR, "h3.style-scope.ytd-video-renderer")

# 조회수 가져오기
views = driver.find_elements(By.CSS_SELECTOR, "span.inline-metadata-item.style-scope.ytd-video-meta-block")

# 결과 저장 및 출력
trending_videos = []
for i in range(len(titles)):
    title = titles[i].text
    if i * 2 + 1 < len(views):  # 조회수만 필터링 (조회수와 업로드 날짜가 같이 있음)
        view_count = views[i * 2 + 1].text
        trending_videos.append(f"{i+1}위: {title} - {view_count}")

# 출력
for video in trending_videos:
    print(video)

# 브라우저 종료
driver.quit()

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

# 멜론 차트 페이지 접속
url = "https://www.melon.com/chart/index.htm"
driver.get(url)

# 페이지 로딩 대기
time.sleep(3)

# 곡 제목 가져오기
titles = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank01 > span > a")
# 아티스트 가져오기
artists = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank02 > span")

# 결과 저장 및 출력
melon_chart = []
for i in range(len(titles)):
    rank = i + 1
    title = titles[i].text
    artist = artists[i].text
    melon_chart.append(f"{rank}위: {title} - {artist}")

# 출력
for song in melon_chart:
    print(song)

# 브라우저 종료
driver.quit()

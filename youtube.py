from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버를 설정하고 헤드리스 모드로 실행
options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 유튜브 인기 급상승 동영상 페이지로 이동
url = 'https://www.youtube.com/feed/trending'
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)  # 5초 대기

# 인기 동영상 정보 추출
videos = driver.find_elements(By.XPATH, '//*[@id=
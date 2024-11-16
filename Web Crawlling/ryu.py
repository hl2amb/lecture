from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

user_id = "hl2amb"
user_pw = "Puteaux54##"

# 드라이버 생성
driver = webdriver.Firefox()
driver.maximize_window()

# 1. 로그인 페이지 이동
driver.get(r"https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(2)

# 2. 아이디 입력
id = driver.find_element(By.CSS_SELECTOR, "#id")
pyperclip.copy(user_id)
id.send_keys(Keys.COMMAND, 'v')
time.sleep(2)

# 3. 비밀번호 입력
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pyperclip.copy(user_pw)
pw.send_keys(Keys.COMMAND, 'v')
time.sleep(2)

# 4. 로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, ".btn_login").click()
time.sleep(10)
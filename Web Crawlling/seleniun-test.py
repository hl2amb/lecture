# selenium 4.6 이상에서는 chromedriver를 따로 설치해줄 필요가 없다
# pip install --upgarde selenium

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://comic.naver.com/webtoon')

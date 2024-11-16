import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pyautogui

keyword = pyautogui.prompt(text = '검색어를 입력하시오', title ="Message", default = '입력하세요')

url_search = f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}'
response = requests.get(url_search).text
soup = BeautifulSoup(response, 'html.parser')

articles = soup.select('.news_tit')
for article in articles:
    print(article.text)








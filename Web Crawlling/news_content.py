import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

links =soup.select('.news_tit')
# pprint.pprint(links)
for link in links:
    title = link.text
    url = link.get('href')
    print(title, url)

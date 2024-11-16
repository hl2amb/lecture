import requests as req
from bs4 import BeautifulSoup
import os
import openpyxl
import pyautogui

# keyword = pyautogui.prompt(text = '검색어를 입력하시오', title ="Message", default = '입력하세요')

page_num = 0
news_title_list =[]
news_content_list = []


url ='https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=kf-&qdt=0&ie=utf8&query=kf-21'
response = req.get(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(response.text, 'html.parser')
selections = soup.find('div', class_='info_group')

titles = selections.find_all ('a', '.news_tit.title')
links = selections.find_all('a', href = True)

print(selections)
print(titles)

# for index in range(min(len(titles), len(links))):
#     print(f'기사번호 : {index + 1}')
#     print(f'헤드라인 : {titles[index].get_text().strip()}')
#     print(f"링크 : {links[index]['href']}")
#     print(f"[기사원문] {links[index].get_text().strip()}")
#     # for link in links:
#     #     text = link.get_text().strip()
#     #     pprint.pprint(f"[본문내용]{text}")
#     print()
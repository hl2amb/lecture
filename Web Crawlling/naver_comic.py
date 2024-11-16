import requests
from newspaper import Article
from selenium import webdriver
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}


url ='https://www.bbc.com/portuguese'
res = requests.get(url, headers=headers)
res.raise_for_status()
# print('응답코드 :', res.status_code)
# if res.status_code == requests.codes.ok:
#     print('request 요청이 정상 처리 되었습니다.')
# else:
#     print("오류가 발생했습니다. 에러코드 ;", res.status_code)

soup = BeautifulSoup(res.text, 'lxml')
fs = soup.find_all('li', {'class':'bbc-jw2yjd'})

link = fs[1].a['href']
content = Article(link)
content.download()
content.parse()

# 기사 내용 출력
print('기사 내용 :')
print(content.text, end='')

# with open('news.txt', 'w', encoding='utf-8-sig') as file:
#     file.write(content.text)




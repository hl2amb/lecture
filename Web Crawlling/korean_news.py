 import requests
from bs4 import BeautifulSoup

url = 'https://media.naver.com/press/437#SpecialReport'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

sections = soup.find('ul', class_='ofra_list')
titles = sections.find_all('div', 'ofra_list_tx_headline')

for index, title in enumerate(titles):
    print(index +1, title.get_text())


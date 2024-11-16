import requests
from bs4 import BeautifulSoup
from newspaper import Article

search = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=kf-21&oquery=kf-21&tqi=iA%2Bn7lqVN8VsshH3deNssssstP4-083634'
html = requests.get(search).text
soup = BeautifulSoup(html, 'html.parser')

# links = soup.select('.news_tit')
links = soup.find_all('a', class_='news_tit')

i = 0
for link in links:
    title = link.text
    url = link.get('href')
    print(i+1, title, url)
    print('[기사원문]')
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    # article = Article(url)
    # article.download()
    # article.parse()
    # text = soup.find('div', class_='main_text').text.strip()
    # print(article.text)
    i+=1

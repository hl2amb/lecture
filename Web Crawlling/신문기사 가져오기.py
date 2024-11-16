from newspaper import Article
from bs4 import BeautifulSoup

# 파싱할 뉴스 기사 주소
url = 'https://search.folha.uol.com.br/search?q=coreia+do+sul&periodo=24&sd=&ed=&site=todos'

# 언어가 한국어이므로 language='ko'로 설정
article = Article(url)
article.download()
article.parse()

# 기사 내용 출력
print('기사 내용 :')
print(article.text)

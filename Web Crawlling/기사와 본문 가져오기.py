import requests

from bs4 import BeautifulSoup
import time
import pprint

url = 'https://www.bbc.com/search?q=south%20korea&edgeauth=eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJrZXkiOiAiZmFzdGx5LXVyaS10b2tlbi0xIiwiZXhwIjogMTcxNDAwOTIwNSwibmJmIjogMTcxNDAwODg0NSwicmVxdWVzdHVyaSI6ICIlMkZzZWFyY2glM0ZxJTNEc291dGglMjUyMGtvcmVhIn0.-m2NWVurz0AqfToJsLMS0lb2rcj9oYf_s-mvpC42k28'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

article_container = soup.find('div', class_='sc-32f23d22-2 iumrhG')

titles = article_container.find_all('h2')
links = article_container.find_all('a', href=True)


# for index in range(min(len(titles), len(links))):
#     title = titles[index].get_text().strip()
#     link = links[index]['href']
#     print(index+1, title, link)
#
# head_lines = []
# for index in range(min(len(titles), len(links))):
#     title = titles[index].get_text().strip()
#     link = links[index]['href']
#     head_lines.append([title, link])
#
# pprint.pprint(head_lines)

for index in range(min(len(titles), len(links))):
    print(f'기사번호 : {index + 1}')
    print(f'헤드라인 : {titles[index].get_text().strip()}')
    print(f"링크 : {links[index]['href']}")
    print(f"[기사원문] {links[index].get_text().strip()}")
    # for link in links:
    #     text = link.get_text().strip()
    #     pprint.pprint(f"[본문내용]{text}")
    print()

import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/portuguese/articles/czkznyzn5rko'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

sections = soup.find('div', class_='bbc-1cvxiy9')
texts = sections.find_all('p', 'bbc-hhl7in e17g058b0')

for t in texts:
    print(t.get_text())

with open('output.txt', 'a') as file:
        for t in texts:
            file.write(f'{t.get_text()}\n')
import requests
from bs4 import BeautifulSoup

url = 'https://startcoding.pythonanywhere.com/basic'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.select('.product')

# 하위태그를 분리하는 방식
for index, item in enumerate(items):
    category = item.select_one('.product-category').get_text()
    name = item.select_one('.product-name').get_text()
    price = item.select_one('.product-price')
    if price.find('del'):                           # 하위 불 필요한 태그 지우기
        price.find('del').decompose()

    print(f'{index+1} {category}  {name}  {price.text.strip()}')

print()

# split 함수를 이용하는 방식
for index, item in enumerate(items):
    category = item.select_one('.product-category').get_text()
    name = item.select_one('.product-name').get_text()
    price = item.select_one('.product-price').text.split('원')[0]
    print(f'{index+1} {category}  {name}  {price}')
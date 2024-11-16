import requests
from bs4 import BeautifulSoup

url = 'https://startcoding.pythonanywhere.com/basic'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# print('하나의 상품 가져오기')# 한개의 상품 크롤링하기
# print()
# category = soup.select_one('.product-category').get_text()
# name = soup.select_one('.product-name').get_text()
# price = soup.select_one('.product-price').get_text()
# print(f'{category}  {name}  {price}')

print('\n 여러개의 상품 가져오기')
items = soup.select('.product')
for index, item in enumerate(items):
    category = item.select_one('.product-category').get_text()
    name = item.select_one('.product-name').get_text()
    price = item.select_one('.product-price').get_text()
    print(f'{index+1} {category}  {name}  {price}')



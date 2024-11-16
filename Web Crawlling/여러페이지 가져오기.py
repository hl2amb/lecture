import requests
from bs4 import BeautifulSoup

global_index = 1
for i in range(1,5):

    url = f'https://startcoding.pythonanywhere.com/basic?page={i} '
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('.product')

    for item in items:
        category = item.select_one('.product-category').get_text()
        name = item.select_one('.product-name').get_text()
        price = item.select_one('.product-price').text.split('원')[0]
        print(f'{global_index} {category}  {name}  {price}')
        global_index += 1
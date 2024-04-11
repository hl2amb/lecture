from bs4 import BeautifulSoup

# xml 데이터에서 원하는 값만 추출하기
with open('users.xml', 'r', encoding='utf-8-sig') as f:
    soup = BeautifulSoup(f, 'lxml')
    users = soup.find_all( 'user')

    for user in users:
        print(f"Name: {user.find('name').text}, Age: {user.find('age').text}")

        # users = soup.select('user')
        # print(f"이름: {user.select_one('name').text}, 나이: {user.select_one('age').text} ")

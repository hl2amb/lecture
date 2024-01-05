# Hello Word! 10번 프린트 하기
i = 1
while i < 10:
    print('Hello World!, {}'.format(i) )
    i += 1

# Jane 이 올 때까지 계속 손님 호충하기
customer = 'Jane'
person = 'unknown'
while person != customer :
    print(f'{customer}, your coffee is ready!')
    person = input('what is your name?: ')

# while 문에서 강제로 빠져 나가기 break

money = 300
coffee = 10
while money :
    print('You got a coffee!')
    coffee = coffee -1
    print(f'availbale coffee: {coffee}')
    if coffee == 0:
        print('Sold out')
        break

# while 문 맨 앞으로 보내기 continue
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0 : continue
    print(a)

# index를 이용한 출력문 반복하기
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
index = 0

while index < len(rainbow):
    print(rainbow[index])
    index += 1

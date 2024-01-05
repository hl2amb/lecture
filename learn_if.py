# 몸무게 측정
w = int(input('Enter ur weight : '))
if  50 <= w <= 59:
    print('저체중')
elif 60 <= w <= 80:
    print('정상')
elif 80 <= w <= 100:
    print('비만')
else :
    print('비정상')

# 성별과 대소문자 1
gender = input('Enter your gender (M/F) : ')
# gender = input('Enter your gender (M/F) : ').upper()
if gender == 'M' :
    print('멋있어요')
else :
    print('예뻐요')

# 논리 연산자 사용하기
if gender == 'M' or gender == 'm':
    print('멋있어요')
else :
    print('예뻐요')

# in, not in 을 이용한 조건문

list = ['apple','banana','grape','orange']
if 'apple' in list:
    print(True)
else:
    print(False)


# 아무것도 않하기 pass
items =['black-ballpen', 'computer pen']
if 'computer pen' in items: pass
else: print('손을 드세요')

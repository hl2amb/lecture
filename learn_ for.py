# 리스트 항목에서 문자의 길이가 red 보단 긴 항목만 순차적 출력

colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
print(len(colors))
print(colors)

for color in colors:
        if len(color) > len(colors[0]) :
            print(color)

# for 문 안에 if 문 사용 하기
grades =[90, 80, 70, 60, 50, 40]
number = 0
for grade in grades:
    number = number + 1
    if grade >= 70 :
        print(f'{number} 학생은 시험에 통과 하셨 습니다.')
    else :
        print(f'{number} 학생은 재시험 대상 입니다.')

# for 문에서 continue 사용
grades =[90, 80, 70, 60, 50, 40]
number = 0
for grade in grades:
    number = number + 1
    if grade <= 69 : continue
    print(f'축하합니다. {number} 학생은 시험에 통과 하셨 습니다.')

# for와 range를 이용한 구구단 만들기

for i in range(2,10) :
    for j in range(1,10) :
        print(f'{i}*{j} = {i*j}', end= ' ')
    print('')




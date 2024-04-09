# 파일 생성
with open ('data.txt', 'w') as f:
    f.write('Hello World\n')
    f.write("I'm your Python\n")
    f.write("I like Python")

test = open('text.txt', 'w')
test.write('Hello World')
test.close()

with open('plain_text.txt', 'w') as file:
    for i in range(1,6):
        data = f'Your text is {i}!\n'
        file.write(data)

# 파일 읽기 readlines()
with open('plain_text.txt', 'r') as file:
    data = file.readlines()
    print(data)

with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# 줄바꿈 문자(\n) 제거하고 출력하기
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        print(line)

with open('plain_text.txt', 'r') as file:
    data =file.readlines()
    for line in data:
        print(line.strip())

# readline()으로 읽어 오기
with open('data.txt', 'r') as file:
    line = file.readline()
    print(line)
    line2 = file.readline()
    print(line2)
    line3 = file.readline()
    print(line3)

# readline()으로 모든 행 가져 오기
with open('data.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line: break
        print(line)

# read()로 읽기
with open('plain_text.txt', 'r') as file:
    text = file.read()
    print(text)
    print(type(text))

# 파일에 내용 추가하기
with open('data.txt', 'a') as file:
    file.write("\nEverything is fine\n")
    # file.close()

with open('data.txt', 'r') as file:
    text = file.read()
    print(text)
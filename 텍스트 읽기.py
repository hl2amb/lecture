# 파일 읽기
with open('new.txt', 'r', encoding='utf-8') as file:
    # text = file.read()
    print(text)

# readline()으로 한 줄씩 읽어오기 : 문자열로 반환해 줌
with open('en_news.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
print(type(line))

# readlines()로 읽어오기 : 각 줄을 요소로 리스트 형태로 반환
with open('en_news.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
print(type(lines))

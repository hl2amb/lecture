# 텍스트 파일 생성 / open()
file = open('new.txt','w', encoding='utf-8')

# 텍스트 파일 생성 / with open()
with open('new.txt', 'w', encoding='utf-8') as file:
    # 생성된 파일에 내용 쓰기
    text = "Hi!, My Phone Number is 123-456-7890. My Email is <email@kmail.com> OK?"
    file.write(text)

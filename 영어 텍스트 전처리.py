# en_text.txt 파일 읽어 오기
with open('en_news.txt','r',encoding='utf-8') as f:
    text = f.read()
    print(text)

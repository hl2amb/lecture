### 테스트 불러오기, 전처리 ###
# 텍스트 1 에서 2자 미만의 글자 제외 하기
from nltk.tokenize import word_tokenize

with open('doc1.txt', 'r', encoding= 'utf-8-sig') as f1:
    raw_doc1 = f1.read()
    # print(raw_doc1)

w_token1 = word_tokenize(raw_doc1)
text1 = []
for word in w_token1:
    if len(word) > 2 :
        text1.append(word)
# print(text1)

# 텍스트 3 에서 2자 미만의 글자 제외하기

with open('doc3.txt', 'r', encoding= 'utf-8-sig') as f3:
    raw_doc3 = f3.read()
    # print(raw_doc3)

w_token3 = word_tokenize(raw_doc3)
text3 = []
for word in w_token3:
    if len(word) > 2 :
        text3.append(word)
# print(text3)

print('텍스트1의 크기:',len(text1), '텍스트3의 크기:',len(text3))

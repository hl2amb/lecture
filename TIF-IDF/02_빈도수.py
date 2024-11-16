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
print('텍스트 전처리 후 결과')
print('텍스트1의 크기:',len(text1), '텍스트3의 크기:',len(text3))

# 테스트1의 빈도수

from collections import Counter # Counter 함수는 빈도수가 높은 단어부터 보여 준다

fq_text1 = Counter(text1)
print('텍스트1에 드장한 단어의 빈도수 :', fq_text1)

# 텍스트3의 term frequency
fq_text3 = Counter(text3)
print('텍스트3에 등장한 단어의 빈도수 :', fq_text3)

# for와 if 구문을 사용한 단어 빈도수를 계산
frequency = {}
for word in text1:
    if word not in frequency:
        frequency[word] = 0  # 새로운 단어는 먼저 0로 초기화한 후
    frequency[word] += 1     # +1씩 증가 시킨다.

print('for와 if 구문으로 만든 text1의 단어 빈도수 ')
print(frequency)
print(frequency['gaza'])

# 빈도수 높은 순으로 정렬하기
frequency_sorted = sorted(frequency.items(), key = lambda x:x[1], reverse= True)
print('높은 빈도수로 출력')
print(frequency_sorted)

# 정수 인코딩
encode1 = {}
i = 0
for (x, y) in frequency_sorted :
    if y > 1 :
        i = i + 1
        encode1[x] = i

print('정수 인코딩 출력: ', encode1)
print()

# 데이타프레임 출력
import pandas as pd
word_indexing = pd.DataFrame.from_dict(encode1, orient='index', columns=['Count']).reset_index()
word_indexing.columns = ['Words', 'Given Index']
print('데이타 프레임 출력')
print(word_indexing.T)

# 상위 빈도수 단어 7개 출력 하기
index_size = 7
w_freq = [word for word, index in encode1.items() if index <= index_size]
print('상위 빈도수 단어 7 개 :')
print(w_freq)

# 상위 7개 단어만 보기




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

######## 텍스트1의 term frequency ##########

from collections import Counter

fq_text1 = Counter(text1)
# print('텍스트1에 드장한 단어의 빈도수 :', fq_text1)

# 텍스트3의 term frequency
fq_text3 = Counter(text3)
# print('텍스트3에 등장한 단어의 빈도수 :', fq_text3)

####### TF를 DTM으로 표현하기 - 단어와 빈도수를 dataFrame으로 만듬, word embedding이 아남 #########

import pandas as pd
print(type(fq_text1))

# 자료형식 class.Collection.Counter를 DataFrame으로 만들기

df_1 = pd.DataFrame.from_dict(fq_text1, orient='index', columns=['Count']).reset_index()

# 열 이름 변경

df_1.columns = ['Item', 'Count']
print(df_1)

# reshape : 119*2 를 2*119로 변형하기
df_transposed = df_1.T
print(df_transposed)

df_3 = pd.DataFrame.from_dict(fq_text3, orient='index', columns=['Count']).reset_index()
df_3.columns = ['단어', '빈도수']
df_3_reshape =df_3.T
print(df_3_reshape)

##### word embedding, - indexing - 하기 #####
# doc1 워드 indexing

indexedword1 = {}  # 단어와 해당 인덱스를 매핑할 딕셔너리
bow = []  # BoW를 저장할 리스트

for word in fq_text1:
    if word not in indexedword1.keys():  # 단어가 처음 등장한 경우, 인덱스를 부여하고 BoW에 1을 추가
        indexedword1[word] = len(indexedword1)
        bow.insert(len(indexedword1) - 1, 1)

    # 이미 등장한 단어의 경우, 해당 인덱스 위치의 BoW 값에 1을 추가
    else:
        index = indexedword1.get(word)
        bow[index] = bow[index] + 1

print('텍스트1에 등장한 단어와 단어에 부여된 인덱스 :')
print(indexedword1)


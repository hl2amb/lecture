# Term Frequency : 하나의 document에서 특정 단어의 빈도수
import pandas as pd
from math import log

doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
doc4 = 'São como o cão e o gato'

docs = [doc1, doc2, doc3, doc4]
print(docs)

# 총 문서의 수
D = len(docs)

# 문서내 단어 집합, 복수의 문서로 부터 단어를 추출하는 방법
# vocas =list(w for doc in docs for w in doc.split()) #합쳐진 문서의 단어를 중복가능한 리스트로 변환

vocas =[]
for doc in docs:
    for word in doc.split():
        vocas.append(word)

print(vocas)

# 전체 문서에 등장한 단어의 빈도수
print('cão의 Term Frequency:', vocas.count('cão'))

#전체 문서에서 TF
#
# def atf(t, d):
#     wf = 0
#     for doc in docs:
#        for t in doc:
#             wf += 1
#             #print(wf)
#     return wf
#
# print('바나나의 Term Frequency:', atf('바나나', doc1))

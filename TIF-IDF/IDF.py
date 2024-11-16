import pandas as pd
from math import log

doc1 = '먹고 싶은 사과'
doc2 = '먹고 싶은 바나나'
doc3 = '길고 노란 바나나 바나나'
doc4 = '저는 과일이 좋아요'

docs = [doc1, doc2, doc3, doc4]

D = len(docs)

#IDF(역문서빈도) 공식: 𝑖𝑑𝑓(𝑡, 𝐷) = log( |𝐷|/1 + 𝑑𝑓 (𝑡, 𝐷 ))

def idf(t):
    df = 0
    for doc in docs:
        df += t in doc  # doc에 t가 있는지 확인
    return log(D / (df + 1))
    # IDF의 다른 계산 방법
    # return log((D + 1) / (df + 1)) + 1


print('사과의 IDF 값:', idf('사과'))
print('바나나의 IDF 값:', idf('바나나'))
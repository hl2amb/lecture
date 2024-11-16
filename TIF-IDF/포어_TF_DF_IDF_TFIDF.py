import pandas as pd
from math import log

doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
doc4 = 'São como o cão e o gato'

docs = [doc1, doc2, doc3, doc4]

docs = [doc1, doc2, doc3, doc4]


# 총 문서의 수
D = len(docs)

# 문서 d 내에서 단어 t의 빈도(TF)를 계산
def tf(t, d):
    return d.count(t)

# 단어 t의 역문서 빈도(IDF)를 계산
def idf(t):
    df = 0
    for doc in docs:
        df += t in doc  # doc에 t가 있는지 확인
    return log(D / (df + 1))
    # IDF의 다른 계산 방법
    # return log((D + 1) / (df + 1)) + 1

# TF-IDF 점수 계산
def tfidf(t, d):
    return tf(t, d) * idf(t)

# 문서 내에 등장하는 단어의 집합
vocas = list(set(w for doc in docs for w in doc.split()))
# print(vocas)

result = []  # 결과를 저장할 리스트

for doc in docs:
    result.append([])
    for voca in vocas:
        result[-1].append(tf(voca, doc))  # TF 값을 결과에 추가

tf_score = pd.DataFrame(result, columns=vocas)
print(tf_score)

result_idf = []  # 결과를 저장할 리스트

for voca in vocas:
    result_idf.append(idf(voca))  # IDF 값을 결과에 추가

idf_score = pd.DataFrame(result_idf, index=vocas, columns=["IDF"])
print(idf_score)

# TF*idf
result_tf_idf  = []

for doc in docs:
    result_tf_idf.append([])
    for voca in vocas:
        result_tf_idf[-1].append(tfidf(voca, doc))  # TF-IDF 값을 결과에 추가

tfidf_score = pd.DataFrame(result_tf_idf, columns=vocas)
print(tfidf_score)
import pandas as pd

doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
doc4 = 'São como o cão e o gato'

docs = [doc1, doc2, doc3, doc4]
print(docs)

# 문서내 단어 집합, 복수의 문서로 부터 단어를 추출하는 방법

# vocas = []
# for doc in docs:
#     for word in doc.split():
#         vocas.append(word)

vocas =list(w for doc in docs for w in doc.split()) # 복수의 문서에서 단어를 추출해서 리스트 형태로 반환
print('단어 리스트: ', vocas)

# 전체 문서에 등장한 단어의 빈도수
print('cão의 Term Frequency:', vocas.count('cão'))

from collections import defaultdict

import pandas as pd

# 예제 문서 집합
doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
doc4 = 'São como o cão e o gato'

docs = [doc1, doc2, doc3, doc4]

def doc_frequency(documents):
    # 각 단어가 등장한 문서의 수를 저장할 딕셔너리
    df = defaultdict(int)

    # 각 문서에서 고유 단어를 추출하여 카운트
    for document in documents:
        words = set(document.split())
        for word in words:
            df[word] += 1

    return df


# 문서 빈도 계산
document_frequency = doc_frequency(docs)
table =pd.DataFrame(list(document_frequency.items()), columns=['word', 'frequency'])
print(table)



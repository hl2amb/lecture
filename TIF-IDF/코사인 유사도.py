from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
# import numpy as np
from numpy import dot
from numpy.linalg import norm
from IPython.display import display
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

cv = CountVectorizer()

doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
docs = [doc1, doc2, doc3]

# 희소행렬 변환
dtm = cv.fit_transform(docs)

# 문서별 어휘와 빈도수 테이블(행렬)로 표시
names = cv.get_feature_names_out()
count_words = pd.DataFrame(dtm.toarray(), columns=names)
display(count_words)

# 유사도 구히기 함수 정의
def cos_sin(A, B):
    return dot(A, B) / (norm(A) * norm(B))

# Computing pairwise cosine similarities
similarities = pd.DataFrame(index=[f'Doc{i+1}' for i in range(len(docs))],
                            columns=[f'Doc{i+1}' for i in range(len(docs))])

for i in range(len(docs)):
    for j in range(len(docs)):
        similarities.iloc[i, j] = cos_sin(dtm.toarray()[i], dtm.toarray()[j])

print("문서 간 코사인 유사도:")
print(similarities)


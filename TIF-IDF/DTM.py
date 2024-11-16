from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from IPython.display import display

cv = CountVectorizer()
doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
docs = [doc1, doc2, doc3]

# 문서를 희소행렬 변환
dtm = cv.fit_transform(docs)
print('희소행렬 출력')
print(dtm.toarray())
print()

# 희소행렬을 dense dense matrix로 변환
dtm_dense = dtm.todense()
print('dense matrix 출력')
print(dtm_dense)
print()

# densematrix를 df로 변환
dtm_df = pd.DataFrame(dtm_dense, columns=cv.get_feature_names_out())
print(dtm_df)
print()

# 모든 단어 출력하기
print('모든 어휘항목 출력하기')
names = cv.get_feature_names_out()
print(names)
print()

# dense matrix를 상관항렬로 변환
print('상관행렬로 변환')
correlation_matrix = np.corrcoef(dtm_dense, rowvar=0)
print(correlation_matrix)
print()

# 단어의 인덱스 값 출력하기
print('단어의 벡터 위치 값 표시 -- 빈도수 표시가 아님')
print(cv.vocabulary_)
print()

# 단어와 빈도수를 df 로 출력하기
print("어휘 빈도수 표시: ")
names = cv.get_feature_names_out()
count_words = pd.DataFrame(dtm.toarray(), columns=names)
display(count_words)
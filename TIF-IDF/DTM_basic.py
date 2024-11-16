from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from IPython.display import display
pd.set_option('display.max_columns', None)  # 행과 열을 생략 없이 모두 보여주는 옵션
pd.set_option('display.max_rows', None)

cv = CountVectorizer()

doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'

docs = [doc1, doc2, doc3]

# 문서를 희소행렬 변환
dtm = cv.fit_transform(docs)

# 단어와 빈도수를 df 로 출력하기
print("어휘 빈도수 표시: ")
names = cv.get_feature_names_out()
count_words = pd.DataFrame(dtm.toarray(), columns=names)
display(count_words)

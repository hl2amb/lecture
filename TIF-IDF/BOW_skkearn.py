from sklearn.feature_extraction.text import CountVectorizer

doc = ['Cão mordido de cobra tem medo até de corda']

# 인덱스와 빈도수 계산 모델
vectorizer = CountVectorizer()

# vectorizer를 doc 학습 및 변환
bow = vectorizer.fit_transform(doc)

print('word index:', vectorizer.vocabulary_)
print(bow.toarray())

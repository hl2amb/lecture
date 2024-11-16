from sklearn.feature_extraction.text import CountVectorizer
from IPython.display import display
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer()

doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
docs = [doc1, doc2, doc3]

# 희소행렬 변환
dtm = cv.fit_transform(docs)

cos_sim = cosine_similarity(dtm.toarray(), dtm.toarray())
display(cos_sim)



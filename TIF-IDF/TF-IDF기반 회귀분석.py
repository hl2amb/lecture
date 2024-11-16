from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

tfidf = TfidfVectorizer(max_features=2000, min_df=5, max_df=0.5)

categories = ['comp.graphics', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train',
                                      remove=('headers', 'footers', 'quotes'),
                                      categories=categories)

newsgroups_test = fetch_20newsgroups(subset='test',
                                     remove=('headers', 'footers', 'quotes'),
                                     categories=categories)
X_train = newsgroups_train.data
y_train = newsgroups_train.target

X_test = newsgroups_test.data
y_test = newsgroups_test.target

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

print(X_train_tfidf[0].toarray())

# TF-IDF 기반 feature 벡터를 이용한 로지스틱 회귀 적합

LR_clf_tfidf = LogisticRegression(max_iter=1000, random_state=3002)
LR_clf_tfidf.fit(X_train_tfidf, y_train)

print('# Training accuracy: {:.3f}'.format(LR_clf_tfidf.score(X_train_tfidf, y_train)))
print('# Test accuracy: {:.3f}'.format(LR_clf_tfidf.score(X_test_tfidf, y_test)))
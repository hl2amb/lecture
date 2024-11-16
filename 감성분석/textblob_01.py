
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
blob = TextBlob(text)

for sentence in blob.sentences:
   print("문장별 극성: ", sentence.sentiment.polarity)


# 단어 단위로 감성 분석
# for word in blob.words:
#     word_blob = TextBlob(word)
#     print(f"Word: {word}, Polarity: {word_blob.sentiment.polarity}")

print("문서의 극성 정도: ", blob.sentiment.polarity)
print("문서의 주관성 정도: ", blob.sentiment.subjectivity)
from textblob import TextBlob

text = "This film is bad but the action was so good. And the actress was my favorite. I pretty like this movie."

blob = TextBlob(text)

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)

for word in blob.words:
    word_blob = Text
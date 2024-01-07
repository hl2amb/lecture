from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize

with open('COREIA DO NORTE.txt', 'r', encoding='utf-8-sig') as f:
   raw_text = f.read()

# 단어 토큰화
tokens = wordpunct_tokenize(raw_text)
print('wordpunct tokens: ', tokens)
print('중복 포함한 단어 수: ', len(tokens))

# 빈도수
from collections import Counter
frequency = Counter(tokens)
print(frequency)
print()

# 문장 토큰화
from nltk.tokenize import sent_tokenize

sentences = sent_tokenize(raw_text)  #list 형식으로 반환해 줌
for sentence in sentences:
    print(sentence)

print('문장의 수: ', len(sentences))


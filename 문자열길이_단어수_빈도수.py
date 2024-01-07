
text= 'Os disparos da Coreia do Norte, segundo o exército da Coreia do Sul, não causaram danos civis ou militares.'

# 문장의 길이 : 문장이 갯수가 아니라 문자열의 길이다
print('text 문자열의 길이: ', len(text))
# print()

# 단어의 갯수:
# words_count = text.split()
import re
# # words_count = re.findall(r'\w+',text)
# print('단어 리스트:', words_count)
# print('단어의 갯수: ', len(words_count))

# counter 함수를 이용한 단어 빈도수 구하기:
from collections import Counter
text2 = 'banana, banana, banana, banana, maçã, maçã, abacaxi, abacaxi, abacaxi, morango'

frequency = Counter(text2.split())
print(frequency)
fre = frequency.items()

for k, v in fre:
    print('[{}] : {}'.format(k, v))

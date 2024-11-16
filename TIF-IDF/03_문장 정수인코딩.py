from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

raw_text = """As Forças de Defesa de Israel (FDI) disseram que permitirão que as pessoas em Gaza se movam para o sul em ruas específicas neste domingo (5), apesar de suas tropas terem sido atacadas no último sábado (4) enquanto tentavam garantir um corredor seguro para os civis.
A principal rota de evacuação será a rua Salah Al-Deen, com janela entre 10h e 14h, horário local (entre 5h e 9h de Brasília), segundo Avichay Adraee, porta-voz das FDI para a mídia árabe.
“Se você se preocupa consigo mesmo e com seus entes queridos, siga para o sul de acordo com nossas instruções. Tenha certeza de que os líderes do Hamas já estão tomando cuidado para se protegerem”, disse Adraee no X, antigo Twitter, sábado à noite.
Não ficou claro até que ponto a mensagem será recebida no território, dadas as interrupções generalizadas de eletricidade e internet, ou quão segura será a passagem.
De acordo com Adraee, o Hamas disparou no sábado morteiros e projéteis antitanque contra as forças israelenses “que estavam ansiosas para abrir a estrada do norte da Faixa de Gaza em direção ao sul”.
“Os membros do Hamas fizeram isto porque queriam manter escudos humanos para si e para os seus líderes”, disse. “Para sua segurança, aproveite a próxima vez para se deslocar para o sul, além de Wadi Gaza.”
As FDI têm apelado repetidamente aos civis em Gaza para se deslocarem para sul de Wadi Gaza, à medida que intensificam o seu ataque aéreo e terrestre à cidade de Gaza e ao norte, incluindo ataques em áreas densamente povoadas e infraestruturas civis que as FDI dizem estar a ser utilizadas por extremistas do Hamas.
"""

# 문장 토큰화
sentences = sent_tokenize(raw_text, language='portuguese')
print('문서를 문장으로 구분한 결과: ')
print(sentences)
print('문장 수:', len(sentences))
print()

vocab ={}   # 단어와 빈도수
preprocessed_sentences =[]
stopwords = set(stopwords.words('portuguese'))

for sentence in sentences :
    tokenized_sentence = word_tokenize(sentence)         # 문장을 단어로 토큰화
    result =[]

    for word in tokenized_sentence :
        word = word.lower()
        if word not in stopwords :
            if len(word) >2 :
                result.append(word)                      # 단어 토큰이 불용어에 없고 두 자 이상이면 result에 기록
                if word not in vocab :                   # 단어 빈도수
                    vocab[word] = 0                      # key, value 값으로 쌍으로 기록
                vocab[word] += 1
    preprocessed_sentences.append(result)               # 문장 단위로 토큰화한 결과값을 preprocessed_semtences에 추가하여 기록

print('result  :', result)
print('문장단위로 단어를 토큰화한 결과 출력:')
print(preprocessed_sentences)
print()
print('단어와 빈도수 :', vocab)

# 높은 빈도수 순서대로 정렬하기
vocab_sorted =sorted(vocab.items(), key= lambda x:x[1], reverse=True)
print('높은 빈도수 순서대로 정렬하기')
print(vocab_sorted)

# 높은 빈도수 단어부터 정수 부여하기 (정수 인코딩)
word_to_index = {}
i = 0
for (word, frequency) in vocab_sorted :
    if frequency > 1 :
        i = i+1
        word_to_index[word] = i
print('워드 인코딩')
print(word_to_index)

# 워드 - 인코딩을 dataframe으로 출력하기
print('워드 - 인코딩을 dataframe으로 출력하기')
df = pd.DataFrame.from_dict(word_to_index, orient='index', columns=['given index']).reset_index()
df.columns = ['Words', 'Given Index']
print(df.T)

# 상위 7개 단어만 출력
voccab_size = 7
most_common = [word for word, index in word_to_index.items() if index <= 7]
print('최상위 빈도수 단어 7개: ', most_common)

#  빈도수 상위 7개 단어와 인덱스 출력하
#  단어와 인덱스는 word_to_index에 기록되어 있다
#  word_to_index 에서 인덱스가 1-7까지 출력하면 ok

# 키, 밸류 값을 애용한 상위 빈도 단어 출력하기
for key in word_to_index :
    value = word_to_index[key]
    if value <= 7 :
        print(f"{key}, {value}")

# 상위 빈도수 단어를 사전 형태로 출력하기

words_frequency =[word for word, index in word_to_index.items() if index > voccab_size] # index가 7이상인 단어로 리스트를 만들고
for w in words_frequency :
    del word_to_index[w]            # 리스트에 있는 단어를 삭제, key를 삭제하면 value도 같이 삭제된다.
print('상위 빈도수 단어를 사전 형태로 출력하기')
print(word_to_index)

# 문장에 등장한 단어에 정수 인코딩하기



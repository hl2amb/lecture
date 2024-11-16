from nltk.tokenize import TreebankWordTokenizer

def build_bag_of_words(doc):
    # 온점 제거 및 토큰화
    doc = doc.replace('.', '')
    tokenized_document = TreebankWordTokenizer().tokenize(doc)

    word_to_index = {}  # 단어와 해당 인덱스를 매핑할 딕셔너리
    bow = []  # BoW를 저장할 리스트

    for word in tokenized_document:
        if word not in word_to_index.keys():
            # 단어가 처음 등장한 경우, 인덱스를 부여하고 BoW에 1을 추가
            word_to_index[word] = len(word_to_index)
            bow.insert(len(word_to_index) -1, 1)
        else:
            # 이미 등장한 단어의 경우, 해당 인덱스 위치의 BoW 값에 1을 추가
            index = word_to_index.get(word)
            bow[index] = bow[index] + 1

    return word_to_index, bow

doc1 = "Cão mordido de cobra tem medo até de corda"

vocab, bow = build_bag_of_words(doc1)
print('vocabulary :', vocab)
print('bag of words :', bow)



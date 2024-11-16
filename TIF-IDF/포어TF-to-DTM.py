import pandas as pd

# tf 계산 함수
def tf(t, d):
    return d.count(t)

# 샘플 문사
doc1 = "Cão mordido de cobra tem medo até de corda"
doc2 = 'Não acordes o cão quando ele está dormindo'
doc3 = 'A ferida do cão cura-se com o pêlo do mesmo cão'
doc4 = 'São como o cão e o gato'

docs = [doc1, doc2, doc3, doc4]

# 문서에 포함된 단어의 집합을 리스트로 변환 (단어 중복 없음)
vocas =list(set(w for doc in docs for w in doc.split()))

# 문서별 tf 게산
result = []  # 결과를 저장할 리스트

for doc in docs:
    result.append([])
    for voca in vocas:
        result[-1].append(tf(voca, doc))  # TF 값을 결과에 추가

# 단어와 단어별 tf값을 매치하여 dataframe 형태로 변환하고 출력
tf_score = pd.DataFrame(result, columns=vocas)
print(tf_score)
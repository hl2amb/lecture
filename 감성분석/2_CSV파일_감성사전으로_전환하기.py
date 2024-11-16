import pandas as pd

# csv 파일을 컴퓨터에 로딩하는 함수
def load_dataset(filename):
    df = pd.read_csv(filename)
    return df

# 함수 호출
df = load_dataset('PoSentiLex.csv')
print(df.head())

# csv 파일을 사전 형태로 변환 하는 함수
def build_senilex(arg):
    sentilex ={}
    for index, row in arg.iterrows():
        word = row['word']
        sentiment = row['sentiment']
        sentilex[word] = sentiment
    return sentilex

sentilex = build_senilex(df)
print(sentilex)



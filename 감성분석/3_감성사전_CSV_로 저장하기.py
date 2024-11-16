import pandas as pd

# csv 파일을 컴퓨터에 로딩하는 함수
def load_dataset(filename):
    df = pd.read_csv(filename)
    return df

# 함수 호출
df = load_dataset('PoSentiLex.csv')
# print(df.head())

# csv 파일을 사잔 형테러 변환하는 함수
def build_senilex(df):
    sentilex ={}
    for index, row in df.iterrows():
        word = row['word']
        sentiment = row['sentiment']
        sentilex[word] = sentiment
    return sentilex

sentilex = build_senilex(df)
# print(sentilex)

# csv 형태로 사전 저장하기
def save_sentiment_dict(sentilex, output_file):
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        for word, sentiment in sentilex.items():
            f.write(f"{word},{sentiment}\n")

output_file = 'portuguese_sentiment_dict.csv'
save_sentiment_dict(sentilex, output_file)
print(f"사전이 {output_file} 파일로 저장되었습니다.")

# pandas를 이용해 csv 파일로 만들기
output_file = 'portuguese_dic.csv'
df.to_csv(output_file, encoding='utf-8-sig', index=False)  # Pandas로 CSV 저장

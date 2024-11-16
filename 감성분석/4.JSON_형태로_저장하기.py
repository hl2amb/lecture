import pandas as pd

# csv 파일을 컴퓨터에 로딩하는 함수
def load_dataset(filename):
    df = pd.read_csv(filename)
    return df

# 함수 호출
df = load_dataset('PoSentiLex.csv')
# print(df.head())

# # csv 파일을 사잔 형테러 변환하는 함수
def build_senilex(df):
    sentilex ={}
    for index, row in df.iterrows():
        word = row['word']
        sentiment = row['sentiment']
        sentilex[word] = sentiment
    return sentilex

sentilex = build_senilex(df)
# print(sentilex)

# json 형태로 저장하기

import json

def save_sentilex_to_json(sentilex, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sentilex, f, ensure_ascii=False, indent=4)

output_file = 'portuguese_sentiment_dict.json'
save_sentilex_to_json(sentilex,output_file )
print(f"사전이 {output_file} 파일로 저장되었습니다.")

with open("portuguese_sentiment_dict.json", 'r', encoding='utf-8') as f:
    sentilex = json.load(f)
    print(sentilex)
    print(type(sentilex))
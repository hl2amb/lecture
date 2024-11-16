import pandas as pd

# csv 파일을 컴퓨터에 로딩하는 함수
def load_dataset(filename):
    df = pd.read_csv(filename)
    return df

# 함수 호출
df = load_dataset('PoSentiLex.csv')
print(df.head())
print(type(df))


import pandas as pd
import re
from tabulate import tabulate


# 텍스트 파일에서 데이터를 한 줄씩 읽어 리스트에 저장
data = []

with open('SentiLex-lem-PT02.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 각 줄에서 단어와 감성 점수(POL:N0 부분)를 추출
        match = re.search(r'([^\.]+)\.PoS=[^;]+;.*POL:N0=(-?\d)', line)
        if match:
            word = match.group(1)  # 단어
            polarity = int(match.group(2))  # 감성 점수
            data.append([word, polarity])

# 리스트를 pandas DataFrame으로 변환
df = pd.DataFrame(data, columns=['Word', 'Polarity'])

# DataFrame 결과 출력
print(tabulate(df, headers='keys'))

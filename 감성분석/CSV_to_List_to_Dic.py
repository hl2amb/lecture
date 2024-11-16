import csv

with open('PoSentiLex.csv', 'r', encoding='utf-8-sig' ) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# CSV 파일을 읽고, 리스트 형태로 반환

def csv_to_dict(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 첫 번째 줄 (헤더) 건너뛰기
        sentilex = {row[0]: row[1] for row in reader}  # 각 행을 사전으로 변환
    return sentilex

# CSV 파일에서 사전 형태로 변환
# filename ="PoSentiLex.csv"
# sentilex = csv_to_dict(filename)
sentilex = csv_to_dict("PoSentiLex.csv")
# 변환된 사전 출력
print(sentilex)

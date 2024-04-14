
import pandas as pd

# 시리즈 데이타(1차원 데이타) 생성하기
seriesdata = pd.Series(['Kim', 'Lee', 'Ko', 'Park'])
print(seriesdata)

# 시리즈 데이터 읽고 index 수정하기
seriesdata = pd.Series([1,2,3,4], index=['A','B','C','D'])
print(seriesdata)

# index 출력하기
print('index 출력하기\n',seriesdata.index)

# index 수정
seriesdata.index = ['Tom','John','Smith', 'Jane']
print(seriesdata)

# 시리즈 데이터의 데이터(밸류) 출력
print(seriesdata.values)

# 특정 인덱스의 밸류 값 출력/ index name과 index 번호로 가능
print(seriesdata['Jane'], seriesdata[2])

# 시리즈 데이터 삭제
del seriesdata['Jane']
print(seriesdata)
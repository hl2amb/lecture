import pandas as pd

# dataframe : 컬럼이 하나 이상인 자료
# df = pd.DataFrame({'year': [2009, 2010],
#                     'korea':['Seoul', 'Busan'],
#                    'Brazil':['Sao Paulo', 'Salvador'],
#                    'China':['Beijing', 'Nanjing']})

# 인덱스와 함께 데이터 프레임 생성
df = pd.DataFrame({'year': [2009, 2010],
                    'korea':['Seoul', 'Busan'],
                   'Brazil':['Sao Paulo', 'Salvador'],
                   'China':['Beijing', 'Nanjing']},
                  index=['1조', '2조'])

# 인덱스 지정/변경
# df.index = ['First year', 'Second year']
# print(df)
# print()

# 컬럼 변경
df.columns =['년도', '한국', '브라질', '중국']

# 특정 컬럼을 인덱스로 만들기
# df.set_index('년도')
# print(df)
# print(df.set_index('년도'))
# print()
# df = df.set_index('년도')
# print(df)
# print()

# 특정 행 가져오기: loc[인덱스], iloc[인덱스번호]
# print(df.loc[2009])
# print()
# print(df.iloc[0])

# 컬럼 추가 하기
# print(df)
# df['일본'] = ['Tokyo', 'Nagoya']
# print(df)

# 행과 열을 바꾸기 .T
# print(df)
# print(df.T)

# 특정 컬럼만 복사하여 데이터프레임 만들기 .copy()
df2=df[['한국', '중국']].copy()
print(df2)





# print(f'index 출력: {df.index}')
#
# print('\nindex change')
# df = pd.DataFrame({'year': [2009, 2010],
#                     'korea':['Seoul', 'Busan'],
#                    'Brazil':['Sao Paulo', 'Salvador'],
#                    'China':['Beijing', 'Nanjing']},
#                   index = ['A', 'B'])
# print('\ndf with changed index\n', df)
#
# print('\nindex 가져오기: ',df.index)
#
# print('\nColumn 가져오기: ',df.columns)
#
# # columns name change
# df.columns = ['한국','브라질','중국']

# df.set_index('year', inplace=True) # 인덱스 변경하기
# print(df)
# df.reset_index(inplace=True) # 인덱스 디폴트로 재설정하기
# print(df)
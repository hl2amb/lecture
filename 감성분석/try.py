import json
data = '{"name": "Jane", "age": 23, "city": "San Francisco"}' # json 데이터가 문자 타입인 경우

# 문자 타입 json 데이터 읽기
json_data = json.loads(data)
print(json_data)
print(json_data['name'], json_data['age'], json_data['city'])
print(type(json_data))
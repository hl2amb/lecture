import json

# data = '{"name": "Jane", "age": 23, "city": "San Francisco"}' # json 데이터가 문자 타입인 경우

# 문자 타입 json 데이터 읽기
# json_data = json.loads(data)
# print(json_data)
# print(json_data['name'], json_data['age'], json_data['city'])
# print(type(json_data))

# jason, 사전 데이터를 문자열로 바꾸기
# data = {"Nome": "Maria", "idade": 8, "cidade": "Lisboa"}
# json_data = json.dumps(data)
# print(json_data)
# print(type(json_data))

# json.dumps()와 extended ascii 문자 처리 및 indent 구조화

# data = {"이름": "José", "나이": 8, "거주지": "北京"}

# json_data = json.dumps(data)
# json_data = json.dumps(data, indent=1, ensure_ascii=False)
# print(json_data)

# jason.dump() : 파일로 만들기
# data = {"이름": "José", "나이": 8, "거주지": "北京"}
# with open('data_json.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

# json 파일 읽기
with open('data_json.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    print(json.dumps(data, indent=1, ensure_ascii=False))
    print(type(data))
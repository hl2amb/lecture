import csv

# csv  파일 열기
with open('csv_sample.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        print(row)

# csv 퍼일 생성하기
with open('test.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
    new_data = csv.writer(csvfile, delimiter=',')
    new_data.writerow([8, '고길동', '1985', '만화과', '10'])

# 생성한 파일 읽어서 출력하기
with open('test.csv', 'r', encoding='utf-8-sig', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)

# 기존 파일에 행 추가하기
with open('test.csv', 'a') as csvfile:
    add_row = csv.writer(csvfile, delimiter=',')
    add_row.writerow(['10', '을지문덕', '2024', '고구려', '3'])
    # csvfile.close()
    with open('test.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# 사전을 사용해 CSV 파일 만들기
with open('name_list.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:

    fieldnames = ['Name', 'Gender', 'Age']

    listwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    listwriter.writeheader()
    listwriter.writerow({'Name': '고길동', 'Gender': 'M', 'Age': '48'})
    listwriter.writerow({'Name': '길복순', 'Gender': 'F', 'Age': '40'})

# 사전으로 만들어진 csv 파일 읽기
with open('name_list.csv', 'r', encoding='utf-8-sig', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
        # key, value로 출력하기
        print(row['Name'], row['Gender'], row['Age'])
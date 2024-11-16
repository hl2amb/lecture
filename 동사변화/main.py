# Type과 연산
# a = 1
# print(a)
# print(type(a))

# b = -1
# print(type(b))
#
# c = 1.2
# print(type(c))
#
# print("1.2 is %s" %type(c))
#
# a = 2
# b = 4

# print('a+b =', a+b)
# print('a*b =', a*b)
# print('a/b =', a/b)
# print('aEb =', a**b)
# print('a//b =', a//b) # 몫
# print('a%b =', a%b)  # 나머지

# a = 10
# b = 1/1000
# print(a**b)

#자료형 선언
# a = 200
# msg = "I love Python."
# list_data = ['a', 'b', 'c']
# dic_data = {'a':97, 'b':98}
# print(a, end='')
# print(msg, end="")
# print(dic_data)
# print(list_data[1])
# # print(dic_data[c])
# print(dic_data.get('c'))
# print("hi")

#list

my_list = ['a', 'b', 'c']
# if "a" in my_list:
#     print('a is in the list.')
#     print(my_list)
# else:
#     print("a is not in the list")

# print(my_list)
# my_list.append("KF21")
# print(my_list)
# my_list.insert(1, "KF21")
# print(my_list) # list에서는 중복이 될 수 있다.

# print(my_list.pop())
# print(my_list)
# print(my_list.count("KF21"))
# my_list.reverse()
# print(my_list)
# ur_list = ["냉장고", "자동차", '비행기']
#
# my_list.extend(ur_list) # 리스트 합치기
# print(my_list)

# if 문

# temp = int(input('What is the temperature?')) #입력은 문자열임
# if temp >= 30:
#     print('Today is hot')
# elif temp <30 and temp >25:
#     print('Today is good')
# else:
#     print('Please stay at home')

# for 문
squadran =['1번기','2번기', '3번기', '4번기']

for x in squadran:
    print("{}가 출격했습니다.".format(x))
    # if x <'3번기':
    #     continue
    # else:
    #     break

# scope = [1, 2, 3, 4, 5]
# for c in scope:
#     print(c)
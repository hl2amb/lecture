from pprint import pprint

# for 문
squadron = ['leader', 'left wingman', 'right wingman','back man' ]

for listing in squadron:
    print("{} sucessfully launched".format(listing))

# clients = ["Tom", "Jonh", "Mary"]
#
# for order in clients:
#     print("{}, your order is ready, sir".format(order))

# customer = 'Tom'
# person ='unkown'
#
# while person != customer:
#     print('{0}, your coffee is ready.'.format(customer))
#     person = input("What's your name?")
#     if person == customer:
#         print('{} Enjoy your coffee!'.format(person))
#     else:
#         print('Sorry, {}. Your coffee is not yet ready. Wait a litte more, please'.format(person))
#         break

# 이중 for 문
# for i in range(2, 10):
#     for j in range(1,10):
#         print(i*j, end= " ")
#     print()

# 사전에 밸류를 리스트로 지정하고 리스트 조작하기
score = {'Kim': [60, 40, 30, 90], 'Lee': [20, 80, 40, 85]}
# print(score.values())

# total = []
# for key, value in score.items():
#
#     total = []
#     sum = 0
#     for i in score:         # 키값 반복
#         for j in value:     # 리스트 값 기준
#             sum += j/4
#
#     total.append(int(sum))  # 실수만 더하기
#     print(key, total)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end=" ")
#     print()

# a = [1, 2, 3, 4, 5]
# result =[i * 3 for i in a if i%2 ==0]
#
# # for i in a:
# #     result.append(i*3)
# print(result)

# result = [ x*y for x in range(2, 10)
#            for y in range(1, 10)]
#
# # pprint(result)
# # print(*result, sep='\n')
# print(result)
#

# coffee = 10
# money = 300
# while money:
#     print("You paid, get your coffee.")
#     money = money -30
#     print(" %d. left. " % money)
#     if money == 0:
#         continue
#         print('Not enough money.')



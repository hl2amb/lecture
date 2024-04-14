import re

texto = "José, já começou a investigar o caso da Amália?"

# [a-zA-z]으로 비문자열 제거 : 액센트 문자가 같이 지워짐
texto1 = re.sub('[^a-zA-z]', '', texto)
print(texto1)

# \W로 비문자열 제거 : 액센트 문자가 남는다.
texto2= re.sub('\W+', '', texto)
print(texto2)

# \W를 사용하여 비문자열을 공백으로 대치
texto3= re.sub('\W+', ' ', texto)
print(texto3)
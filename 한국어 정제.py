import re

text ="9시에 아버지가 방에 들어가시니?"
print(text)
print()
text1 = re.sub('[^가-힣ㄱ-ㅎ]', ' ', text)
print(text1)
import re

# 감성사전 블로오기
with open('SentiLex-lem-PT02.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
        # 정규 표현식 패턴
        # pattern = r'([^\.]+)POL:N0=(-?\d+)'
        # pattern = r'([^\.]+)\.PoS=[^;]+;.*POL:N0=(-?\d)'
        # # match = re.search(r'([^\.]+).*POL:N0=(-?\d)', line)
        # match = re.search(pattern, line)
        #
        #
        # if match:
        #     lemma = match.group(1)
        #     print(lemma)
            # polarity = match.group(2)
            # print(polarity)
            # print(lemma, polarity)


import re

# SentiLex-PT 파일 로드
sentilex_dict = {}

# SentiLex-PT 텍스트 파일 경로
with open('SentiLex-lem-PT02.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 각 줄에서 단어와 POL(감성 점수) 값 추출
        # match = re.search(r'([^\.]+)\.PoS=[^;]+;.*POL:N0=(-?\d)', line)
        match = re.search(r'([^\.]+).*POL:N0=(-?\d)', line)

        if match:
            word = match.group(1).lower()  # 단어 추출
            polarity = int(match.group(2))  # 감성 점수 추출
            sentilex_dict[word] = polarity

# 감성 분석할 텍스트
text = "Esse filme é maravilhoso e emocionante, mas o final foi muito abafado"

# 텍스트를 토큰화 (간단한 방법으로 공백 기준 분리)
words = text.split()

# 감성 분석 결과를 저장할 변수
positive_score = 0
negative_score = 0

# 텍스트에서 각 단어의 감성을 계산
for word in words:
    # SentiLex 사전에서 단어의 감성 점수를 찾음
    polarity = sentilex_dict.get(word.lower(), 0)

    # 감성 점수 업데이트
    if polarity == 1:  # 긍정적인 경우
        positive_score += 1
    elif polarity == -1:  # 부정적인 경우
        negative_score += 1

# 최종 감성 점수 계산
total_score = positive_score - negative_score

# 감성 분석 결과 출력
print(f"긍정 단어 개수: {positive_score}")
print(f"부정 단어 개수: {negative_score}")

if total_score > 0:
    print("전체 감정 분석 결과: 긍정적")
elif total_score < 0:
    print("전체 감정 분석 결과: 부정적")
else:
    print("전체 감정 분석 결과: 중립적")

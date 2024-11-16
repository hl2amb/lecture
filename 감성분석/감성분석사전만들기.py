import pandas as pd
import re


# 감성 데이터셋 로드: 데이터셋은 'word', 'sentiment' 열을 가지고 있다고 가정
# 'sentiment'는 'positive', 'negative', 'neutral'과 같은 레이블을 가짐
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


# 텍스트 정규화: 단어를 소문자로 변환하고 불필요한 기호를 제거
def normalize_text(text):
    text = text.lower()  # 소문자로 변환
    text = re.sub(r'[^\w\s]', '', text)  # 구두점 제거
    return text


# 감성 사전 구축 함수: 각 단어와 감성 레이블을 사전 형태로 저장
def build_sentiment_dict(df):
    sentiment_dict = {}
    for index, row in df.iterrows():
        word = normalize_text(row['word'])
        sentiment = row['sentiment']
        sentiment_dict[word] = sentiment
    return sentiment_dict


# 사전 저장
def save_sentiment_dict(sentiment_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, sentiment in sentiment_dict.items():
            f.write(f"{word},{sentiment}\n")


# 메인 실행 함수
def main():
    # 데이터셋 파일 경로 (포르투갈어 감성 데이터셋)
    dataset_path = 'portuguese_sentiment_dataset.csv'

    # 데이터셋 로드
    df = load_dataset(dataset_path)

    # 감성 사전 구축
    sentiment_dict = build_sentiment_dict(df)

    # 사전 저장 (CSV 파일로 저장)
    output_file = 'portuguese_sentiment_dict.csv'
    save_sentiment_dict(sentiment_dict, output_file)
    print(f"사전이 {output_file} 파일로 저장되었습니다.")


# main 함수 실행
if __name__ == "__main__":
    main()

import re
import emoji

text = input("Enter Your Text with Emojis: " )
# "Hello 👋! How are you 😊? Let's grab some 🍕!"

# 이모지만 추출하는 정규표현식 사용
def extract_emoji():

    emoji_list = re.findall(r'[^\w\s,]', text)
    print("Non-Alpha-Numerics:", emoji_list)

    # emoji 라이브러리를 사용하여 이모지만 추출
    emoji_list = [char for char in text if char in emoji.EMOJI_DATA]
    print("이모지콘:", emoji_list)
    return


def emoji_to_text():
    text_with_description = emoji.demojize(text)
    print("텍스트+이모지콘 풀어쓰기:", text_with_description)
    return

def main():
    extract_emoji()
    emoji_to_text()

if __name__ == "__main__":
    main()
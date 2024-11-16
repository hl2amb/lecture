import re
import emoji

text = "Hello 👋! How are you 😊? Let's grab some 🍕!"

# 이모지만 추출하는 정규표현식 사용
emoji_list = re.findall(r'[^\w\s,]', text)
print("Detected emojis:", emoji_list)

# emoji 라이브러리를 사용하여 이모지만 추출
emoji_list = [char for char in text if char in emoji.EMOJI_DATA]
print("Detected emojis (using emoji library):", emoji_list)


# text = "I love coding! 💻🔥"

# 이모지를 텍스트로 변환
text_with_description = emoji.demojize(text)
print("Text with emoji descriptions:", text_with_description)


# 이모지 추가
phrase = "Python is fun"
text_with_emoji = phrase + " " + emoji.emojize(":snake:")
print("Text with added emoji:", text_with_emoji)

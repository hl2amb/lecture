from googleapiclient.discovery import build
from datetime import datetime, timedelta


# API 키 설정
API_KEY = "AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c"  # Google Cloud Console에서 발급받은 YouTube Data API Key
keyword = input("KEYWORD: ")
SEARCH_QUERY = f"{keyword}"
from_date = input('Enter the Start date: ')
to_date = input('Enter the End Date :')

MAX_RESULTS = 5  # 검색 결과 제한 설정 (테스트 목적으로 5개만 가져옴)

# YouTube 서비스 초기화
youtube = build('youtube', 'v3', developerKey=API_KEY)

# from_date = input('Enter the Start date: ')
# to_date = input('Enter the End Date :')


# 문자열을 datetime 객체로 변환 후 ISO 8601 형식으로 변환
start_date = datetime.strptime(from_date, "%Y-%m-%d").isoformat("T") + "Z"
end_date = datetime.strptime(to_date, "%Y-%m-%d").isoformat("T") + "Z"

# API 요청
request = youtube.search().list(
    q=SEARCH_QUERY,
    part="snippet",
    maxResults=MAX_RESULTS,
    type="video",
    publishedAfter=start_date,
    publishedBefore=end_date
)
response = request.execute()

# 결과 출력
for index, item in enumerate(response['items'], 1):
    print(f"{index}. {item['snippet']['title']}")
    print("Published At:", item['snippet']['publishedAt'][:10])
    print("Video ID:", item['id']['videoId'])
    print("URL: https://www.youtube.com/watch?v=" + item['id']['videoId'])
    print("\n")



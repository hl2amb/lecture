from googleapiclient.discovery import build
import html
from datetime import datetime

# Print the current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)
# API 키 설정
API_KEY = "AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c"  # Google Cloud Console에서 발급받은 YouTube Data API Key
keyword = input("KEYWORD: ")
SEARCH_QUERY = f"{keyword}"
MAX_RESULTS = 5  # 검색 결과 제한 설정 (테스트 목적으로 5개만 가져옴)

# Enter the publishedAfter date
date_input = input("Enter the date: ")

# Validate and check that the date is in the past
try:
    published_after_date = datetime.strptime(date_input, "%Y-%m-%d")
    current_date = datetime.now()

    # Check if the entered date is in the future
    if published_after_date >= current_date:
        print("Error: The date must be in the past. Please enter a date before today.")
    else:
        published_after = published_after_date.strftime("%Y-%m-%dT00:00:00Z")

        # YouTube API 클라이언트 초기화
        youtube = build("youtube", "v3", developerKey=API_KEY)

        # 검색 요청
        request = youtube.search().list(
            q=SEARCH_QUERY,
            part="id,snippet",
            type="video",
            maxResults=MAX_RESULTS,
            publishedAfter=published_after  # Filter for videos published after this date
        )
        response = request.execute()

        # 비디오 정보를 담을 리스트
        videos = [{"videoId": item["id"]["videoId"], "title": html.unescape(item["snippet"]["title"])} for item in response["items"]]

        # 비디오 세부 정보 출력
        for index, video in enumerate(videos, start=1):
            video_id = video["videoId"]

            # 비디오 상세 정보 요청
            request = youtube.videos().list(
                part="snippet,statistics",
                id=video_id
            )
            response = request.execute()
            item = response["items"][0]

            title = item["snippet"]["title"]
            published_at = item["snippet"]["publishedAt"][:10]  # "YYYY-MM-DD" 형식으로 자르기
            view_count = item["statistics"].get("viewCount", 0)

            print(f"{index}. {title}\n게시일: {published_at}\n조회수: {view_count}")
except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


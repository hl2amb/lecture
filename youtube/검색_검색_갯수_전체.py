import googleapiclient.discovery
from datetime import datetime
from langdetect import detect
import html

# API 키 설정
API_KEY = "AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c"
SEARCH_QUERY = "coreia do sul"

# YouTube API 클라이언트 초기화
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

# 검색 시작일과 종료일 설정 (옵션)
from_date = "2024-01-01"
to_date = "2024-10-31"
start_date = datetime.strptime(from_date, "%Y-%m-%d").isoformat("T") + "Z"
end_date = datetime.strptime(to_date, "%Y-%m-%d").isoformat("T") + "Z"

# 전체 검색 결과 저장 리스트
videos = []

# 페이지네이션 처리
next_page_token = None
while True:
    search_request = youtube.search().list(
        q=SEARCH_QUERY,
        part="snippet",
        maxResults=50,  # API의 최대 값
        type="video",
        publishedAfter=start_date,
        publishedBefore=end_date,
        pageToken=next_page_token
    )
    search_response = search_request.execute()

    # 검색 결과 저장
    videos = [{"videoId": item["id"]["videoId"], "title": html.unescape(item["snippet"]["title"])} for item in
              search_response["items"]]


    # for item in search_response.get("items", []):
    #     title = item["snippet"]["title"]
    #     try:
    #         # 제목이 포르투갈어인지 확인
    #         if detect(title) == "pt":
    #             videos.append({
    #                 "video_id": item["id"]["videoId"],
    #                 "title": title,
    #                 "published_at": item["snippet"]["publishedAt"]
    #             })
    #     except Exception as e:
    #         print(f"언어 감지 오류: {e} (제목: {title})")

    # 다음 페이지 토큰 확인
    next_page_token = search_response.get("nextPageToken")
    if not next_page_token:  # 다음 페이지가 없으면 루프 종료
        break

# 결과 출력
# print(f"총 검색 결과 수: {len(videos)}")
for index, video in enumerate(videos, 1):
    print(f"{index}. Video ID: {video['videoId']}, Title: {video['title']}")

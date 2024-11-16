import googleapiclient.discovery
from datetime import datetime
import pandas as pd
from datetime import datetime
import json


# API 키 설정
API_KEY = "AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c"  # Google Cloud Console에서 발급받은 YouTube Data API Key
keyword = input("KEYWORD: ")
SEARCH_QUERY = f"{keyword}"
from_date = input('검색 시작일(YYYY-MM-DD) : ')
to_date = input('검색 종료일(YYYY-MM-DD) : ')

MAX_RESULTS = 1  # 검색 결과 제한 설정

# YouTube API 클라이언트 초기화
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

# 문자열을 datetime 객체로 변환 후 ISO 8601 형식으로 변환
start_date = datetime.strptime(from_date, "%Y-%m-%d").isoformat("T") + "Z"
end_date = datetime.strptime(to_date, "%Y-%m-%d").isoformat("T") + "Z"

# 검색 API 요청
search_request = youtube.search().list(
    q=SEARCH_QUERY,
    part="snippet",
    maxResults=MAX_RESULTS,
    type="video",
    publishedAfter=start_date,
    publishedBefore=end_date
)
search_response = search_request.execute()

# 동영상 ID 리스트 추출
videos = [
    {"video_id": item["id"]["videoId"], "title": item["snippet"]["title"]}
    for item in search_response.get("items", [])
]

# 댓글 가져오기
comments = []

for video in videos:
    video_id = video["video_id"]
    video_title = video["title"]
    next_page_token = None  # 초기 페이지 설정

    while True:
        comment_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText",
            pageToken=next_page_token  # 페이지 토큰 추가
        )
        comment_response = comment_request.execute()

        for item in comment_response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            comments.append({
                "video_id": video_id,
                "title": video_title,
                "comment": comment
            })

        # 다음 페이지 토큰 확인
        next_page_token = comment_response.get("nextPageToken")
        if not next_page_token:  # 다음 페이지가 없으면 루프 종료
            break

# 결과 출력
for index, comment in enumerate(comments, start=1):
    print(f"{index}. 비디오 ID: {comment['video_id']}, 제목: {comment['title']}, \n댓글: {comment['comment']}")


# 데이터프레임으로 변환
# df = pd.DataFrame(comments)
#
# # 결과 출력 및 엑셀 저장
# print(df)
# df.to_excel("youtube_comments.xlsx", index=False)
# print("Comments saved to youtube_comments.xlsx")

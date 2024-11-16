import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import openpyxl

from googleapiclient.discovery import build
from datetime import datetime, timedelta


# API 키 설정
API_KEY = "AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c"  # Google Cloud Console에서 발급받은 YouTube Data API Key
keyword = input("KEYWORD: ")
SEARCH_QUERY = f"{keyword}"
from_date = input('검색 시작일(YYYY-MM-DD) : ')
to_date = input('검색 종료일(YYYY-MM-DD) : ')

MAX_RESULTS = 5  # 검색 결과 제한 설정 (테스트 목적으로 5개만 가져옴)

# YouTube 서비스 초기화
youtube = build('youtube', 'v3', developerKey=API_KEY)

# 문자열을 datetime 객체로 변환 후 ISO 8601 형식으로 변환
start_date = datetime.strptime(from_date, "%Y-%m-%d").isoformat("T") + "Z"
end_date = datetime.strptime(to_date, "%Y-%m-%d").isoformat("T") + "Z"


def search_videos(query, max_results=5):
    """
    YouTube에서 검색어로 비디오를 검색하여 videoId 리스트 반환.
    """
    request = youtube.search().list(
        q=SEARCH_QUERY,
        part="snippet",
        maxResults=MAX_RESULTS,
        type="video",
        publishedAfter=start_date,
        publishedBefore=end_date
    )

    response = request.execute()
    videos = [{"videoId": item["id"]["videoId"], "title": item["snippet"]["title"]} for item in response["items"]]
    return videos


def get_video_details(video_id):
    """
    videoId에 대한 비디오 제목, 업로드 날짜, 조회수를 반환.
    """
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()
    item = response["items"][0]

    title = item["snippet"]["title"]
    published_at = item["snippet"]["publishedAt"]
    view_count = item["statistics"].get("viewCount", 0)

    return {"title": title, "published_at": published_at, "view_count": view_count}


def get_video_comments(video_id, max_results=20):
    """
    특정 videoId에 대한 댓글을 가져와 리스트로 반환.
    """
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )
    response = request.execute()

    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments


def main():
    # 1. 비디오 검색
    videos = search_videos(SEARCH_QUERY, MAX_RESULTS)

    # 2. 데이터 저장용 리스트 초기화
    video_data = []

    # 3. 각 비디오의 정보 및 댓글 가져오기
    for video in videos:
        video_id = video["videoId"]

        # 비디오 메타데이터 가져오기
        details = get_video_details(video_id)
        comments = get_video_comments(video_id)

        print(f"Video Title: {details['title']}")
        print(f"Published Date: {details['published_at']}")
        print(f"View Count: {details['view_count']}")
        print(f"Comments: {comments}")
        print("\n" + "=" * 50 + "\n")

        # 데이터 프레임에 추가할 형식으로 딕셔너리 생성
        video_info = {
            "Video ID": video_id,
            "Title": details["title"],
            "Published Date": details["published_at"],
            "View Count": details["view_count"],
            "Comments": "\n".join(comments)  # 댓글을 한 칸에 줄바꿈으로 연결
        }

        video_data.append(video_info)

    # 4. DataFrame 생성 및 엑셀 파일로 저장
    df = pd.DataFrame(video_data)
    # df.to_excel("youtube_search_results.xlsx", index=False)
    print("Data saved to youtube_search_results.xlsx")


if __name__ == "__main__":
    main()
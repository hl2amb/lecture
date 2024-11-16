import googleapiclient.discovery
import googleapiclient.errors
import html

# API 키 설정
API_KEY = "AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c"  # Google Cloud Console에서 발급받은 YouTube Data API Key
keyword = input("KEYWORD: ")
SEARCH_QUERY = f"{keyword}"
MAX_RESULTS = 5  # 검색 결과 제한 설정 (테스트 목적으로 5개만 가져옴)

# YouTube API 클라이언트 초기화
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def info_detail():
    request = youtube.search().list(
        q=SEARCH_QUERY,
        part="id,snippet",
        type="video",
        maxResults=MAX_RESULTS
    )
    response = request.execute()
    videos = [{"videoId": item["id"]["videoId"], "title": html.unescape(item["snippet"]["title"])} for item in response["items"]]

    for index, video in enumerate(videos, start=1):
        video_id = video["videoId"]

        request = youtube.videos().list(
            part="snippet,statistics",
            id=video_id )

        response = request.execute()
        item = response["items"][0]

        title = item["snippet"]["title"]
        published_at = item["snippet"]["publishedAt"][:10] # 시간 표시 없이 날짜만 나오게 하기
        view_count = item["statistics"].get("viewCount", 0)

        print(f"{index}.{title}, \n게시일 :{published_at}, \n조회수 : {view_count}")


info_detail()


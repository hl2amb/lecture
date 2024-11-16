import googleapiclient.discovery
import googleapiclient.errors
import html

# API 키 설정
API_KEY = "AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c"
keyword = input("KEYWORD: ")
SEARCH_QUERY = f"{keyword}"
MAX_RESULTS = 5  # 검색 결과 제한 설정 (테스트 목적으로 5개만 가져옴)

# YouTube API 클라이언트 초기화
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def search_youtube(SEARCH_QUERY, MAX_RESULTS):

    request = youtube.search().list(
            q=SEARCH_QUERY,
            part="id,snippet",
            type="video",
            maxResults=MAX_RESULTS,
    )
    response = request.execute()
    # videos = [{"videoId": item["id"]["videoId"], "title": item["snippet"]["title"]} for item in response["items"]]
    videos = [{"videoId": item["id"]["videoId"], "title": html.unescape(item["snippet"]["title"])} for item in response["items"]]
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}")
    return videos

search_youtube(SEARCH_QUERY, MAX_RESULTS)
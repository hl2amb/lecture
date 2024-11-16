from googleapiclient.discovery import build
import pandas as pd

# Replace with your API key
API_KEY = 'AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c'

# Replace with the video ID of the YouTube video you want to fetch comments from
VIDEO_ID = 'SK4iwzv8BlU'

youtube = build('youtube', 'v3', developerKey=API_KEY)

comments = []
next_page_token = None # 첫번째 페이지의 정보를 가져오기

while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        pageToken=next_page_token, #API에서 pageToken을 받아와 next_page_token에 저장
        maxResults=100
    )
    response = request.execute()

    for item in response['items']:
        top_comment = item['snippet']['topLevelComment']['snippet']
        comments.append({
            'type': 'Top-level',
            'author': top_comment['authorDisplayName'],
            'comment': top_comment['textOriginal'],
            'likes': top_comment['likeCount'],
            'published_at': top_comment['publishedAt']
        })

    if 'replies' in item:
        for reply in item['replies']['comments']:
            reply_snippet = reply['snippet']
            comments.append({
                'type': 'Reply',
                'author': reply_snippet['authorDisplayName'],
                'comment': reply_snippet['textOriginal'],
                'likes': reply_snippet['likeCount'],
                'published_at': reply_snippet['publishedAt']
            })

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

    for index, comment in enumerate(comments):
        print(
            f"{index + 1}. [{comment['type']}] {comment['author']} - {comment['comment']} (Likes: {comment['likes']}, Published: {comment['published_at']})")

    # for index, comment in enumerate(comments):
    #     print(f'{index}. {comment}')




# def save_to_csv(comments, file_name='comments.csv'):
#     df = pd.DataFrame(comments)
#     df.to_csv(file_name, index=False)
#     print(f"Saved {len(comments)} comments to {file_name}")



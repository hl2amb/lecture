from googleapiclient.discovery import build
import pandas as pd

# Replace with your API key
API_KEY = 'AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c'

# Replace with the video ID of the YouTube video you want to fetch comments from
VIDEO_ID = 'SK4iwzv8BlU'

youtube = build('youtube', 'v3', developerKey=API_KEY)

comments = []
next_page_token = None

while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        pageToken=next_page_token,
        maxResults=100
    )
    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append({
            # 'author': comment['authorDisplayName'],
            comment['textOriginal'],
            # 'like_count': comment['likeCount'],
            # 'published_at': comment['publishedAt']
        })

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

    for index, comment in enumerate(comments,1):
        print(f'{index}. {comment}')




# def save_to_csv(comments, file_name='comments.csv'):
#     df = pd.DataFrame(comments)
#     df.to_csv(file_name, index=False)
#     print(f"Saved {len(comments)} comments to {file_name}")



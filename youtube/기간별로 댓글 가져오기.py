import googleapiclient.discovery
import pandas as pd
from datetime import datetime
import html
import os

# Secure API key via environment variable
API_KEY = os.getenv("AIzaSyCsQH7CJnoKuEFmRvyyzGfNIUhXpj8nZ0c")

keyword = input("Enter the keyword to search for: ")
SEARCH_QUERY = f"{keyword}"
MAX_RESULTS = 5  # Limit the search results to 5 for testing
MAX_COMMENTS = 10  # Limit comments to 10 per video

# YouTube API client initialization
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

# Date range input
from_date = input('Enter the Start date (YYYY-MM-DD): ')
to_date = input('Enter the End date (YYYY-MM-DD): ')

# Convert strings to datetime objects and format as ISO 8601
start_date = datetime.strptime(from_date, "%Y-%m-%d").isoformat("T") + "Z"
end_date = datetime.strptime(to_date, "%Y-%m-%d").isoformat("T") + "Z"

# YouTube video search
request = youtube.search().list(
    q=SEARCH_QUERY,
    part="id,snippet",
    type="video",
    publishedAfter=start_date,
    publishedBefore=end_date,
    maxResults=MAX_RESULTS
)

response = request.execute()
videos = [{"videoId": item["id"]["videoId"], "title": html.unescape(item["snippet"]["title"])} for item in response["items"]]

# Initialize a list to store video details
video_data = []

for index, video in enumerate(videos, start=1):
    video_id = video["videoId"]
    video_request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    video_response = video_request.execute()
    item = video_response["items"][0]

    title = item["snippet"]["title"]
    published_at = item["snippet"]["publishedAt"][:10]  # Display date only
    view_count = item["statistics"].get("viewCount", 0)

    # Collect comments for each video
    comments = []
    try:
        comments_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=MAX_COMMENTS,
            order="relevance"
        )
        comments_response = comments_request.execute()

        for comment_item in comments_response["items"]:
            comment = comment_item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            author = comment_item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
            comments.append(f"{author}: {comment}")

    except googleapiclient.errors.HttpError as e:
        comments.append("Comments are disabled or unavailable for this video.")

    # Collect video and comment information
    video_data.append({
        "Title": title,
        "Published Date": published_at,
        "Views": view_count,
        "URL": f"https://www.youtube.com/watch?v={video_id}",
        "Comments": "\n".join(comments)  # Join comments into a single string for easy export
    })

    print(f"{index}. {title}\nPublished Date: {published_at}\nViews: {view_count}")
    print("URL:", f"https://www.youtube.com/watch?v={video_id}")
    print("Comments:\n" + "\n".join(comments), "\n")

# Optional: Convert data to DataFrame and export to Excel
# df = pd.DataFrame(video_data)
# df.to_excel("youtube_search_results_with_comments.xlsx", index=False)
# print("\nData has been saved to 'youtube_search_results_with_comments.xlsx'.")

import pandas as pd
import os
import googleapiclient.discovery

# Function to get video comments from YouTube API
def get_video_comments(youtube, video_id, max_results=100):
    comments = []
    try:
        # Call the commentThreads.list API to retrieve comments
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText"
        )
        response = request.execute()

        # Loop through each comment and append relevant information
        while response:
            for item in response["items"]:
                comment = item["snippet"]["topLevelComment"]["snippet"]
                comments.append({
                    "video_id": video_id,
                    "author": comment["authorDisplayName"],
                    "comment": comment["textDisplay"],
                    "likes": comment["likeCount"],
                    "published_at": comment["publishedAt"]
                })

            # Check if there's another page of comments
            if "nextPageToken" in response:
                request = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=max_results,
                    textFormat="plainText",
                    pageToken=response["nextPageToken"]
                )
                response = request.execute()
            else:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
        return comments
    return comments

# Main function to scrape comments from a list of YouTube videos and save to a CSV
def scrape_multiple_youtube_comments(video_urls, api_key, output_csv="youtube_comments.csv"):
    # Initialize the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Initialize an empty DataFrame to store all comments
    all_comments_df = pd.DataFrame()

    # Iterate over all video URLs
    for video_url in video_urls:
        # Extract video ID from the YouTube URL
        video_id = video_url.split("v=")[1]
        print(f"Scraping comments for video ID: {video_id}")
        
        # Scrape comments for the current video
        comments = get_video_comments(youtube, video_id)
        
        if len(comments) == 0:
            print(f"No comments found or comments are disabled for video: {video_id}")
            continue

        # Convert the list of comments into a pandas DataFrame
        video_comments_df = pd.DataFrame(comments)
        
        # Append the comments to the overall DataFrame
        all_comments_df = pd.concat([all_comments_df, video_comments_df], ignore_index=True)

    # Save the DataFrame to a CSV file with UTF-8 BOM encoding
    if not os.path.isfile(output_csv):
        all_comments_df.to_csv(output_csv, encoding='utf-8-sig', index=False)
    else:  # Append to existing CSV if it already exists
        all_comments_df.to_csv(output_csv, mode='a', encoding='utf-8-sig', index=False, header=False)

    print(f"Saved {len(all_comments_df)} comments to {output_csv}.")

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    api_key = "AIzaSyAAwY-uPy6XUHBh0cV1u4yHPTyYzxskNgI"

    # Replace with a list of YouTube video URLs
    video_urls = [
        "https://youtube.com/watch?v=6altVgTOf9s",
        "https://www.youtube.com/watch?v=NptnmWvkbTw",
        "https://www.youtube.com/watch?v=eE9MnoS0lc0"
    ]

    # Output CSV file name
    output_csv = "youtube_comments.csv"

    # Scrape the comments from all video URLs and save to CSV
    scrape_multiple_youtube_comments(video_urls, api_key, output_csv)

import youtube_dl

def youtube_scraper(keyword):
    """
    Scrapes YouTube videos based on a keyword search.

    Args:
        keyword (str): The keyword to search for on YouTube.

    Returns:
        list: A list of dictionaries containing video information, including title, URL, and duration.
    """
    videos = []

    # Set up the options for the YouTube downloader
    ydl_opts = {
        'ignoreerrors': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Perform the search and retrieve video information
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch:{keyword}", download=False)

        # Iterate over the retrieved videos
        for video in search_results['entries']:
            if video is not None:
                title = video['title']
                url = video['webpage_url']
                duration = video['duration']
                videos.append({
                    'title': title,
                    'url': url,
                    'duration': duration
                })

    return videos

# Example usage
results = youtube_scraper("python tutorial")
for video in results:
    print(f"Title: {video['title']}")
    print(f"URL: {video['url']}")
    print(f"Duration: {video['duration']} seconds")
    print()

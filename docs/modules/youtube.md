
### Scrape Video Details

Create an instance of `Video` class.

```python
video = Video(video_url="video_url")
```

| Methods         | Details                   |
| --------------- | ------------------------- |
| `.getDetails()` | Returns the video details |

## Scrape Channel Details

Create an instance of `Channel` class.

```python
channel_data = Channel(channel_username="BeABetterDev")
```

| Methods            | Details                                                                |
| ------------------ | ---------------------------------------------------------------------- |
| `.getAbout()`      | Returns the channel details mentioned in the about page of the channel |
| `.getVideos()`     | Returns all the video details in the videos page of the channel        |
| `.get_community()` | Returns all the post details in the community page of the channel      |

---
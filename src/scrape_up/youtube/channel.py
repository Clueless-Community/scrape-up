import requests
from bs4 import BeautifulSoup
import json


class Channel:
    """
    Create an instance of `Channel` class.
    ```python
    channel_data = Channel(channel_username="BeABetterDev")
    ```

    | Methods       | Details                                                                |
    | ------------- | ---------------------------------------------------------------------- |
    | `.getAbout()` | Returns the channel details mentioned in the about page of the channel |
    """

    def __init__(self, channel_username):
        self.channel_username = channel_username

    def getAbout(self):
        """
        Class - `Channel`
        ```py
        channel_data = Channel(channel_username="BeABetterDev")
        channel_data.getAbout()
        ```
        Returns:
        ```js
        {
            "name": Name of the channel
            "description": Description of the channel
            "channel_url": Link to the channel
            "channel_avatar": Channel avatar
            "channel_banner": Channel banner
            "subscriber_count": No. of subscribers of the channel
            "toal_videos": Total videos uploaded in the channel
            "total_views": Total views till date of the channel
            "join_date": Date the channel joined YouTube
            "country": Country of origin of the channel
            "links": Additional links provided from the channel
        }
        ```
        """
        url = f"https://www.youtube.com/@{self.channel_username}/about"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            channel_data = {"channel_data": []}
            link_data = {"link_data": []}
            scripts = soup.find_all("script")
            req_script = scripts[35].text.strip()
            script = req_script[20:-1]
            data = json.loads(script)

            metadata = data["metadata"]["channelMetadataRenderer"]
            title = metadata["title"]
            desc = metadata["description"]
            channel_url = metadata["vanityChannelUrl"]
            channel_avatar = metadata["avatar"]["thumbnails"][0]["url"]
            header = data["header"]["c4TabbedHeaderRenderer"]
            channel_banner = header["banner"]["thumbnails"][5]["url"]
            subs = header["subscriberCountText"]["simpleText"]
            total_videos = header["videosCountText"]["runs"][0]["text"]

            baser = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]
            for b in baser:
                try:
                    base = b["tabRenderer"]["content"]["sectionListRenderer"][
                        "contents"
                    ][0]["itemSectionRenderer"]["contents"][0][
                        "channelAboutFullMetadataRenderer"
                    ]

                    total_views = base["viewCountText"]["simpleText"]
                    join_date = base["joinedDateText"]["runs"][1]["text"]
                    country = base["country"]["simpleText"]

                    links = base["primaryLinks"]
                    for i in links:
                        link_data["link_data"].append(
                            {
                                "link_url": i["navigationEndpoint"]["urlEndpoint"][
                                    "url"
                                ],
                                "link_name": i["title"]["simpleText"],
                                "link_icon": i["icon"]["thumbnails"][0]["url"],
                            }
                        )
                except:
                    pass

            channel_data["channel_data"].append(
                {
                    "name": title,
                    "description": desc,
                    "channel_url": channel_url,
                    "channel_avatar": channel_avatar,
                    "channel_banner": channel_banner,
                    "subscriber_count": subs,
                    "toal_videos": total_videos,
                    "total_views": total_views,
                    "join_date": join_date,
                    "country": country,
                    "links": link_data,
                }
            )
            return channel_data["channel_data"][0]
        except:
            return None
        
    def getVideos(self):
        """
        Class - `Channel`
        ```py
        channel_data = Channel(channel_username="BeABetterDev")
        channel_data.getVideos()
        ```
        Returns:
        ```js
        {
            "title": Title of the video
            "description": Description of the video
            "thumbnail_url": Link of the thumbnail image
            "views_count": Total views till date of the video
            "publishedAt": Date the video was published
            "video_length": Time length of the video
            "link": Link to the video
        }
        ```
        """
        url = f"https://www.youtube.com/@{self.channel_username}/videos"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            videos_data = {"videos": []}
            scripts = soup.find_all("script")
            req_script = scripts[35].text.strip()
            script = req_script[20:-1]
            data = json.loads(script)

            vids = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1]["tabRenderer"]["content"]["richGridRenderer"]["contents"]
            for v in vids:
                try:
                    base = v["richItemRenderer"]["content"]["videoRenderer"]
                    title = base["title"]["runs"][0]["text"]
                    thumbnail_url = base["thumbnail"]["thumbnails"][-1]["url"]
                    desc = base["descriptionSnippet"]["runs"][0]["text"]
                    publishedAt = base["publishedTimeText"]["simpleText"]
                    length = base["lengthText"]["accessibility"]["accessibilityData"]["label"]
                    views = base["viewCountText"]["simpleText"]
                    link = "https://www.youtube.com/" + base["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"]
                except:
                    pass

                videos_data["videos"].append(
                    {
                        "title": title,
                        "description": desc,
                        "thumbnail_url": thumbnail_url,
                        "views_count": views,
                        "publishedAt": publishedAt,
                        "video_length": length,
                        "link": link 
                    }
                )
            return videos_data["videos"]
        except:
            return None

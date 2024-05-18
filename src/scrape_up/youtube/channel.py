from bs4 import BeautifulSoup
import json

from scrape_up.config.request_config import RequestConfig, get


class Channel:
    """
    Create an instance of `Channel` class.
    ```python
    channel_data = Channel(channel_username="BeABetterDev")
    ```

    | Methods       | Details                                                                |
    | ------------- | ---------------------------------------------------------------------- |
    | `.get_about()` | Returns the channel details mentioned in the about page of the channel |
    | `.get_videos()`| Returns all the video details in the videos page of the channel |
    | `.get_community()`| Returns all the post details in the community page of the channel |
    """

    def __init__(
        self, channel_username: str, *, config: RequestConfig = RequestConfig()
    ):
        self.channel_username = channel_username
        self.config = config

    def get_about(self):
        """
        Class - `Channel`
        ```py
        channel_data = Channel(channel_username="BeABetterDev")
        channel_data.get_about()
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
            res = get(url, self.config)
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

    def get_videos(self):
        """
        Class - `Channel`
        ```py
        channel_data = Channel(channel_username="BeABetterDev")
        channel_data.get_videos()
        ```
        Returns:
        ```js
        [
            {
                "title": Title of the video
                "description": Description of the video
                "thumbnail_url": Link of the thumbnail image
                "views_count": Total views till date of the video
                "publishedAt": Date the video was published
                "video_length": Time length of the video
                "link": Link to the video
            }
            ...
        ]
        ```
        """
        url = f"https://www.youtube.com/@{self.channel_username}/videos"
        try:
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")
            videos_data = {"videos": []}
            scripts = soup.find_all("script")
            req_script = scripts[35].text.strip()
            script = req_script[20:-1]
            data = json.loads(script)

            vids = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1][
                "tabRenderer"
            ]["content"]["richGridRenderer"]["contents"]
            for v in vids:
                try:
                    base = v["richItemRenderer"]["content"]["videoRenderer"]
                    title = base["title"]["runs"][0]["text"]
                    thumbnail_url = base["thumbnail"]["thumbnails"][-1]["url"]
                    desc = base["descriptionSnippet"]["runs"][0]["text"]
                    publishedAt = base["publishedTimeText"]["simpleText"]
                    length = base["lengthText"]["accessibility"]["accessibilityData"][
                        "label"
                    ]
                    views = base["viewCountText"]["simpleText"]
                    link = (
                        "https://www.youtube.com/"
                        + base["navigationEndpoint"]["commandMetadata"][
                            "webCommandMetadata"
                        ]["url"]
                    )
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
                        "link": link,
                    }
                )
            return videos_data["videos"]
        except:
            return None

    def get_community(self):
        """
        Class - `Channel`
        ```py
        channel_data = Channel(channel_username="BeABetterDev")
        channel_data.get_community()
        ```
        Returns:
        ```js
        [
            {
                "title":"Over the past few weeks, this channel crossed 10,000,000 total views and 150,000 subscribers. It's incredible to think how far its come and how many people this channel has managed to help. Thank you for your support!",
                "images":[

                ],
                "likes_count":"157",
                "comment_count":"10",
                "publishedAt":"4 months ago"
            },
            ...
        ]
        ```
        """
        url = f"https://www.youtube.com/@{self.channel_username}/community"
        try:
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")
            posts_data = {"posts": []}
            scripts = soup.find_all("script")
            req_script = scripts[35].text.strip()
            script = req_script[20:-1]
            data = json.loads(script)

            try:
                posts = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][6][
                    "tabRenderer"
                ]["content"]["sectionListRenderer"]["contents"][0][
                    "itemSectionRenderer"
                ]["contents"]
            except:
                posts = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][5][
                    "tabRenderer"
                ]["content"]["sectionListRenderer"]["contents"][0][
                    "itemSectionRenderer"
                ]["contents"]

            for p in posts:
                images = {"images": []}
                try:
                    base = p["backstagePostThreadRenderer"]["post"][
                        "backstagePostRenderer"
                    ]
                    try:
                        title = base["contentText"]["runs"][0]["text"]
                    except:
                        title = ""
                    try:
                        try:
                            imagebloc = base["backstageAttachment"][
                                "postMultiImageRenderer"
                            ]["images"]
                            for i in imagebloc:
                                images["images"].append(
                                    i["backstageImageRenderer"]["image"]["thumbnails"][
                                        -1
                                    ]["url"]
                                )
                        except:
                            images["images"].append(
                                base["backstageAttachment"]["backstageImageRenderer"][
                                    "image"
                                ]["thumbnails"][-1]["url"]
                            )
                    except:
                        images["images"] = []
                    date = base["publishedTimeText"]["runs"][0]["text"]
                    try:
                        likes = base["voteCount"]["simpleText"]
                    except:
                        likes = "0"
                    try:
                        comment_count = base["actionButtons"][
                            "commentActionButtonsRenderer"
                        ]["replyButton"]["buttonRenderer"]["text"]["simpleText"]
                    except:
                        comment_count = "0"
                except:
                    pass

                posts_data["posts"].append(
                    {
                        "title": title,
                        "images": images["images"],
                        "likes_count": likes,
                        "comment_count": comment_count,
                        "publishedAt": date,
                    }
                )
            return posts_data["posts"]
        except:
            return None

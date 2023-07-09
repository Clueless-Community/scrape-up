import requests
from bs4 import BeautifulSoup
import json


class Channel:
    """
    Class - `Channel`
    Example:
    ```
    channel_data = Channel(channel_url = "url")
    ```\n
    Methods :\n
    1. ``.getAbout() | Response - Channel details with name, description, channel avatar, 
                                  subscriber count, channel url, channel banner, total videos,
                                  total views, join date, country and links in the about page
    """

    def __init__(self, channel_url):
        self.channel_url = channel_url

    def getAbout(self):
        """
        Class - `Channel`
        Example:
        ```
        channel_data = Channel("https://www.youtube.com/@GitHub/about")
        channel_data.getAbout()
        ```
        Returns:
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
        """
        url = self.channel_url
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            channel_data = {"channel_data": []}
            link_data = {"link_data":[]}
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
                    base = b["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["channelAboutFullMetadataRenderer"]
                    
                    total_views = base["viewCountText"]["simpleText"]
                    join_date = base["joinedDateText"]["runs"][1]["text"]
                    country = base["country"]["simpleText"]   

                    links = base["primaryLinks"]
                    for i in links:
                        link_data["link_data"].append(
                            {
                                "link_url": i["navigationEndpoint"]["urlEndpoint"]["url"],
                                "link_name": i["title"]["simpleText"],
                                "link_icon": i["icon"]["thumbnails"][0]["url"]
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
                    "links": link_data
                }
            )
            res_json = json.dumps(channel_data)
            return res_json
        except:
            error_message = {"message": "Can't fetch channel data from the url provided."}
            ejson = json.dumps(error_message)
            return ejson

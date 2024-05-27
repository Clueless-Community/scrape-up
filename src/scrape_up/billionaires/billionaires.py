import json

import requests

from scrape_up.config.request_config import RequestConfig, get


class Billionaires:
    """
    Create an instance of `Billionaires` class.\n
    ```python
    billionaires = Billionaires()
    ```
    | Methods               | Details                                                                                      |
    | --------------------- | -------------------------------------------------------------------------------------------- |
    | `.realtime()`         | It takes a user query parameter as an argument and returns all relevant terms related to it. |
    | `.powerfulwomen()`    | Returns as JSON the list of Forbes most powerful women in the world.                         |
    | `.powerfulpeople()`   | Returns as JSON a list of Forbes Porweful people.                                            |
    | `.bylocation()`       | Returns as JSON the billionaires of a particular nation.                                     |


    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.lists = [
            {"type": "person", "year": 2022, "uri": "billionaires"},  # World richest
            {
                "type": "person",
                "year": 2022,
                "uri": "forbes-400",
            },  # American richest 400
            {
                "type": "person",
                "year": 2022,
                "uri": "hong-kong-billionaires",
            },  # Hong Kong richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "australia-billionaires",
            },  # Australia richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "china-billionaires",
            },  # China richest 400
            {
                "type": "person",
                "year": 2022,
                "uri": "taiwan-billionaires",
            },  # Taiwan richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "india-billionaires",
            },  # India richest 100
            {
                "type": "person",
                "year": 2022,
                "uri": "japan-billionaires",
            },  # Japan richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "africa-billionaires",
            },  # Africa richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "korea-billionaires",
            },  # Korea richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "malaysia-billionaires",
            },  # Malaysia richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "philippines-billionaires",
            },  # Philippines richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "singapore-billionaires",
            },  # Singapore richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "indonesia-billionaires",
            },  # Indonesia richest 50
            {
                "type": "person",
                "year": 2022,
                "uri": "thailand-billionaires",
            },  # Thailand richest 50
            {
                "type": "person",
                "year": 2017,
                "uri": "self-made-women",
            },  # American richest self-made women
            {"type": "person", "year": 2017, "uri": "richest-in-tech"},  # tech richest
            {
                "type": "person",
                "year": 2019,
                "uri": "hedge-fund-managers",
            },  # hedge fund highest-earning
            {
                "type": "person",
                "year": 2018,
                "uri": "powerful-people",
            },  # world powerful
            {
                "type": "person",
                "year": 2022,
                "uri": "power-women",
            },  # world powerful women
            {"type": "person", "year": 0, "uri": "rtb"},
            {
                "type": "person",
                "year": 0,
                "uri": "rtrl",
            },
        ]
        self.config = config

    def realtime(self):
        """
        Get the realtime position and details of 2000+ billionaires.\n
        Class - `Billionaires`\n
        Example -\n
        ```python
        item = Billionaires()
        item.realtime()
        ```
        Return
        ```js
        [
            {
                "position":2650,
                "rank":2650,
                "name":"Elizabeth Holmes",
                "lastName":"Holmes",
                "uri":"elizabeth-holmes",
                "imageUri":"elizabeth-holmes",
                "worth":0.0,
                "age":39,
                "source":"blood testing",
                "industry":"Healthcare",
                "gender":"F",
                "country":"United States",
                "timestamp":1690481101727,
                "headquarters":"CA",
                "state":"California",
                "date":725846400000,
                "description":"",
                "squareImage":"https://specials-images.forbesimg.com/imageserve/f73972b9d28df45e961ffa27a62cdff5/416x416.jpg?background=000000&cropX1=0&cropX2=744&cropY1=150&cropY2=894"
            }
            ...
        ]
        ```
        """
        # try:
        #
        #     response = requests.get(url, params=self.lists[20])
        #     k = response.json()
        #     return k
        # except:
        #     return None
        try:
            url = "http://www.forbes.com/ajax/list/data"
            response = get(url, self.config)
            if response.status_code == 200:
                k = response.json()
                return k
            else:
                print("Request failed with status code:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Request error:", e)
            return None
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
            return None

    def powerfulwomen(self):
        """
        Class - `Billionaires`\n
        Example -\n
        ```python
        item = Billionaires()
        item.powerfulwomen()
        """
        try:
            url = "http://www.forbes.com/ajax/list/data"
            response = get(url, self.config)
            k = response.json()
            return k
        except:
            return None

    def powerfulpeople(self):
        """
        Class - `Billionaires`\n
        Example -\n
        ```python
        item = Billionaires()
        item.powerfulpeople()
        """
        try:
            url = "http://www.forbes.com/ajax/list/data"
            response = get(url, self.config)
            k = response.json()
            return k
        except:
            return None

    def bylocation(self, location):
        """
        Class - `Billionaires`\n
        Example -\n
        ```python
        item = Billionaires()
        item.bylocation(location)
        ```
        Return\n
        ```js
        [
            {
                "position":100,
                "rank":100,
                "name":"Bhadresh Shah",
                "lastName":"Shah",
                "uri":"bhadresh-shah",
                "imageUri":"bhadresh-shah",
                "worth":1900.0,
                "age":71,
                "source":"engineering",
                "industry":"Manufacturing",
                "gender":"M",
                "squareImage":"//specials-images.forbesimg.com/imageserve/5c79af93a7ea431000441f81/416x416.jpg?background=000000&cropX1=2863&cropX2=4946&cropY1=1612&cropY2=3696"
            }
            ...
        ]
        ```
        """
        k = None
        url = "http://www.forbes.com/ajax/list/data"
        for i in self.lists:
            if location in i["uri"]:
                k = i
                break
        if i is not None:
            response = get(url, self.config)
            k = response.json()
            return k
        else:
            return None


forbes = Billionaires()
print(forbes.worldrichest())

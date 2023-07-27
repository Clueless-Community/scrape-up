import requests


class Pixabay():
    """
    Class - `Pixabay`\n

    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.get_params_video()`       | Returns the list of parameters required to load the videos from Pixaby.                              |
    | `.get_video()`              | Downloads the videos from pixaby to the local storage.                                               |
    | `.get_params_photo()`       | Returns the list of parameters required to load pics from Pixaby.                                    |
    | `.get_photo()`              | Downloads the photos from pixaby to local storage.                                                   |


    """
    def __init__(self, api_key='38504833-19606430bd8fde504120d1630', verbose=True):
        self.api_key = api_key
        self.name = 'Pixabay'
        self.verbose = verbose

    def _get_params_video(self, query, num, update_params={}):

        """
         Class - `Pixabay`
         Example:
         ```
         quora = Pixabay()
         quora.get_params_video(query,num)
         ```
         Returns:
         ```js
         {
            'key': API Key from Pixaby,
            'q': query given by user,
            'video_type': typeof video(default is film),
            'orientation': orientation of the video,
            'safesearch': prevents adult content,
            'per_page': number of videos to be fetched
         }
         ```
        """
        params = {
            'key': self.api_key,
            'q': query,
            'video_type': 'film',
            'orientation': 'horizontal',
            'safesearch': 'true',
            'per_page': num
        }
        params.update(update_params)
        return params

    def get_video(self, query, num=10, params={}):
        """
         Class - `Pixabay`
         Example:
         ```
         quora = Pixabay()
         quora.get_video(query,num)
         ```
         Returns: Downloads num number of videos into local storage.
         
        """
        BASE_URL = 'https://pixabay.com/api/videos/'
        _params = self._get_params_video(query, num, params)
        response = requests.get(BASE_URL, params=_params)

        data = response.json()
        hits = data['hits']
        for i, hit in enumerate(hits):
            if self.verbose:
                print(f"  Downloading Pixabay videos {i+1}/{num}")
            video_url = hit['videos']['large']['url']
            response = requests.get(video_url)
            if response is not None:
                with open(f'video_pixabay_{i+1:02d}.mp4', 'wb') as f:
                    f.write(response.content)

    def _get_params_photo(self, query, num, update_params={}):
        """
         Class - `Pixabay`
         Example:
         ```
         quora = Pixabay()
         quora.get_params_photo(query,num)
         ```
         Returns:
         ```js
         {
            'key': API Key from Pixaby,
            'q': query given by user,
            'video_type': type of photo,
            'orientation': orientation of the photo,
            'safesearch': prevents adult content,
            'per_page': number of images to be fetched
         }
         ```
        """
        params = {
            'key': self.api_key,
            'q': query,
            'image_type': 'photo',
            'orientation': 'horizontal',
            'safesearch': 'true',
            'per_page': num
        }
        params.update(update_params)
        return params

    def get_photo(self, query, num=10, params={}):
        """
         Class - `Pixabay`
         Example:
         ```
         quora = Pixabay()
         quora.get_photo(query,num)
         ```
         Returns: Downloads num number of photos into local storage.
         
        """
        BASE_URL = 'https://pixabay.com/api/'
        _params = self._get_params_photo(query, num, params)
        response = requests.get(BASE_URL, params=_params)

        data = response.json()
        hits = data['hits']
        for i, hit in enumerate(hits):
            if self.verbose:
                print(f"  Downloading Pixabay photos {i+1}/{num}")
            image_url = hit['largeImageURL']
            response = requests.get(image_url)
            if response is not None:
                with open(f'photo_pixabay_{i+1:02d}.jpg', 'wb') as f:
                    f.write(response.content)

Pixabay().get_photo('computer')                    

from pexels_api import API, api


class Images():
    PEXELS_API_KEY = '563492ad6f917000010000015f3eaa7edfa64de1ae3ee3bca5508fa9'
    api = API(PEXELS_API_KEY)

    def __init__(self, image, length):
        self.image = image
        self.length = length

    def getImages(self):
        try:
            self.api.search(self.image, page=1, results_per_page=self.length)
            print(f'The image {self.image} successfully located')
            self.photos = self.api.get_entries()
        except:
            print(f"Can't find an image named{self.image}, Trying to download next image")
        
        
        self.photo_urls = []
        for self.photo in self.photos:
            self.photo_urls.append(self.photo.original)
        return self.photo_urls

from pexels_api import API
from ReadBroll import ReadBroll


class Images():
    PEXELS_API_KEY = '563492ad6f917000010000015f3eaa7edfa64de1ae3ee3bca5508fa9'
    api = API(PEXELS_API_KEY)

    def __init__(self, image, length=10):
        self.image = image
        self.length = length

    def getImages(self):
        self.api.search(self.image, page=1, results_per_page=self.length)
        self.photos = self.api.get_entries()
        self.photo_urls = []
        for self.photo in self.photos:
            self.photo_urls.append(self.photo.url)
        return self.photo_urls

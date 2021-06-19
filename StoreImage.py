from ReadBroll import ReadBroll
from GetImages import Images
import os
import requests


class StoreB_roll():
    def __init__(self, path, no_of_images):
        self.path = path
        self.no_of_images = no_of_images

    def store_images(self):
        if os.path.isdir('B-roll Photos'):
            print("B-roll Photo directory already exists....")
            print("Replacing images.....")
        else:
            print("B-roll Photo directory dosen't exist, Creating one....")
            os.makedirs('B-roll Photos')

        self.keyWords = ReadBroll(self.path).getKeywords()
        self.keyWords_images_urls_chunks = []
        for self.Keywords in self.keyWords:
            self.keyWords_images_urls_chunks.append(
                Images(self.Keywords, self.no_of_images).getImages())
        i = 1
        for self.index, self.urls_chunks in enumerate(self.keyWords_images_urls_chunks):
            for self.urls in self.urls_chunks:
                if i <= self.no_of_images:
                    self.image = requests.get(self.urls).content
                    with open('B-roll Photos/' + str(i) + '.jpeg', 'wb+') as self.f:
                        print(f'Downloading image {i}')
                        self.f.write(self.image)
                    i += 1
                else:
                    print('All images downloaded')
                    self.f.close()
                    break


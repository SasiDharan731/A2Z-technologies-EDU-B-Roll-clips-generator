from ReadBroll import ReadBroll
from GetImages import Images
import os
import requests

if os.path.isdir('B-roll Photos'):
    print("B-roll Photo directory already exists....")
else:
    print("B-roll Photo directory dosen't exist, Creating one....")
    os.makedirs('B-roll Photos')


keyWords = ReadBroll('script.txt').getKeywords()
keyWords_images_urls_chunks = []
for Keywords in keyWords:
    keyWords_images_urls_chunks.append(Images(Keywords, 3).getImages())


i = 1
for index, urls_chunks in enumerate(keyWords_images_urls_chunks): 
    for urls in urls_chunks:   
        if i <= 3:
            image = requests.get(urls).content
            with open('B-roll Photos/'+ str(i) + '.jpeg', 'wb+') as f:
                print(f'Downloading image {i}')
                f.write(image)

            i += 1
        else:
            print('All images downloaded')
            f.close()
            break
        

from ReadBroll import ReadBroll
from GetImages import Images

keyWords = ReadBroll('script.txt').getKeywords()
keyWords_images = []
for Keywords in keyWords:
    keyWords_images.append(Images(Keywords).getImages())
print(keyWords_images)

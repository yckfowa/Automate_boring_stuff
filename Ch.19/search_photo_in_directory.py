import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('<Enter your own directory>'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0

    for filename in filenames:
        if not (filename.lower().endswith('png') or filename.lower().endswith('jpg')):
            numNonPhotoFiles += 1
            continue

        img = Image.open(os.path.join(foldername, filename))
    
        width, height = img.size

        if width > 500 and height > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1

    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))

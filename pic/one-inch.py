import cv2
import numpy as np

from PIL import Image



oneInchPic = Image.new("RGB",(295,413))
pixTuple = (255,0,255,0)
pixBack = (255,255,255,0)
image_row = 413
image_col = 295
i = 0
j = 0
for i in range(image_col - 1):
    for j in range(image_row - 1):
            oneInchPic.putpixel((i,j),pixBack)
       
i = 0
j = 0
for i in range(image_col - 1):
    for j in range(image_row - 1):
        if j == 24:
            oneInchPic.putpixel((i,j),pixTuple)
        if (i == 70) and (j > 24):
            oneInchPic.putpixel((i,j),pixTuple)
        if (i == 225) and (j > 24):
            oneInchPic.putpixel((i,j),pixTuple)


        


oneInchPic.save("one-inch.jpg")
print(oneInchPic)
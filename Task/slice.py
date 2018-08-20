import cv2
import sys
import os
from PIL import Image

c=0
filename = "grey.jpg"
with Image.open(filename) as img:  # PIL
    width, height = img.size       #PIL

image = cv2.imread(filename)
h = height/5 #instead of 5 you can manually take an input from user.
b=h

for i in range(1,6):
	s = str(i)
	crop_img = image[c:b,0:376]
	cv2.imwrite("test"+s+".jpg",crop_img)
	c = b
	b = h+b

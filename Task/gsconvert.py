import cv2
import sys
import os

filename = "capture.jpg"
image = cv2.imread(filename)
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imwrite("grey.jpg", image)

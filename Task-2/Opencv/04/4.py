import cv2

import numpy as np

img = cv2.imread('c:/watch.jpg', cv2.IMREAD_COLOR)
img[55, 55] = [255, 255, 255]
px = img[55, 55]

img[100:150, 100:150]= [255,255,255]# creafing a white block on the images


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
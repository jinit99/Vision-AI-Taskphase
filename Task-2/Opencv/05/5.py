from typing import final
import cv2
import numpy as np

# Load two images
img1 = cv2.imread('D:/3D-Matplotlib.png')
img2 = cv2.imread('D:/mainlogo.png')
#img2 = cv2.imread('D:/mainsvmimage.png')

# I want to put logo on top-left corner, 
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]# region of image

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)# converting colour to black and white

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

final= cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = final

cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('final', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
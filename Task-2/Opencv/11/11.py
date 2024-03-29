import cv2
import numpy as np

img_rgb = cv2.imread('D:/opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('D:/opencv-template-for-matching.jpg', 0)
w, h = template.shape[::-1] # width and height
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(result >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow('Detected', img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()

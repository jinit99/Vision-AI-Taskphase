import numpy as np
import cv2

img = cv2.imread('c:/watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0, 0), (200, 300), (255, 255, 255), 10)# the brackets are for line start,end,colour, and linewidth
cv2.rectangle(img, (500, 250), (1000, 500), (0, 0, 255), 15)
cv2.circle(img, (50, 63), 55, (0, 0, 255), -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))# reshapping the lines
cv2.polylines(img, [pts], True, (0, 255, 255), 3)# location of the poly lines
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0, 100), font,
            1, (200, 255, 155), 5, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

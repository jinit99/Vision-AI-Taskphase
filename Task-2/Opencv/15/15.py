import numpy as np
import cv2

cap = cv2.VideoCapture('D:/opencv-python-foreground.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):# when the key q is pressed it exits
        break


cap.release()
cv2.destroyAllWindows()

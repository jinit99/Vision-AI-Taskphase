import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    kernel = np.ones((15, 15), np.float32)/225# to get 15 by 15 pixels
    smoothed = cv2.filter2D(result, -1, kernel)
    blur = cv2.GaussianBlur(result, (15, 15), 0)
    median = cv2.medianBlur(result, 15)
    bilateral = cv2.bilateralFilter(result, 15, 75, 75)
    cv2.imshow('Bilateral Blur', bilateral)
    cv2.imshow('Median Blur', median)

    cv2.imshow('Gaussian Blurring', blur)
    cv2.imshow('Original', frame)
    cv2.imshow('Averaging', smoothed)

    if cv2.waitKey(1) & 0xFF == ord('q'):# when the key q is pressed it exits
        break

cv2.destroyAllWindows()
cap.release()

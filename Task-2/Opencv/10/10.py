import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 150, 150)
    cv2.imshow('Original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)# for gradient in x
    cv2.imshow('sobely', sobely)# for gradient in y
    cv2.imshow('edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):# when the key q is pressed it exits
        break


cv2.destroyAllWindows()
cap.release()

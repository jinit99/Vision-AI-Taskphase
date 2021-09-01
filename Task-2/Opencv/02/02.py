import numpy as np
import cv2

cap = cv2.VideoCapture(0)# to capture the video from the first web cam the system has
fourcc = cv2.VideoWriter_fourcc(*'XVID')# to output the code somwhere
out = cv2.VideoWriter('2ndoutput.avi', fourcc, 20.0, (640, 480))
# here all the output commands refer for the output of the video file shown and how to save
while(True):
    ret, frame = cap.read()# this returns the video feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# this converts the colour(BGR) to gray
    out.write(frame)
    cv2.imshow('original video', frame)
    cv2.imshow('grayscale video', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):# when the key q is pressed it exits
        break

cap.release()
out.release()
cv2.destroyAllWindows()

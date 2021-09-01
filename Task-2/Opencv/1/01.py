import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('c:/watch.jpg', 0)# imread reads the image and imshow shows the image in different window


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# to plot using matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.show()

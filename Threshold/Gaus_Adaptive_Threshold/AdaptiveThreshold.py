#Yogesh Pawar
import cv2
import numpy as np

img=cv2.imread("bookpage.jpg",1)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
gaus=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("gray",gray)
cv2.imshow("img",img)
cv2.imshow("gaus",gaus)
cv2.waitKey(0)
cv2.destroyAllWindow()
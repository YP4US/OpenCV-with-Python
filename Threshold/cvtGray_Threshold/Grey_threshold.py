#Yogesh Pawar
import numpy as np
import cv2

img=cv2.imread("bookpage.jpg",1)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
ret,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

#grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret2,graythresh=cv2.threshold(gray,15,255,cv2.THRESH_BINARY)



cv2.imshow("img",img)
cv2.imshow("threshold",threshold)
cv2.imshow("graythresh",graythresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
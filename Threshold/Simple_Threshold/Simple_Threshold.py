#Yogesh Pawar
import numpy as np
import cv2

img=cv2.imread("bookpage.jpg",1)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
#threshold(src, dst, thresh, maxval, type)
ret,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
cv2.imshow("img",img)
cv2.imshow("threshold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
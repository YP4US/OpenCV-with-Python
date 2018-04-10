#Yogesh Pawar
import numpy as np
import cv2

img=cv2.imread("pvd.png",1)
cv2.namedWindow("1",cv2.WINDOW_NORMAL)
img2=img.copy()
cv2.imshow("1",img2)
cv2.waitKey()
cv2.destroyAllWindows()
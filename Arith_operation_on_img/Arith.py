#Yogesh Pawar
import numpy as np 
import cv2

img1=cv2.imread("3D-Matplotlib.png",1)
img2=cv2.imread("mainsvmimage.png",1)

#add=img1+img2
add=cv2.add(img1,img2)
cv2.namedWindow("add",cv2.WINDOW_NORMAL)
cv2.imshow("add",add)
cv2.waitKey(0)
cv2.destroyAllWindows()

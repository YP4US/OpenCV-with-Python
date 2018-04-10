#Yogesh Pawar
import numpy as np 
import cv2

img=cv2.imread("yogesh.jpg",1)
cv2.namedWindow("Img",cv2.WINDOW_NORMAL)

Pix=img[450,862]
print(Pix)
#Pix=[255,255,255]			#to change pixel value
#print(Pix)

ROI=img[176:250,207:294]	#ROI
img[0:74,0:87]=ROI			#COPY PASTE ROI
cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Yogesh Pawar
import cv2
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as matimg

img=cv2.imread("yogesh.jpg",1)
cv2.namedWindow("1",cv2.WINDOW_NORMAL)
xScale=0.5
yScale=0.5
scaleDown=cv2.resize(img,None,fx=xScale,fy=yScale,interpolation=cv2.INTER_LINEAR)     #resize
scaleUp=cv2.resize(img,None,fx=xScale*5,fy=yScale*5,interpolation=cv2.INTER_LINEAR)	  #resize
Crop=img[0:400,750:1250]

cv2.imshow("Scale Down Image",scaleDown)
cv2.imshow("Scale Up Image",scaleUp)
cv2.imshow("1",img)
cv2.imshow("cropped",Crop)
cv2.waitKey()
cv2.destroyAllWindows()

imageMat=matimg.imread("yogesh.jpg")   #read img using matplotlib to get coordinates
plt.imshow(imageMat)
plt.show()

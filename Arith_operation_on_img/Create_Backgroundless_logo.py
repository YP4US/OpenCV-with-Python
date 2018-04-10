#Yogesh Pawar
import numpy as np
import cv2

img1=cv2.imread("3D-Matplotlib.png",1)
img2=cv2.imread("mainlogo.png",1)
cv2.namedWindow("img1",cv2.WINDOW_NORMAL)
cv2.namedWindow("img2",cv2.WINDOW_NORMAL)

rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]

#create mask
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)	#convert it into gray
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)    #thresholding 

mask_inv=cv2.bitwise_not(mask)						#masking

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)		#inverse masking

img2_fg=cv2.bitwise_and(img2,img2,mask=mask)		#adding inveerse img to original img

dst=cv2.add(img1_bg,img2_fg)			#combine image
img1[0:rows,0:cols]=dst

cv2.imshow("res",img1)					#show combined logo image



#cv2.imshow("img2gray",img2gray)
#cv2.imshow("mask",mask)
#cv2.imshow("img1",img1)
#cv2.imshow("img2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
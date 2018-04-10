#Yogesh Pawar
import cv2
import numpy as np

frame=cv2.imread("yogesh.jpg")
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


lower_red=np.array([150,150,0])
upper_red=np.array([180,185,255])

mask=cv2.inRange(hsv,lower_red,upper_red)
res=cv2.bitwise_and(frame,frame,mask=mask)


#blurring
kernal=np.ones((20,20),np.float32)/400
smoothed=cv2.filter2D(res,-1,kernal)
#another method for blurr
blur=cv2.GaussianBlur(res,(15,15),0)
#one more blurr method
median=cv2.medianBlur(frame,11)



cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
cv2.namedWindow("mask",cv2.WINDOW_NORMAL)
cv2.namedWindow("res",cv2.WINDOW_NORMAL)
cv2.namedWindow("smoothed",cv2.WINDOW_NORMAL)
cv2.namedWindow("blur",cv2.WINDOW_NORMAL)
cv2.namedWindow("median",cv2.WINDOW_NORMAL)


cv2.imshow("frame",frame)
cv2.imshow("mask",mask)
cv2.imshow("res",res)
cv2.imshow("smoothed",smoothed)
cv2.imshow("blur",blur)
cv2.imshow("median",median)

cv2.waitKey(0)
cv2.destroyAllWindow()
cap.release()
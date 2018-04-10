#Yogesh Pawar
import cv2
import numpy as np

#cap=cv2.VideoCapture("ypgesh.jpg")

#while True:
#	ret,frame=cap.read()
#	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


#	lower_red=np.array([0,0,0])
#	upper_red=np.array([255,255,255])

#	mask=cv2.inRange(hsv,lower_red,upper_red)
#	res=cv2.bitwise_and(frame,frame,mask=mask)

#	cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
#	cv2.imshow("frame",frame)
#	#cv2.imshow("mask",mask)
#	#cv2.imshow("res",res)

frame=cv2.imread("yogesh.jpg")
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


lower_red=np.array([150,150,0])
upper_red=np.array([180,185,255])

mask=cv2.inRange(hsv,lower_red,upper_red)
res=cv2.bitwise_and(frame,frame,mask=mask)

cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
cv2.namedWindow("mask",cv2.WINDOW_NORMAL)
cv2.namedWindow("res",cv2.WINDOW_NORMAL)
cv2.imshow("frame",frame)
cv2.imshow("mask",mask)
cv2.imshow("res",res)


cv2.waitKey(0)
cv2.destroyAllWindow()
cap.release()


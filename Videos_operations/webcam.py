#Yogesh Pawar
import cv2
import numpy as numpy

cap=cv2.VideoCapture(0)

while True:
	ret, frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 


	cv2.imshow('Livefeed',frame)
	cv2.imshow('Gray',gray)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break

cap.release()
cap.destroyAllWindow()
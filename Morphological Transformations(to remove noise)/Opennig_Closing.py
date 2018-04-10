#Yogesh Pawar
import cv2
import numpy as np

frame = cv2.imread("yogesh.jpg",1)


hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
    
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)

kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.namedWindow("Mask",cv2.WINDOW_NORMAL)
cv2.namedWindow("opening",cv2.WINDOW_NORMAL)
cv2.namedWindow("closing",cv2.WINDOW_NORMAL)

cv2.imshow('Original',frame)
cv2.imshow('Mask',mask)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

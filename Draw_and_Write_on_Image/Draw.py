#Yogesh Pawar
#in all line type is optional: lineType=cv2.LINE_AA
#cv2.line ( image, starting point , end point , color , line thickness, line type)
#cv2.circle ( image, center, radius, color of border, line thickness / fill type, line type)
#cv2.ellipse ( image, center, axes lengths, rotation degree of ellipse, starting angle , ending angle, color, line thickness / fill type, line type)
#cv2.rectangle ( image, upper left corner vertex, lower right corner vertex, line thickness / fill type, line type)
#cv2.putText ( image, text, starting point of text, font type, font scale, color, linetype )

import cv2
import numpy as np

img=cv2.imread("yogesh.jpg",1)
cv2.namedWindow('1',cv2.WINDOW_NORMAL)


cv2.line(img,(0,0),(150,150),(155,55,15),20)
#cv2.line(img, (322, 179), (400, 183), (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.circle(img,(150,150),100,(0,0,255),15)
cv2.rectangle(img,(150,150),(750,750),(255,0,255),10)
# IMP Note: Ellipse Centers and Axis lengths must be integers
#cv2.ellipse(imageEllipse, (360, 200), (100, 170), 45, 0, 360, (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.ellipse(img,(750,750),(100,170),45,0,360,(150,75,200),5)
cv2.putText(img,"Hello My cat",(950,850),cv2.FONT_HERSHEY_SIMPLEX,2,(120,255,100),5,lineType=cv2.LINE_AA)

cv2.imshow('1',img)
cv2.waitKey(0)
cv2.destroyAllWindow()

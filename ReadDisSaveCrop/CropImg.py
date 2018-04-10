#Yogesh Pawar
import cv2
import numpy
img=cv2.imread("yogesh.jpg",1)
cv2.namedWindow("1",cv2.WINDOW_NORMAL)
img[300:350,100:500]=[255,255,255]
Kat_face=img[37:111,107:194]
img[0:74,0:87]=Kat_face #[0:111-37,0,194-107]
cv2.imshow("1",img)
cv2.waitKey()
cv2.destroyAllWindows()
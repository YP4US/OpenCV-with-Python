#Yogesh Pawar
import numpy as np
import cv2

img=cv2.imread("yogesh.jpg",1)
cv2.namedWindow("1",cv2.WINDOW_NORMAL)
NoOfRow=img.shape[0]
NoOfCol=img.shape[1]
NoOfChan=img.shape[2]
print("Number of Rows in img:")
print(NoOfRow)
print("Number of Columns in img:")
print(NoOfCol)
print("Number of channels in img(in colour img only):")
print(NoOfChan)
cv2.imshow("1",img)
cv2.waitKey()
cv2.destroyAllWindows()
#Yogesh Pawar
import numpy
import cv2


img=cv2.imread("yogesh.jpg",1)			#read
cv2.imwrite("alex.jpg",img)				#write
cv2.namedWindow("1",cv2.WINDOW_NORMAL)	#set windowsize
cv2.imshow("1",img)						#display
cv2.waitKey(0)							#holddisplay	
cv2.destroyAllWindows()					#close windows
print("Program ended")
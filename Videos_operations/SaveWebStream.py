#Yogesh Pawar
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
savefourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',savefourcc,20.0,(640,480))

while True:
		ret, frame=cap.read()
		out.write(frame)
		cv2.imshow('Frame', frame)

		if cv2.waitKey(1) & 0xFF ==ord('q'):
			break

cap.release()
out.release()
cap.destroyAllWindow()

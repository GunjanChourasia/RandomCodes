import cv2
import numpy as np

#cap=cv2.VideoCapture(0)
ret=True
while ret:
	#ret,cam=cap.read()
	cam=cv2.imread('ob.jpg')
	mask = cv2.inRange(cam, (np.array([97,46,17])), (np.array([117,46,17])))
	cv2.imshow("Masking",mask)
	erode = cv2.erode(mask,None,iterations = 1)
	dilate = cv2.dilate(erode,None,iterations = 1)
	image,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(cam,contours,-1,(255,0,0),3)
	cv2.imshow("cam",cam)
	if contours:
		for cnt in contours:
			x, y, w, h = cv2.boundingRect(cnt)
	        cv2.rectangle(cam,(x,y),(x+w,y+h),[255,0,0],2)

	if cv2.waitKey(5)==27:
		break
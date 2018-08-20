import cv2
import numpy as np

cap=cv2.VideoCapture(1)
ret=True
while ret:
	ret,cam=cap.read()
	#yuv=cv2.cvtColor(cam,cv2.COLOR_BGR2YUV)
	cv2.imshow("yuv",cam)
	#mask = cv2.inRange(cam, (np.array([97,46,17])), (np.array([117,46,17])))
	if cv2.waitKey(1)==ord("c"):
		cv2.imwrite("fan18.jpg",cam)
		#cv2.imshow("fan.jpg")

	'''erode = cv2.erode(mask,None,iterations = 1)
	dilate = cv2.dilate(erode,None,iterations = 1)
	image,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(cam,contours,-1,(255,0,0),3)
	cv2.imshow("cam",cam)
	ret,cam=cap.read()
	if contours:
		for cnt in contours:
			x, y, w, h = cv2.boundingRect(
			cnt)
	        cv2.rectangle(cam,(x,y),(x+w,y+h),[255,0,0],2)'''

	if cv2.waitKey(5)==27:
		break
cap.release()
cv2.destroyAllWindows()
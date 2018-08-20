#!/usr/bin/env python
import cv2
import numpy as np



try:
	index = sys.argv[1]
except:
	index = 1

flag = True

cap = cv2.VideoCapture(index)

u_blue,v_blue = 183,66
u_red,v_red =98,233
u_yellow,v_yellow =101,66
kernel = np.ones((5,5),np.uint8)


def detect():

	global cap,y,u,v,kernel,width,height,flag,area,state,paramx,paramy,x1,y1,stop,u_blue,v_blue,u_red,v_red,u_yellow,v_yellow
	x,y,h,w = 0,0,0,0
	
		
	ret,frame = cap.read()

	img_yuv = cv2.cvtColor(frame,cv2.COLOR_BGR2YUV)
	mask_blue = cv2.inRange(img_yuv, (np.array([0,u_blue-30,v_blue-30])), (np.array([255,u_blue+30,v_blue+30])))
	mask_red = cv2.inRange(img_yuv, (np.array([0,u_red-30,v_red-30])), (np.array([255,u_red+30,v_red+30])))
	mask_yellow = cv2.inRange(img_yuv, (np.array([0,u_yellow-30,v_yellow-30])), (np.array([255,u_yellow+30,v_yellow+30])))



	#FOR BLUE
	erode_b = cv2.erode(mask_blue,kernel,iterations = 1)
	dilate_b = cv2.dilate(erode_b,kernel,iterations = 1)
	image_b,contour_b,hierarchy_b = cv2.findContours(dilate_b,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


	#FOR RED
	erode_r = cv2.erode(mask_red,kernel,iterations = 1)
	dilate_r = cv2.dilate(erode_r,kernel,iterations = 1)
	image_r,contour_r,hierarchy_r = cv2.findContours(dilate_r,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	#FOR YELLOW
	erode_y = cv2.erode(mask_yellow,kernel,iterations = 1)
	dilate_y = cv2.dilate(erode_y,kernel,iterations = 1)
	image_y,contour_y,hierarchy_y = cv2.findContours(dilate_y,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


	if cv2.waitKey(5) == 27:
		flag = False
	
	
	if contour_b or contour_y or contour_r :
	 
	
		if contour_b:

			for i in range(0,len(contour_b)):
				b1=[]
				b2=[]
				if cv2.contourArea(contour_b[i])>1000:
					x, y, w, h = cv2.boundingRect(contour_b[i])
	        		cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2)
	        		print "Blue obstacle:",cv2.contourArea(contour_b[i])
	        		cv2.imshow("YUV",frame)
	        		b1.append((x+h)/2)
	        		b2.append((y+w)/2)
	        		print b1,b2
	        		if len(b1)>1:
	        			


		if contour_r:

			for i in range(0,len(contour_r)):
				r1=[]
				r2=[]
				if cv2.contourArea(contour_r[i])>1000:
					x, y, w, h = cv2.boundingRect(contour_r[i])
	        		cv2.rectangle(frame,(x,y),(x+w,y+h),[0,0,255``],2)
	        		print "Blue obstacle:",cv2.contourArea(contour_r[i])
	        		cv2.imshow("YUV",frame)
	        		r1.append((x+h)/2)
	        		r2.append((y+w)/2)
	        		print r1,r2

		if contour_y:

			for i in range(0,len(contour_y)):
				y1=[]
				y2=[]
				if cv2.contourArea(contour_y[i])>1000:
					x, y, w, h = cv2.boundingRect(contour_y[i])
	        		cv2.rectangle(frame,(x,y),(x+w,y+h),[0,255,0],2)
	        		print "Green obstacle:",cv2.contourArea(contour_y[i])
	        		cv2.imshow("YUV",frame)
	        		y1.append((x+h)/2)
	        		y2.append((y+w)/2)
	        		print y1,y2

	else:
		cv2.imshow("YUV",frame)

while flag:
	detect()







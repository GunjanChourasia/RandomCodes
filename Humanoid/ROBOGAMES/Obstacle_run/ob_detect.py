import cv2
import numpy as np
from math import pi


f=cv2.imread('board.jpg')
f1=cv2.imread('green.jpg')   
img_yuv = cv2.cvtColor(f, cv2.COLOR_BGR2YUV)
img = cv2.cvtColor(f1, cv2.COLOR_BGR2YUV)

 

'''refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
 
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
    elif cropping==True:
        refPt.append((x+10, y+10))
        cropping = False
 
    
        

 
clone = img_yuv.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)'''
 
#cv2.imwrite("image_hsv_board.jpg",img_yuv)
'''while True:
    cv2.imshow("image", img_yuv)
    key = cv2.waitKey(1) & 0xFF
 

    if key == ord("r"):
        image = clone.copy()
 
    elif key == ord("c"):
        break
 

if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    #cv2.imshow("ROI", roi)
    count=0
    sum=np.array([0,0,0])
    for i in range (0,np.size(roi,0)):
        for j in range(0,np.size(roi,1)):
            count+=1
            sum+=roi[i,j]
    [y,u,v]=np.array(sum/count)
    drag_area=np.size(roi,0)*np.size(roi,1)
    print "drag area",drag_area
    print [y,u,v]'''
#[141 145 104][133, 128, 104]
#[102, 133, 116]
mask = cv2.inRange(img_yuv, (np.array([0,133-17,116-17])), (np.array([102+17,133+17,116+17])))
erode = cv2.erode(mask,None,iterations = 1)
dilate = cv2.dilate(erode,None,iterations = 1)
image,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#[120, 128, 130]
mask1 = cv2.inRange(img, (np.array([107,115,117])), (np.array([133,141,143])))

#alpha = beta = 1
#abc = cv2.addWeighted(mask,alpha,mask1,beta,0.0)
cv2.imshow("Masking_yuv_board",mask)
cv2.imshow("Masking_yuv_board_1",mask1)

#lur=cv2.GaussianBlur(mask1,(5,5),50)
erode1 = cv2.erode(mask1,None,iterations = 4)
dilate1 = cv2.dilate(erode1,None,iterations = 50)
image1,contours1,hierarchy1 = cv2.findContours(dilate1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt)>1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_yuv,(x,y),(x+w,y+h),[255,0,0],2)
        print "Blue obstacle:",cv2.contourArea(cnt)
        b1=(x+h)/2
        b2=(y+w)/2
        print b1,b2

for cnt1 in contours1:
    if cv2.contourArea(cnt1)>1000:
        x1, y1, w1, h1 = cv2.boundingRect(cnt1)
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),[0,0,255],2)
        print "Red obstacle:",cv2.contourArea(cnt1)
        r1=(x1+h1)/2
        r2=(y1+w1)/2
        print r1,r2



'''area=0
c=0
while contours and c<len(contours):
    if cv2.contourArea(contours[c])>10000:
        area+=cv2.contourArea(contours[c])
    else:
        area-=cv2.contourArea(contours[c])
    c+=1
    



#area = cv2.contourArea(cnt)
center=(327,166)
radius=87

area1=pi*(radius**2)
print "Total_area",area1
print "area_yuv",area
print "Error% ",(area1-area)*100/area1
cv2.drawContours(img_yuv, contours, -1, (0,255,0), 2)
#cv2.circle(img_yuv,center,radius,(0,0,255),2)
cv2.imshow("contour_yuv_board", img_yuv)'''

cv2.imshow("Output_img",img_yuv)
cv2.imshow("Output_img1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
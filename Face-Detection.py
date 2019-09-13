#Creating mask
#define the upper and lower bounderies of the HSV ixel
#intensities to be considered "Skin"

import cv2
import numpy as np

img=cv2.imread("Trump.png")
lower=np.array([0,48,30],dtype="uint8")
upper=np.array([20,255,255],dtype="uint8")
frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
skinmask=cv2.inRange(frame,lower,upper)
cv2.imshow("Out",skinmask)
cv2.imshow("Out3",frame)
#apply a series of erosions and dilations to the mask
#using an elliptical kernel

kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
skinmask=cv2.erode(skinmask,kernel,iterations=2)
skinmask=cv2.dilate(skinmask,kernel,iterations=2)
cv2.imshow("Out1",skinmask)
#Blur the mask to help remove noise then apply the mask to frame

skinmask=cv2.GaussianBlur(skinmask,(3,3),0)
skin=cv2.bitwise_and(frame,frame,mask=skinmask)

cv2.imshow("Out2",skin)
cv2.waitKey()
cv2.destroyAllWindows()

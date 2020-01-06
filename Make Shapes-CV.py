import cv2
import numpy as np
import matplotlib.pyplot as plt 
#Resize the image to 600x600
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
#BGR
img=cv2.imread('1.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),10)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV rocks',(300,300),font,5,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.imwrite("text-shapes.jpg",img)
cv2.waitKey()
cv2.destroyAllWindows()
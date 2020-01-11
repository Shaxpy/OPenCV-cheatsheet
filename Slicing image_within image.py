import numpy as np
import cv2

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
img=cv2.imread('1.jpg',cv2.IMREAD_COLOR)
img[55,55]=[255,255,255]
px=img[55,55]
print(px)

img[100:150,100:150]=[255,255,255]
# wat=img[1200:1012,1627:1041]
# img[0:95,0:670]=wat
print(img)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
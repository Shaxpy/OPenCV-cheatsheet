import cv2
import numpy as np
import matplotlib.pyplot as plt 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
img=cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()
cv2.imwrite('bnw.jpg',img)
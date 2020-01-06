import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#--IF WE WANNA TAKE A VIDEO OF INTRUDER
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # out.write(frame)
    cv2.imshow('cap',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
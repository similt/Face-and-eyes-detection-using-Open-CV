import cv2
import numpy as np
import matplotlib.pyplot as plt
##Face
img=cv2.imread("test.jpg")
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
##Eyes
eyes = eye_cascade.detectMultiScale(roi_gray)
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

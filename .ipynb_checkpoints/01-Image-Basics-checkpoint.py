import cv2 as cv
import numpy as np
img = np.zeros((500,800,3))

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),10,(0,0,255),5)

cv.namedWindow(winname="my_drawing")

cv.setMouseCallback("my_drawing",draw_circle)

while True:
    cv.imshow("my_drawing",img)
    if cv.waitKey(20) & 0xFF == 27:
        break
        
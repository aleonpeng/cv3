import cv2
import numpy as np
from matplotlib import pyplot as plt

imgviewx=cv2.imread("E:/opencv/demo/pic/matchshape/a.bmp",cv2.IMREAD_COLOR)
width, heigh, channel =imgviewx.shape
print(imgviewx.size)
print(imgviewx.dtype)
print(cv2.mean(imgviewx))

image=imgviewx.copy()

font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image,"DONG XIAO DONG",(10, 50), font, 1.2, (0, 0, 255), 5)
cv2.namedWindow("operation", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("operation",heigh,width)
cv2.resizeWindow("operation",480,640)
#cv2.imshow("Demo",image)

b,g,r=cv2.split(image)
imgray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(imgray, 175, 255, cv2.THRESH_BINARY)
ret, connect = cv2.connectedComponents(thresh1)
#ret,threadimg=cv2.threshold(imgray,120,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
#threadimg=cv2.adaptiveThreshold(imgray,100,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,5)
cv2.imshow("operation",thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(cv2.getVersionRevision())
print(cv2.getVersionString())
#plt.imshow(thresh1,'gray')
#plt.show()
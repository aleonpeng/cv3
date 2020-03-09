import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.getVersionString())
img = cv2.imread('E:/opencv/demo/pic/matchtemplate/a.jpg', cv2.IMREAD_COLOR)
print(img.shape)
img2 = img[670:1056, 423:600]
print(img2.shape)
cv2.imshow('1', img2)
cv2.waitKey(0)
"""
cv2.imshow('2', img)
cv2.imshow('1', img2)
cv2.waitKey(0) & 0xFF == ord('q')
htich = np.hstack((thresh,thresh))
cv2.imshow("merged_img", img2)
cv2.waitKey(0)
"""
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh2 = cv2.threshold(imgray2, 127, 255, cv2.THRESH_TOZERO)
print(thresh.shape)
print(thresh2.shape)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
print(cnt1)
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours[0]
#cv2.imshow("merged_img", cnt2)
#cv2.waitKey(0)
#ret2 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)

ret2 = cv2.matchTemplate(img, img2, 1, result=None, mask=None)
print(ret2)
cv2.destroyAllWindows()
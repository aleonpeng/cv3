import cv2
import numpy as np
from matplotlib import pyplot as plt

src0 = 'E:/opencv/demo/pic/matchshape/a.bmp'
src1 = 'E:/opencv/demo/pic/matchshape/b.bmp'
print(cv2.getVersionString())
img = cv2.imread(src0, cv2.IMREAD_COLOR)
print(img.shape)
img2 = cv2.imread(src1, cv2.IMREAD_COLOR)
print(img2.shape)
"""
htich = np.hstack((img, img2))
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 1080, 640)
cv2.imshow('image', htich)
cv2.waitKey(0) & 0xFF == ord('q')


plt.imshow(htich)
plt.show()
"""
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh2 = cv2.threshold(imgray2, 127, 255, cv2.THRESH_TOZERO)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt1 = contours[0]
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours[0]

rage2D = cv2.minAreaRect(cnt2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 1080, 640)
cv2.imshow('image', contours)
cv2.waitKey(0)

ret2 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print('The similar value is : ' + str(ret2))

cv2.destroyAllWindows()
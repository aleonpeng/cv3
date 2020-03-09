import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('E:/halcon/opencv/aa.jpg', cv2.IMREAD_COLOR)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.medianBlur(imgray, 5)
ret, th1 = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
titles = ['Original','Global Thresholding(v = 127)','Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']
images = [imgray, th1, th2, th3]
for i in range(len(images)):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

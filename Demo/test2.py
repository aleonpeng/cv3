import cv2
import numpy as np
from matplotlib import pyplot as plt

# encoding:utf-8
#
'''
img = cv2.imread('E:/halcon/opencv/aa.jpg',cv2.IMREAD_COLOR)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(imgray, 127, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(imgray, 127, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(imgray, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [imgray, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
'''

imgx=np.zeros([400,600,3],np.uint8)

imgx[100:300,100:400,2]=np.ones([200,300],np.uint8)*255
imgx[100:300,100:400,1]=np.ones([200,300],np.uint8)*255
cv2.imshow(u"第二个图形窗口",imgx)
cv2.waitKey(0)
cv2.destroyAllWindows()
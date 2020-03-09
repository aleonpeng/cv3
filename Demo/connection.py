import cv2
import numpy as np
from matplotlib import pyplot as plt

src0 = 'E:/opencv/demo/pic/matchshape/a.bmp'

img = cv2.imread(src0, cv2.IMREAD_COLOR)
print(img.shape)

image_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh1 = cv2.threshold(image_gray, 175, 255, cv2.THRESH_BINARY)
ret, connect = cv2.connectedComponents(thresh1)


#contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#connect, stats, centroids = cv2.connectedComponentsWithStats(thresh1)

label_hue = np.uint8(179*connect/np.max(connect))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

# cvt to BGR for display
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

# set bg label to black
labeled_img[label_hue==0] = 0
cv2.namedWindow('labeled',cv2.WINDOW_NORMAL)
cv2.resizeWindow('labeled', 480, 640)
cv2.imshow('labeled', labeled_img)
cv2.waitKey()

cv2.destroyAllWindows()
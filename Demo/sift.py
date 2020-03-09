#
#  FLANN匹配
#
#
import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils
import glob


Image = 'E:/halcon/logo/model7/a.jpg'
Image_1 = 'E:/halcon/logo/model7/b.jpg'

ModelImage = cv2.imread(Image)
rightImage = cv2.imread(Image_1)
leftImage = ModelImage[1140:1857, 2357:3473]
# 创造sift
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(leftImage, None)
kp2, des2 = sift.detectAndCompute(rightImage, None)  # 返回关键点信息和描述符


FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees = 3)
searchParams = dict(checks = 50  )  # 指定索引树要被遍历的次数

flann = cv2.FlannBasedMatcher(indexParams, searchParams)
matches = flann.knnMatch(des1, des2, k=2)
matchesMask = [[0 ,0] for i in range(len(matches))]
print("matches:", matches)
for i, (m ,n) in enumerate (matches):
    print(m.distance)
    if m.distance < 0.07 * n.distance:
        matchesMask[i] = [1, 0]

drawParams = dict(matchColor = (0, 255, 0), singlePointColor=None,
                  matchesMask = matchesMask, flags = 2  )  # flag=2只画出匹配点，flag=0把所有的点都画出
resultImage = cv2.drawMatchesKnn(leftImage ,kp1 ,rightImage ,kp2 ,matches ,None ,**drawParams)
plt.imshow(resultImage)
plt.show()

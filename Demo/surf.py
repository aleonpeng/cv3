import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils
import glob


src0 = 'E:/halcon/logo/model7/Model.bmp'
img_dir = 'E:/halcon/logo/model7'
print(cv2.getVersionString())
img = cv2.imread(src0,  cv2.COLOR_BGR2GRAY)
print(img.shape)

roi = img[1140:1857, 2357:3473]
Canny = cv2.Canny(roi, 50, 200)


surf = cv2.xfeatures2d.SURF_create(400)
surf.setUpright(True)
print(surf.getUpright())
image = roi
kp1, desc_query = surf.detectAndCompute(img, None)
draw_model = cv2.drawKeypoints(image, kp1, image)
print(surf.descriptorSize())

#nst = np.hstack((img, draw_img))

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 1080, 640)

for imagePath in glob.glob(img_dir + "/*.bmp"):
    image = cv2.imread(imagePath, cv2.COLOR_BGR2GRAY)
    found = None

    kp2, desc_query = surf.detectAndCompute(image, None)
    test = cv2.drawKeypoints(image, kp2, image)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(test,draw_model,k=2)

    good = [[m] for m, n in matches if m.distance < 0.5 * n.distance]
    img3 = cv2.drawMatchesKnn(draw_model, kp1, test, kp2, good, None, flags=2)

    cv2.imshow('image', img3)
    cv2.waitKey(0)

    print(imagePath)

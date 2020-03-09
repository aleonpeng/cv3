import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
import time

src0 = 'E:/opencv/demo/pic/matchtemplate/a.jpg'
src1 = 'E:/opencv/demo/pic/matchtemplate/a.jpg'

img = cv.imread(src0,cv.IMREAD_COLOR)
#image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

temp = img[670:1056, 423:600]  # 脸部

def template_demo(image, template):

    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]   #3种模板匹配方法
    th, tw = template.shape[:2]
    for md in methods:
        starttime = datetime.now()

        print('Method is: ' + str(md))
        result = cv.matchTemplate(image, template, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(image, tl, br, (0, 0, 255), 2)
        cv.namedWindow("match-" + np.str(md), cv.WINDOW_NORMAL)
        cv.imshow("match-" + np.str(md), image)
        print('min_value: ' + str(min_val) + '; max_value:' + str(max_val) + '; min_loc: ' + str(min_loc) + '; max_loc: ' + str(max_loc))

        endtime = datetime.now()
        durn = (endtime - starttime).microseconds

        print('Run During is:' + str(durn/1000))

template_demo(img, temp)
cv.waitKey(0)
cv.destroyAllWindows()
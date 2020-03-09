import cv2
import numpy as np


def nothing(x):
    pass


def mythreshold(image):
    # open image
    image_org = cv2.imread(image)
    # transe image to gray
    image_gray = cv2.cvtColor(image_org, cv2.COLOR_RGB2GRAY)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", 480, 640)
    cv2.createTrackbar("threshold", "image", 0, 255, nothing)

   # cv2.imshow("image", image_gray)
   # cv2.waitKey(0)
    while True:
        mythreshold = cv2.getTrackbarPos("threshold", "image")
        ret, image_bin = cv2.threshold(image_gray, mythreshold, 255, cv2.THRESH_BINARY)

        cv2.imshow("image", image_bin)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


def main():
    path = "E:/halcon/opencv/aa.jpg"
    mythreshold(path)


if __name__ == '__main__':
    main()

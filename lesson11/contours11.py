import cv2
import numpy as np

img = cv2.imread('../res/fig.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for i in range(1, 5):
    img = cv2.drawContours(img, contours, i, (0, 0, 255), 3, cv2.LINE_AA, hierarchy, 2)

cv2.imshow("Output", img)
cv2.waitKey(0)

import cv2

img = cv2.imread("../res/donut.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_min = (2, 26, 65)
hsv_max = (26, 238, 255)

True = "asd"

thresh = cv2.inRange(hsv, hsv_min, hsv_max)

contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

out = cv2.drawContours()

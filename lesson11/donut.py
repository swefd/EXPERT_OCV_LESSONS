import cv2

img = cv2.imread("../res/donut.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_min = (2, 28, 70)
hsv_max = (26, 255, 255)

thresh = cv2.inRange(hsv, hsv_min, hsv_max)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)

import cv2


def nothing(self):
    pass


cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)
cv2.createTrackbar("MyTrackbar", "Trackbars", 0, 255, nothing)

while True:
    l_h = cv2.getTrackbarPos("myTrackBar", "Trackbars")
    cv2.imshow("Trackbars", l_h)
    cv2.waitKey(1)

import cv2

# 31, 91, 42


#cap = cv2.VideoCapture(2)

cap = cv2.imread("../res/donut.jpg")


def nothing(self):
    pass


cv2.namedWindow("GetColor")
cv2.createTrackbar("Hue", "GetColor", 0, 255, nothing)
cv2.createTrackbar("Sat", "GetColor", 0, 255, nothing)
cv2.createTrackbar("Val", "GetColor", 0, 255, nothing)

while True:
    #_, frame = cap.read()
    frame = cap
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hValue = cv2.getTrackbarPos("Hue", "GetColor")
    sValue = cv2.getTrackbarPos("Sat", "GetColor")
    vValue = cv2.getTrackbarPos("Val", "GetColor")
    lower = (hValue, sValue, vValue)
    higher = (255, 255, 255)
    mask = cv2.inRange(hsv, lower, higher)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    final = cv2.hconcat([frame, res])
    cv2.imshow("GetColor", final)
    cv2.imshow("mask", mask)
    cv2.waitKey(1)

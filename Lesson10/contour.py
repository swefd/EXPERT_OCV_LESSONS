import cv2


def noth(self):
    pass


cap = cv2.VideoCapture(2)
cv2.namedWindow("Filter")
cv2.createTrackbar("Switch", "Filter", 0, 2, noth)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (80, 100, 100), (150, 255, 255))
    swch = cv2.getTrackbarPos("Switch", "Filter")

    res = cv2.bitwise_and(frame, frame, mask=mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 900:
            x, y, w, h, = cv2.boundingRect(contour)
            print(w)
            if swch == 0:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            elif swch == 1:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            elif swch == 2:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Filter", frame)
    cv2.waitKey(1)

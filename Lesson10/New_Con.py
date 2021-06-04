import cv2

# cap = cv2.imread("../res/apple.jpg")
cap = cv2.VideoCapture(2)

cv2.namedWindow("Filter")

while True:
    _, frame = cap.read()
    # frame = cap
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (30, 0, 40), (70, 255, 255))
    res = cv2.bitwise_and(frame, frame, mask=mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        if cv2.contourArea(contour) > 900:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            #frame = cv2.drawContours(frame, contours, 0, (0, 0, 255), 3, cv2.LINE_AA, hierarchy, 2)

    cv2.imshow("Filter", frame)
    cv2.waitKey(1)

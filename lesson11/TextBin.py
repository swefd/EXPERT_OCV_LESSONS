import cv2

img = cv2.imread("../res/text.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (70, 0, 0), 1)
    cv2.imshow("Output", img)
    # cv2.imshow("Mask", thresh)
    cv2.waitKey(0)

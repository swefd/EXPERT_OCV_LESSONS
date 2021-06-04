import cv2

image_file = '../res/text.png'
img = cv2.imread(image_file)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(img, (x,y), (x + w, y + h), (150, 0, 0), 1)

    cv2.imshow("img", img)
    cv2.imshow("Output", img)
    cv2.waitKey(0)
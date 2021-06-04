import cv2

img = cv2.imread("../res/apple.jpg")
cv2.rectangle(img, (20, 40), (150, 120), (255, 0, 0),5)
cv2.rectangle(img, (300, 300), (500, 450), (0, 255, 0),5)
cv2.rectangle(img, (530, 20), (450, 450), (0, 0, 255),5)
cv2.imshow("Apple", img)
cv2.waitKey(0)

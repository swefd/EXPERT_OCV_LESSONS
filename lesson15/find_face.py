import cv2

img = cv2.imread("../res/vandam.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


face = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

faces = face.detectMultiScale(gray, 1.5, 4, 0, (30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("test", img)
cv2.waitKey(0)
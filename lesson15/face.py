import cv2

cap = cv2.VideoCapture(0)

path = "../haarcascades/haarcascade_eye_tree_eyeglasses.xml"

face = cv2.CascadeClassifier(path)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.05, 4, 0, (30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ( x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', frame)
    cv2.waitKey(1)

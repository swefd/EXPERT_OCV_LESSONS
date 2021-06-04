# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2


face_cascode_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(12)


while True:
    success, img = cap.read()

    #img = cv2.imread("test3.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascode_db.detectMultiScale(img_gray, 1.1, 19)

    for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)


    cv2.imshow("test", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
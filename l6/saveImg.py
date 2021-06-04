import cv2

cap = cv2.VideoCapture(4)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('p'):
        cv2.imwrite('img/first.png', frame)
    elif cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

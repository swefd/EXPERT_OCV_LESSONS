import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

while True:  # Нескінченний цикл
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):  # Перевірка чи нажата кнопка
        break
cap.release()  # Закриття відеопотоку
out.release()  # Закритття потоку запису
cv2.destroyAllWindows()

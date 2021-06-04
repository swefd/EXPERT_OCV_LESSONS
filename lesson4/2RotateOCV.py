import cv2

img = cv2.imread('../res/cat.png')

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


cv2.namedWindow('rot90', cv2.WINDOW_NORMAL)
cv2.imshow('rot90', img)
cv2.waitKey(0)

import cv2

img = cv2.imread('../res/cat.png')

img = cv2.flip(img, 1)


cv2.namedWindow('Flip', cv2.WINDOW_NORMAL)
cv2.imshow('Flip', img)

cv2.waitKey(0)


cv2.waitKey()







import cv2
import numpy

img = cv2.imread('../res/cat.png')
array = numpy.array(img)
array90 = numpy.rot90(array, 3)


cv2.namedWindow('rot90', cv2.WINDOW_NORMAL)
cv2.imshow('rot90', array90)
cv2.waitKey(0)

#filter colouring on photo

import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\bl.png")

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# Threshold of blue in HSV space
lower_blue = np.array([60, 35, 140])

upper_blue = np.array([180, 255, 255])

mask = cv.inRange(hsv, lower_blue, upper_blue)

result = cv.bitwise_and(img, img, mask=mask)

cv.imshow('frame', img)

cv.imshow('mask', mask)

cv.imshow('result', result)

cv.waitKey()

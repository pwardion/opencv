#colour filtering on image

import cv2 as cv
img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\cr.jpg")

low = (160,50,50)
up = (180,255,255)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, low,up) #inrange maskeleme için kullanılır

res = cv.bitwise_and(img,img,mask=mask)

cv.imshow("original", img)

cv.imshow("masked", mask)

cv.imshow("result",res)

cv.waitKey()

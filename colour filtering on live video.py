#colour filtering on live video

import cv2 as cv
cap = cv.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    low = (160, 50, 50)
    up = (180, 255, 255)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, low, up)  # inrange maskeleme için kullanılır

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("original", frame)

    cv.imshow("masked", mask)

    cv.imshow("result", res)
    cv.waitKey(1)

cap.release()
cv.destroyAllWindows()


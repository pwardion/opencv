import cv2 as cv

cap = cv.VideoCapture("C:\\Users\\berka\\OneDrive\\Desktop\\vtest.avi")

while cap.isOpened():
    _, frame1 = cap.read()
    _, frame2 =  cap.read()
    diff = cv.absdiff(frame1,frame2)

    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

    blurred = cv.GaussianBlur(gray, (5,5), sigmaX=0)

    _, threshold = cv.threshold(blurred, 20,255,cv.THRESH_BINARY)

    dilate = cv.dilate(threshold, (5,5))

    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv.boundingRect(contour)

        if cv.contourArea(contour) < 900:

            continue
        cv.rectangle(frame1, (x,y),(x+w,y+h), color=(0,255,0), thickness=2)

        cv.imshow("asd", frame1)





    cv.waitKey(50)

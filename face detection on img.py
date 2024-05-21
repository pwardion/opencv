import cv2 as cv

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\indir.webp")

source = r"C:\\Users\\berka\\OneDrive\\Desktop\\haarcascade_frontalface_default.xml"

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cascade = cv.CascadeClassifier(source)
faces = cascade.detectMultiScale(gray, 1.2,5)

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h),color=(0,255,0), thickness=3)

cv.imshow("asd", img)


cv.waitKey()
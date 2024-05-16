import cv2 as cv

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\cr.jpg")


def nothing(x):
    pass

cv.namedWindow("frame")

cv.createTrackbar("min","frame",0,255,nothing)
cv.createTrackbar("max","frame",0,255,nothing)


while True:

    test1 = cv.getTrackbarPos("min","frame")
    test2 = cv.getTrackbarPos("max","frame")
    #minThreshold: İlk eşik değeri. Kenarlar belirlenirken kullanılan ikinci eşik değerinin altında kalan kenar
    # pikselleri olarak kabul edilir.

    #maxThreshold: İkinci eşik değeri. Kenarlar belirlenirken kullanılan birinci
    #eşik değerinin üstünde kalan kenar pikselleri olarak kabul edilir.

    cannyimg = cv.Canny(img,test1,test2)
              #cv.Canny(source, minThreshold, maxThreshold)

    cv.imshow('frame', cannyimg)

    key = cv.waitKey(1)

    if key==ord('q'):

        break
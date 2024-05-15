import cv2 as cv #cv2 cv olarak import edildi

cap = cv.VideoCapture(0) #kameradan değer okundu

def nothing(x): #boş bir fonksiyon tanımlandı
    pass

cv.namedWindow("frame") #yeni bir pencere oluşturulup isimlendirildi

cv.createTrackbar("test","frame",50,250,nothing) #yeni bir trackbar oluşturuldu
#cv.createTrackbar("trackbarName","windowName",minVal,maxVal,nothing)

while True:

    _, frame = cap.read()

    cv.imshow("frame",frame)

    test = cv.getTrackbarPos("test","frame") #trackbarın verisi okundu

    print(test)

    key = cv.waitKey(1)

    if key==ord('q'):

        break

cap.release()

cv.destroyAllWindows()
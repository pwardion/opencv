import cv2 as cv #cv2 cv olarak import edildi
import cv2

image1 = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\resim.jpg")

img = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)




def nothing(x): #boş bir fonksiyon tanımlandı
    pass

cv.namedWindow("frame") #yeni bir pencere oluşturulup isimlendirildi
cv.namedWindow("frame1")
cv.createTrackbar("blockSize","frame",2,250,nothing) #yeni bir trackbar oluşturuldu
cv.createTrackbar("C","frame",2,250,nothing)
#cv.createTrackbar("trackbarName","windowName",minVal,maxVal,nothing)

while True:

    test1 = cv.getTrackbarPos("C","frame") #trackbarın verisi okundu
    test2 = cv.getTrackbarPos("blockSize","frame")

    if test1%2==0:
        test1+=1

    if test2%2==0:
        test2+=1
    if test1==0:
        test1+=1
    if test2==0:
        test2+=2

    thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, test2, test1)

    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, test2, test1)

    r1 = cv2.resize(thresh1, (600, 600))
    r2 = cv2.resize(thresh2, (600, 600))
    cv2.imshow('Adaptive Mean', r1)
    cv2.imshow('Adaptive Gaussian', r2)

    key = cv.waitKey(1)

    if key==ord('q'):

        break


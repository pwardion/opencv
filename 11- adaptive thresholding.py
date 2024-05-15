import cv2 #cv2 import edildi

image1 = cv2.imread("C:\\Users\\berka\\OneDrive\\Desktop\\resim.jpg",0) #resim okundu



#blockSize arttıkça detay artar
#C arttıkça resim beyazlaşır
#maxVal = piksel değerinin eşik değerinden büyük olması durumunda verilecek değeri temsil eden değişken.

#blockSize çift sayı olamaz!!!!

#cv2.adaptiveThreshold(source, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C,
                                #cv2.THRESH_BINARY, blockSize, C)

thresh1 = cv2.adaptiveThreshold(image1, 1000, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 51, 2)


thresh2 = cv2.adaptiveThreshold(image1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 51, 5)

r1 = cv2.resize(thresh1,(600,600))
r2 = cv2.resize(thresh2,(600,600))

cv2.imshow('Adaptive Mean', r1)
cv2.imshow('Adaptive Gaussian', r2)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
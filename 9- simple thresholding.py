import cv2 #cv2 cv olarak import edildi

image1 = cv2.imread("C:\\Users\\berka\\OneDrive\\Desktop\\cr7.jpg") #resmin kaynağını söyledik

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) #resmi griye çevirdik (zorunlu)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)

ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)

ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)

ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold', thresh1)

cv2.imshow('Binary Threshold Inverted', thresh2)

cv2.imshow('Truncated Threshold', thresh3)

cv2.imshow('Set to 0', thresh4)

cv2.imshow('Set to 0 Inverted', thresh5)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

#THRESH_BINARY
#eğer piksel değeri thresh'ten büyükse 255, değilse 0 olarak ayarlanır

#THRESH_TRUNC
#eğer piksel değeri threst'ten büyükse değer thresh ile aynı olur değilse pikselin değeri değişmez


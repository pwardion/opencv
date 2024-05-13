#image resizing

import cv2 as cv #cv2 cv olarak import edildi

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\uzuminyo.jpeg") #okunacak resmin kaynağı belirtildi

width = 100 #resmin ayarlanacak genişliği belirtildi

height = 100 #resmin ayarlanacak yüksekliği belirtildi

dims = (width,height) #genişlik ve yükseklik dims olarak tek değişkene atandı

img = cv.resize(img,dims) #resim resize edildi

cv.imshow('title', img) #resim gösterildi

cv.waitKey() #herhangi bir tuşa basana kadar resmin görüntülenmesi sağlandı

cv.destroyAllWindows() #herhangi bir tuşa basınca tüm pencerelerin kapanması söylendi
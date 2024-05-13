#image reading and displaying on opencv-python

import cv2 as cv #cv2 cv olarak import edildi

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\uzuminyo.jpeg") #resmin kaynağı belirtildi ve resim okutuldu

cv.imshow('title', img) #resim title başlığıyla gösterildi

cv.waitKey() #herhangi bir tuşa basılana kadar resmin kapatılmaması söylendi

cv.destroyAllWindows() #tuşa basılınca tüm pencerelerin kapanması söylendi

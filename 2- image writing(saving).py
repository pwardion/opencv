import cv2 as cv #cv2 cv olarak import edildi

import os #os modülü import edildi

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\uzuminyo.jpeg") #resmin kaynağı söylendi

os.chdir("C:\\Users\\berka\\OneDrive\\Desktop\\other") #resmin kaydedileceği yer söylendi

cv.imwrite('kaydedilen.jpg', img) #resim kaydedilen.jpg olarak kaydedildi



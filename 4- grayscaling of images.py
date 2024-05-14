#grayscaling images

import cv2 as cv #cv2 cv olarak import edildi

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\bayrak.jpg") #resmin kaynağı belirtildi

#method 1
"""
gray_image = cv.cvtColor(img, cv2.COLOR_BGR2GRAY) #resmin renk uzayının bgrden graya çevrileceği söylendi

cv2.imshow('GRAY', gray_image) #gri resim gösterildi
cv.waitKey() #herhangi bir tuşa basana kadar resmin açık kalması sağlandı
cv.destroyAllWindows() #herhangi bir tuşa basılınca bütün pencerelerin kapanması gerektiği söylendi
"""
#method 2

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\bayrak.jpg", 2) #sondaki flag anlamına gelen 2 resmi
                                                                                # gri yapar


cv.imshow('2', img) #resim gösterildi
cv.waitKey()
cv.destroyAllWindows()

"""
1: IMREAD_COLOR
If the flag is set to this value, the loaded image will be converted to a 3-channel BGR (Blue Green Red) color image.

2: IMREAD_GRAYSCALE
If the flag is set to this value, the loaded image will be converted to a single-channel grayscale image.

3: IMREAD_LOAD_GDAL
If the flag is set to this value, you can load the image using the gdal driver.

4: IMREAD_ANYCOLOR
If the flag is set to this value, the image is read in any possible color format.

5: IMREAD_REDUCED_COLOR_2
IMREAD_REDUCED_COLOR_4
IMREAD_REDUCED_COLOR_8
If the flag is set to this value, the image is read as three-channel BGR, and the size of the image is reduced to ½, 
¼th or ⅛th of the original size of the image with respect to the field used.

6: IMREAD_REDUCED_GRAYSCALE_2
IMREAD_REDUCED_GRAYSCALE_4
IMREAD_REDUCED_GRAYSCALE_8
If the flag is set to this value, the image is read as a single-channel grayscale image, and the size of the 
image is reduced to ½, ¼th or ⅛th of the original size of the image with respect to the field used.

7: IMREAD_UNCHANGED
If the flag is set to this value, the loaded image is returned as it is.
"""

#method 3 (avg method, most efficient)
"""
ÖZET OLARAK HER BİR PİKSELİN ORTALAMA BGR DEĞERLERİ ALINDI 
(row, col) = img.shape[0:2]

for i in range(row)

    for j in range(col):
        
        img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
"""

import cv2 as cv

resim = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\opencv\\aq7.webp",0)

temp = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\opencv\\temp.jpg",0)


res=cv.matchTemplate(resim, temp, cv.TM_SQDIFF_NORMED)

"""
METODLAR
cv.TM_SQDIFF:

Karesel fark yöntemi.
Eşleştirme skoru, ana görüntü ile şablon arasındaki piksel değerlerinin farklarının karelerinin toplamıdır.
Düşük skorlar daha iyi eşleşmeyi gösterir.
cv.TM_SQDIFF_NORMED:

Normalleştirilmiş karesel fark yöntemi.
Eşleştirme skoru, karesel farkın ana görüntü ve şablonun normlarına bölünmesiyle elde edilir.
0'a yakın skorlar daha iyi eşleşmeyi gösterir.
cv.TM_CCORR:

Çapraz korelasyon yöntemi.
Eşleştirme skoru, ana görüntü ile şablon arasındaki piksel değerlerinin korelasyon katsayısıdır.
Yüksek skorlar daha iyi eşleşmeyi gösterir.
cv.TM_CCORR_NORMED:

Normalleştirilmiş çapraz korelasyon yöntemi.
Eşleştirme skoru, çapraz korelasyonun ana görüntü ve şablonun normlarına bölünmesiyle elde edilir.
1'e yakın skorlar daha iyi eşleşmeyi gösterir.
cv.TM_CCOEFF:

Korelasyon katsayısı yöntemi.
Eşleştirme skoru, ana görüntü ile şablon arasındaki piksel değerlerinin çapraz korelasyon katsayısının normalleştirilmiş haliyle elde edilir.
Yüksek skorlar daha iyi eşleşmeyi gösterir.
cv.TM_CCOEFF_NORMED:

Normalleştirilmiş korelasyon katsayısı yöntemi.
Eşleştirme skoru, korelasyon katsayısının ana görüntü ve şablonun normlarına bölünmesiyle elde edilir.
1'e yakın skorlar daha iyi eşleşmeyi gösterir."""

h,w = temp.shape[::]

minval, maxval,minloc,maxloc = cv.minMaxLoc(res) #benzerlik haritasının minimum ve maksimum değerlerini
                                                 #(minval ve maxval) ve bu değerlerin konumlarını (minloc ve maxloc) buluyoruz

tl = minloc

br = (tl[0]+w, tl[1]+h)

cv.rectangle(resim, tl,br,color=(0,255,0), thickness=3)

cv.imshow("asd", resim)

cv.waitKey()
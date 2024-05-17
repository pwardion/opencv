#corner detection

import numpy as np
import cv2

img = cv2.imread("C:\\Users\\berka\\OneDrive\\Desktop\\corner1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 27, 0.1, 10)
#SYNTAX: cv.goodFeaturesToTrack(source, maxCorners, qualityLevel, minDistance)
#maxCorners: Algılanacak maksimum köşe sayısı.
#qualityLevel: Algılanan köşelerin kalitesini belirlemek için kullanılan bir eşik değeri. Daha yüksek kalite seviyeleri,
             #daha yüksek kaliteli köşeleri döndürür.

#minDistance: İki köşe arasındaki minimum uzaklık. Bu değerden daha yakın olan köşeler dikkate alınmaz.

corners = np.int0(corners)
#köşelerin koordinatlarını 0 boyutlu diziye çevirdik çevirdik

# we iterate through each corner,
# making a circle at each point that we think is a corner.

for i in corners:
    x, y = i.ravel() #ravel: çok boyutlu bir diziyi tek boyutlu bir diziye dönüştürmek için kullanılır.
    cv2.circle(img, (x, y), 3, 255, -1) #çember çizdirdik

cv2.imshow('title', img)
cv2.waitKey()
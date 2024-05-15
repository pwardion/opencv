import cv2 as cv #cv2 cv olarak import edildi

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\cr7.jpg") #resmin kaynağı söylendi

cv.imshow('title', img) #resmin normal hali gösterildi

#134 20 87 108 #roi ile alınan sırasıyla x,y,w,h değerleri

x = 134
y = 20
w = 87
h = 108

output = img.copy() #output adında resmin bir kopyası oluşturuldu

cv.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2) #dikdörtgen çizdirildi
                                                         #(x,y) starting point(sağ alt)
                                                         #(x+w,y+h) ending point (sol üst)
                                                         #0,255,0 çizilecek dikdörtgenin rengi (BGR)
                                                         #en sondaki 2 dikdörtgenin kalınlığı

cv.imshow('rect', output) #dikdörtgen çizilmiş resim rect başlığıyla gösterildi

cv.waitKey() #herhangi bir tuşa basana kadar beklenmesi söylendi

cv.destroyAllWindows() #herhangi bir tuşa basıldığında tüm pencerelerin kapanması söylendi
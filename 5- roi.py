#ROI (Region of Interest)
#roi fonksiyonu ile ilgilendiğimiz alanın piksel numaralarını öğreniyoruz


import cv2 as cv

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\cr7.jpg")

"""
x,y,w,h = cv.selectROI(img)
print(x,y,w,h)
selected = img[y:y+w,x,x+h]
selected = img[startY:endY,startX,endX]
"""


selected = img[20:128,129:228] #resmin hangi piksellerini almak istediğimizi söyledik (önce x sonra y)

cv.imshow('s', selected)

cv.waitKey()

cv.destroyAllWindows()

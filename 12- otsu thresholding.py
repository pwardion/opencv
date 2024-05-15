import cv2

image1 = cv2.imread("C:\\Users\\berka\\OneDrive\\Desktop\\cr7.jpg",0)

ret, thresh1 = cv2.threshold(image1, 120, 255, cv2.THRESH_BINARY +
                             cv2.THRESH_OTSU)
#thresh1 = cv2.threshold(source, thresh, maxval, cv2.THRESH_BINARY +
                             #cv2.THRESH_OTSU)
                             
cv2.imshow('Otsu Threshold', thresh1)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
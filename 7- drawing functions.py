import cv2 as cv
import numpy as np

img = np.zeros((300,400),np.uint8)

#drawing line
img1 = img.copy()
img1 = cv.line(img1,(0,0),(400,300),(255,255,255),2)
#SYNTAX: cv.line(image, start_point, end_point, color, thickness)

#drawing rectangle
img2 = img.copy()
img2 = cv.rectangle(img2,(10,10),(50,50), (255,255,255), 2) #thickness == -1 dikdörtgenin içi dolu olur
#SYNTAX: cv.rectangle(image, start_point (TOP LEFT), end_point (BOTTOM RIGHT), color, thickness)

#drawing circle
img3 = img.copy()
img3 = cv.circle(img3, (200,150),100,(255,255,255),2) #thickness == -1 çemberin içi dolu olur
#SYNTAX: cv.circle(image, center_coordinates, radius, color, thickness)

#putting text on an image
img4 = img.copy()
img4 = cv.putText(img4,'Merhaba', (200,150),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
#SYNTAX: image = cv2.putText(image, 'OpenCV', org, font,
                   #fontScale, color, thickness, cv2.LINE_AA) #org: textin sol alt köşe koordinatları


cv.imshow('line',img1)
cv.imshow('rectangle',img2)
cv.imshow('circle',img3)
cv.imshow('text', img4)


cv.waitKey()
cv.destroyAllWindows()
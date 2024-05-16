#bitwise operations
#AND: A bitwise AND is true if and only if both pixels are greater than zero.
#OR: A bitwise OR is true if either of the two pixels is greater than zero.
#XOR: A bitwise XOR is true if and only if one of the two pixels is greater than zero, but not both.
#NOT: A bitwise NOT inverts the “on” and “off” pixels in an image.


import cv2 as cv

img1 = cv.imread("C:\\Users\\berka\\PycharmProjects\\opencvv\\input1.png")
img2 = cv.imread("C:\\Users\\berka\\PycharmProjects\\opencvv\\input2.png")


#bitwise_and
bitwiseand = cv.bitwise_and(img2,img1)

#bitwise_or
bitwiseor = cv.bitwise_or(img1,img2)

#bitwise_xor
bitwisexor = cv.bitwise_xor(img1,img2)

#bitwise_not
bitwisenot = cv.bitwise_not(img1,img2)

cv.imshow('AND', bitwiseand)
cv.imshow('OR', bitwiseor)
cv.imshow('XOR', bitwisexor)
cv.imshow('NOT', bitwisenot)
cv.waitKey()
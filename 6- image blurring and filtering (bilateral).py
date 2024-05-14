#blurring images

#as the size of the kernel increases, so will the amount in which the image is blurred.
#the larger your smoothing kernel is, the more blurred your image will look.
import cv2 as cv

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\cr7.jpg")

#avg blur
#An average filter does exactly what you think it might do — takes an area of pixels surrounding a central pixel,
#averages all these pixels together, and replaces the central pixel with the average.
averageblurred = cv.blur(img,(3,3))
cv.imshow('average blur', averageblurred)

#gaussian blur
#pixel intensity of the neighborhood
gaussianblurred = cv.GaussianBlur(img,(3,3),0) #sigmaX = 0 olması hem sigmaY'nin de 0 olması hem de bu değerlerin
                                                    #bilgisayar tarafından hesaplanmasını sağlar
cv.imshow('gaussian blur', gaussianblurred)

#median blurring
# instead of replacing the central pixel with the average of the neighborhood, we instead replace the central
#pixel with the median of the neighborhood.
medianblur = cv.medianBlur(img,3)
cv.imshow('median blur', medianblur)


#bilateral filtering
#sigmaColor: Standard deviation that controls the influence of pixels with different intensity values
#sigmaSpace: Standard deviation that controls the influence of distant pixels
bilateralfilter = cv.bilateralFilter(img,70,70,350)
cv.imshow('bilateral', bilateralfilter)

cv.waitKey()

cv.destroyAllWindows()

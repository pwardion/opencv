import cv2 as cv

img = cv.imread("C:\\Users\\berka\\OneDrive\\Desktop\\asdd.jpg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret, threshold = cv.threshold(gray,230,255, cv.THRESH_BINARY)

cv.imshow( "th", threshold)

countours,hierarchy=cv.findContours(threshold, mode=cv.RETR_CCOMP, method=cv.CHAIN_APPROX_SIMPLE)

#"mode" alınacak kontur türünü, "method" ise bir kontur içinde hangi noktaların saklanacağını belirtir.
#hierarchy: konturlar arasındaki ilişkileri tanımlayan bir yapıdır. Örneğin, bir konturun iç içe geçmiş bir kontur olup
#olmadığını veya başka bir konturun bir delik olduğunu gösteren bilgiler içerir.

#cv.CHAIN_APPROX_NONE: Konturun tüm noktalarını saklar.
#cv.CHAIN_APPROX_SIMPLE: Konturun yalnızca uç noktalarını saklar ve aradaki tüm noktaları atar.

cv.drawContours(img, contours=countours, contourIdx=-1 , color=(0,255,0), thickness=4, lineType=cv.LINE_AA)
#contours: findContours() fonksiyonundan elde edilen konturları gösterir.
#contourIdx: Elde edilen konturlardaki kontur noktalarının piksel koordinatları listelenir.
#Bu argümanı kullanarak, bu listeden hangi kontur noktasını çizmek istediğinizi belirtebilirsiniz.
#Negatif bir değer sağlamak, tüm kontur noktalarını çizer.

#cv.RETR_EXTERNAL: Yalnızca en dıştaki konturları alır. Diğer konturlar iç içe geçmiş olsa bile, yalnızca en dıştaki konturlar listelenir.

#cv.RETR_LIST: Tüm konturları hiyerarşi yapısını dikkate almadan alır. Bu, hiyerarşi bilgisi gereksiz olduğunda kullanılır.

#cv.RETR_CCOMP: Tüm konturları iki seviyeli hiyerarşi olarak alır. İçteki konturlar, dıştaki konturların delikleridir.
#Bu mod, nesnelerin içerisindeki diğer nesnelerin konturlarını da almak için kullanılır.

#cv.RETR_TREE: Tüm konturları tam bir hiyerarşi ağacı olarak alır. Örneğin, iç içe geçmiş konturların ilişkisini tam olarak gösterir.

cv.imshow("resim", img)

cv.waitKey()
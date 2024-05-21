import cv2 as cv

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280) #görüntünün genişliği ayarlandı

cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720) #görüntünün yüksekliği ayarlarndı



while True:

    _, frame = cap.read()

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    height, width,_ = frame.shape

    y = int(height/2)

    x = int(width/2)

    cpbgr = frame[y, x]

    centerpixel = hsv[y,x] #belirtilen koordinatlardaki pikselin HSV renk değerleri elde edilir.


    hue_value = centerpixel[0] #centerpixel'den alınan değerler arasından sadece ton bileşenini (hue) seçer.

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"


    b, g, r = int(cpbgr[0]), int(cpbgr[1]), int(cpbgr[2]) #her bir renk bileşenini ondalık sayıdan tamsayıya dönüştürerek, b, g ve r değişkenlerine atar.

    cv.circle(frame, (x,y), 5,color=(0,255,0), thickness=3)

    cv.putText(frame,color,(500,100),fontFace=1,fontScale=5,color=(b,g,r), thickness=3)

    cv.imshow("fr", frame)




    cv.waitKey(1)
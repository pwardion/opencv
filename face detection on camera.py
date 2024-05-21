import cv2 as cv

cap = cv.VideoCapture(0)


source = r"C:\\Users\\berka\\OneDrive\\Desktop\\haarcascade_frontalface_default.xml"

cascade = cv.CascadeClassifier(source) #CascadeClassifier sınıfından bir nesne oluşturur



while cap.isOpened():
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray, 1.2, 3) #cascade nesnesi üzerinde detectMultiScale
                                                                         #yöntemini çağırarak nesne tespiti işlemini gerçekleştirir.


    for (x,y,w,h) in faces:

        cv.rectangle(frame, (x,y),(x+w,y+h), color=(0,255,0), thickness=3)

        cv.imshow("asd", frame)

        cv.waitKey(1)


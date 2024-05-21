import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)


mphands = mp.solutions.hands #mediapipe kütüphanesinin el tespit modelini yükler.

"""mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5)
    """
hands = mphands.Hands(max_num_hands=1) #el tespit modelini başlatır.

mpdraw = mp.solutions.drawing_utils #mediapipe'nin çizim yardımcı fonksiyonlarını yükle

while cap.isOpened():
    _, frame = cap.read()
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    key = cv.waitKey(1)
    result = hands.process(rgb) #el tespit modelini kullanarak, verilen görüntüdeki elleri tespit eder.
                                #giriş olarak RGB formatındaki görüntüyü alır.

    if result.multi_hand_landmarks: #eğer bir el tespit edilmişse bu bloğa girilir.

        for handlms in result.multi_hand_landmarks: #her tespit edilen el için döngü başlatılır.

            for id,lm in enumerate(handlms.landmark):

                h,w,c = frame.shape

                cx,cy = int(lm.x*w), int(lm.y*h)

                print(id, cx,cy)

                if id == 0:
                    cv.circle(frame, (cx,cy), 10, color=(0,255,0), thickness=-1)

                mpdraw.draw_landmarks(frame, handlms, mphands.HAND_CONNECTIONS)

            #mp.solutions.drawing_utils.draw_landmarks(image, landmark_list, connections=None,landmark_drawing_spec=None, connection_drawing_spec=None)
            
             #Mediapipe çizim yardımcı fonksiyonunu
                                                                            #kullanarak, tespit edilen elin etrafına
                                                                            #çizgiler çizer. Bu çizgiler eldeki çeşitli noktaları birleştirir.

    cv.imshow("frame", frame)
    if key == ord("q"):
        break
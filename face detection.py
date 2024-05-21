import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

face = mp.solutions.face_detection

det = face.FaceDetection(min_detection_confidence=0.5)

drawinyo = mp.solutions.drawing_utils


while cap.isOpened():
    _, frame = cap.read()
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    res= det.process(rgb)

    for df  in res.detections:
        drawinyo.draw_detection(frame,df)


    cv.imshow("frame", frame)
    cv.waitKey(1)



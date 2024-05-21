import cv2 as cv

import pandas as pd

names = ['color', 'color_names', 'hex' , 'R','G','B']

data = pd.read_csv("C:\\Users\\berka\\OneDrive\\Desktop\\opencv\\dataset.csv", names=names)

#print(data.head())

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)

cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)



def kontrol(R,G,B):
    min = 150
    for i in range(len(data)):
        d = abs(R - int(data.loc[i, "R"])) + abs(G - int(data.loc[i, "G"])) + abs(B - int(data.loc[i, "B"]))
        if d<= min:
            d= min
            cname = data.loc[i, "color_names"]
    return cname

while cap.isOpened():
    _, frame = cap.read()

    h,w,_ = frame.shape
    #print(h,w)
    y = int(h/2)

    x = int(w/2)

    merkeznokta = frame[y,x]
    print(merkeznokta)
    b,g,r = merkeznokta[0], merkeznokta[1], merkeznokta[2]

    text = kontrol(r,g,b) , "R: ",r , "G: ",g, "B: ",b
    print(text)

    cv.circle(frame,(x,y), 10, color=(0,255,0),thickness=3)

    cv.imshow("frame", frame)

    cv.waitKey(1)

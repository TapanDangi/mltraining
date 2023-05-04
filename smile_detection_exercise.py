import cv2
import numpy as np
from time import sleep

vid = cv2.VideoCapture(0)
notCaptured = True

fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
sd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')

while True:
    flag, img = vid.read()

    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(
            img_gray,
            scaleFactor = 1.1,
            minNeighbors = 10,
            minSize = (50,50)
        )

        np.random.seed(80)
        colors = np.random.randint(0,255,(len(faces),3)).tolist()

        i = 0
        for x,y,w,h in faces:
            face = img_gray[y:y+h, x:x+w].copy()
            
            smiles = sd.detectMultiScale(
                face,
                scaleFactor = 1.1,
                minNeighbors = 10,
                minSize = (10,10)
            )

            cv2.rectangle(img, pt1 = (int(x+3*w/10),int(y+3*h/4)), pt2 = (int(x+7*w/10),int(y+6*h/7)), color = colors[i], thickness = 2)
            i += 1

            if len(smiles) == 1:
                cv2.imwrite('myselfie.png', img)
                notCaptured = False
                break

        cv2.imshow('Preview', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break
    sleep(0.1)
cv2.destroyAllWindows()
vid.release()
del vid
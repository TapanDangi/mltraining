import cv2
from time import sleep
import numpy as np

fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
sd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')

vid = cv2.VideoCapture(0)
notCaptured = True

while notCaptured:
    flag,img = vid.read()

    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = fd.detectMultiScale(
            img_gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (50,50)
        )

        np.random.seed(80)
        colors = np.random.randint(0,255,(len(faces),3)).tolist()

        i=0
        for x,y,w,h in faces:
            face = img_gray[y:y+h, x:x+w].copy()

            smiles = sd.detectMultiScale(
            face,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (5,5)
            )

            if len(smiles) == 1:
                cv2.imwrite('selfie.png', img)
                notCaptured = False
                break

            cv2.rectangle(img, pt1 = (x,y), pt2 = (x+w, y+h), color = colors[i], thickness = 4)
            i += 1

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
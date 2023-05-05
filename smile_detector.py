import cv2
from time import sleep
import numpy as np

fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
sd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')

vid = cv2.VideoCapture(0)
notCaptured = True
seq = 0
while notCaptured:
    flag,img = vid.read()

    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = fd.detectMultiScale(
            img_gray,   #face is detected inside of an image
            scaleFactor = 3,
            minNeighbors = 5,
            minSize = (50,50)
        )

        np.random.seed(80)
        colors = np.random.randint(0,255,(len(faces),3)).tolist()

        i=0
        for x,y,w,h in faces:
            face = img_gray[y:y+h, x:x+w].copy()    #coordinates of a single face is taken by cropping

            smiles = sd.detectMultiScale(
            face,   #smile is detected inside of a face
            scaleFactor = 3,
            minNeighbors = 5,
            minSize = (5,5)
            )

            if len(smiles) == 1:
                seq += 1
                if seq == 10:   #if ten frames are continually captured, then image is taken, otherwise seq is reset
                    cv2.imwrite('selfie.png', img)
                    notCaptured = False
                    break
            else:
                seq = 0

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
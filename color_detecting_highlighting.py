import cv2
import skimage
import plotly
import plotly.express as px
from time import sleep

vid = cv2.VideoCapture(0)
while True:
    flag, img = vid.read()
    if(flag):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_p = cv2.subtract(img[:,:,-1], cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))    #To subtract blue plane and grayscale image to get blue color
        th, img_p2 = cv2.threshold(img_p, 60, 255, cv2.THRESH_BINARY)  #Implement thresholding

        img_p3 = skimage.morphology.remove_small_objects(img_p2.astype(bool), 10)   #To remove noise from image
        img_p4 = cv2.dilate(
            img_p3.astype('uint8'),
            cv2.getStructuringElement(
                cv2.MORPH_ELLIPSE,
                (10,10)
            )
        ).astype(bool)  #To draw circle around the badge
        img_p5 = skimage.morphology.remove_small_holes(img_p4, 180) #To remove holes from image

        rp = skimage.measure.regionprops(skimage.measure.label(img_p5))
        img_preview = img.copy()

        if len(rp) > 0:
            (y1,x1,y2,x2) = rp[0].bbox
            cv2.rectangle(
                img_preview,
                pt1 = (x1,y1), pt2 = (x2,y2),
                color = (255,255,0),
                thickness = 5
            )
        
        cv2.imshow('Preview', img_preview[:,:,::-1])
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break
    sleep(0.1)
cv2.destroyAllWindows()
vid.release()
del vid
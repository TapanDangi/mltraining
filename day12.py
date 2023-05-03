import cv2
import numpy as np

from time import sleep

# To import face descriptor files
fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

# To show a series of images as a live feed
vid = cv2.VideoCapture(0)

while True:
    flag, img = vid.read()  # Continuously reads images from camera
    if flag:
        # Processing Code
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Converts BGR image to Grayscale Image
        faces = fd.detectMultiScale(    # Used to detect faces
            img_gray,   # Faces are better detected in grayscale image
            scaleFactor = 1.1,  #scales the image by this factor if not able to detect
            minNeighbors = 5,  #Minimum number of similar items to consider it an image
            minSize = (50,50)  # w and h in x,y,w,h should be at least of this size to consider it an image
        )

        np.random.seed(78)
        colors = np.random.randint(0,255,(len(faces),3)).tolist()   # Generates a random color
        i = 0
        
        for x,y,w,h in faces:   # Loop for multiple faces
            cv2.rectangle(img, pt1 = (x,y), pt2 = (x+w, y+h), color = colors[i], thickness = 4)    # Rectangle is drawn over the image
            i += 1
        
        cv2.imshow('Preview', img)
        key = cv2.waitKey(1)    # waits for 1 key to be pressed
        if key == ord('q'): # executed when q is pressed on keyboard
            break
    else:
        break
    sleep(0.1)
cv2.destroyAllWindows() # Closes all windows after stopping the camera
vid.release()   # Camera is turned off
del vid
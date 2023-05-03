import cv2
import matplotlib.pyplot as plt

# To show a series of images as a live feed
vid = cv2.VideoCapture(0)
while True:
    flag, img = vid.read()  # Continuously reads images from camera
    if flag:
        # Processing Code
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Converts BGR image to Grayscale Image
        th, img_bw = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)   # Converts grayscale image to Black and White

        x,y,w,h = (240,320,100,100) # defines the dimensions of cropped image
        img_cropped = img[y: y+h, x: x+w, :]

        cv2.rectangle(img, pt1 = (x,y), pt2 = (x+w, y+h), color = (0,0,255), thickness = 4)    # Rectangle is drawn over the image

        cv2.imshow('Preview1', img)
        cv2.imshow('Preview2', img_gray)
        cv2.imshow('Preview3', img_bw)
        cv2.imshow('Preview4', img_cropped)

        key = cv2.waitKey(1)    # waits for 1 key to be pressed
        if key == ord('q'): # executed when q is pressed on keyboard
            break
    else:
        break
cv2.destroyAllWindows() # Closes all windows after stopping the camera
vid.release()   # Camera is turned off
del vid
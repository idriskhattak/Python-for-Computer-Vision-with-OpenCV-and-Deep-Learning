import cv2
import os

#image_path = os.path.join('..','..','DATA','00-puppy.jpg')

# cv2 was not reading image directly causing an error so i passed the whole image file now it's working

image = cv2.imread('E:/Python-for-Computer-Vision-with-OpenCV-and-Deep-Learning/DATA/00-puppy.jpg')

while True:

    cv2.imshow('Puppy',image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows
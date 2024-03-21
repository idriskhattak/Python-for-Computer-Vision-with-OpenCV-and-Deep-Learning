import cv2
import os

image_path = os.path.join('..','..','DATA','00-puppy.jpg')

image = cv2.imread(image_path)

while True:

    cv2.imshow('Puppy',image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows
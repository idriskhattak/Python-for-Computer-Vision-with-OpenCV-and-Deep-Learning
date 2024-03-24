import numpy as np
import cv2

# Variables
# When left button is clicked drawing will set to be true
drawing = False
ix = -1
iy = -1

# Function
def drawing_rec(event,x,y,flags,param):

    global drawing,ix,iy

    if event == cv2.EVENT_LBUTTONDOWN:
        # When you click DOWN with left mouse button drawing is set to True
        drawing = True
        # Then we take note of where that mouse was located
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        # Now the mouse is moving

        if drawing == True:
            # If drawing is True, it means you've already clicked on the left mouse button
            # We draw a rectangle from the previous position to the x,y where the mouse is
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),1)

    elif event == cv2.EVENT_LBUTTONUP:
        # Once you lift the mouse button, drawing is False
        drawing = False
        # we complete the rectangle.
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),1)


# This names the window so we can reference it
cv2.namedWindow(winname='my_image')

# Connects the mouse button to our callback function
cv2.setMouseCallback('my_image',drawing_rec)

# Creating an image
img = np.zeros((500,500,3),dtype=np.uint8)

while True:

    cv2.imshow('my_image',img)
    if cv2.waitKey(1) & 0xFF == 27:   # ---> When escape key pressed the loop will break
        break


# Once script is done, its usually good practice to call this line
# It closes all windows (just in case you have multiple windows called)
cv2.destroyAllWindows()
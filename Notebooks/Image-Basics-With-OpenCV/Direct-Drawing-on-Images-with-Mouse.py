import cv2
import numpy as np

# Creating a blank image using numpy
img = np.zeros((500,500,3),dtype=np.uint8)

# Creating a function that will draw circles image where left button is clicked
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,0,0),-1) # ---> Blue circle will be created when left button is pressed
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,0,255),-1) # ---> Red circle will be created when right button is pressed



# This method will connect draw_circle function with callbacks
# This line creates a named window with the title 'my_image'.
# A named window is a window that can be referenced later for displaying images or capturing mouse events.
cv2.namedWindow(winname='my_image')

# This line sets a mouse callback function for the named window 'my_image'.
# Whenever a mouse event occurs in the window 'my_image', the function draw_circle will be called with the appropriate parameters (event, x, y, flags, param).
# So, whenever the user clicks the left mouse button in the window 'my_image', the function draw_circle will be called to draw a circle at the clicked position on the image.
cv2.setMouseCallback('my_image',draw_circle)

while True:
    cv2.imshow('my_image',img)

    if cv2.waitKey(30) & 0xFF == 27: # ---> 0xFF == 27  refers to escape key
        break

cv2.destroyAllWindows()



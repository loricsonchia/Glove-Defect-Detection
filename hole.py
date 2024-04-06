import cv2
import numpy as np

# Load the image
image = cv2.imread('IMG20220420171946_jpg.rf.e6e9937eb1ad1346f818a7abd574dd3c.jpg')
image = cv2.imread('IMG20220420171946_jpg.rf.98a8654da80836562634c2edab22fc89.jpg')
#image = cv2.imread('close-up-hand-wearing-torn-medical-gloves-torn-rubber-gloves-white-background_335640-3477.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarize image
ret, th = cv2.threshold(gray, 113, 255, cv2.THRESH_BINARY)

# Reduce noise
blur = cv2.medianBlur(th, 9)

# Eliminate small hole/ noise
opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, np.ones((7, 7)))

# Find hole with contour
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

holeCounter = 0
for contour in contours:
    if (cv2.contourArea(contour) < 8000 and cv2.contourArea(contour) > 815):
        # draw out all the contour
        perimeter = cv2.arcLength(contour, True)
        vertices = cv2.approxPolyDP(contour, perimeter * 0.02, True)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Put text on top of the rectangle
        cv2.putText(image, 'Hole', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        holeCounter = holeCounter + 1

# Put text to show number of hole detected
cv2.putText(image, 'Hole detected: ' + str(holeCounter), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
            cv2.LINE_AA)

# show result
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Opening", opening)
cv2.imshow("result", image)
cv2.waitKey(0)
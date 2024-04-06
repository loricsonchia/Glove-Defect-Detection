import cv2
import numpy as np

# Load the image
image = cv2.imread('discolouration_black.png')

fullHLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS_FULL)
H, L, S = cv2.split(fullHLS)

lower_saturation = 240
upper_saturation = 250
saturation_mask = cv2.inRange(H, lower_saturation, upper_saturation)

# Apply morphological operations to enhance areas of low saturation
kernel = np.ones((3, 3), np.uint8)
eroded = cv2.erode(image, kernel)

# Find Contours
contours, hierarchy = cv2.findContours(saturation_mask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(eroded, contours, -1, (0, 255, 0), 2)

# Detect the defect within the glove
internal_cnt = [contours[i] for i in range(len(contours)) if hierarchy[0][i][3] >= 0]

cv2.imshow("Original Image", image)
cv2.imshow("Detected Discolouration", eroded)
cv2.imshow("Full HLS", fullHLS)
# cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
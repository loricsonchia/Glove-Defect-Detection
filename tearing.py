import cv2
import numpy as np

# Load the image
image = cv2.imread('IMG20220420171356_jpg.rf.4ce93fccf13a1021f6299a1bb55d6d81.jpg')
image = cv2.imread('IMG20220420171943_jpg.rf.7144f2ab6feeafecadc44fcdc7e9634c.jpg')
cv2.imshow('Image', image)


hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Mask for detecting glove
# lower = np.array([85, 111, 122])
# upper = np.array([103, 255, 255])
lower = np.array([45, 45, 45])
upper = np.array([255, 255, 255])
mask = cv2.inRange(hsv_frame, lower, upper)

# apply median filtering
blurred_frame = cv2.medianBlur(mask, 9)

# Define the structuring element (kernel) for erosion
kernel = np.ones((15, 15), np.uint8)

# Perform erosion
eroded_frame = cv2.erode(blurred_frame, kernel)

# Find Contours
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(eroded_frame, contours, -1, (0, 255, 0), 2)

# Detect the defect within the glove
internal_cnt = [contours[i] for i in range(len(contours)) if hierarchy[0][i][3] >= 0]

if len(contours) > 0:
    blue_area = max(contours, key=cv2.contourArea)
    (xg, yg, wg, hg) = cv2.boundingRect(blue_area)

    # Find defect
    if len(internal_cnt) > 0:
        for i in internal_cnt:
            # Check defect size
            area = cv2.contourArea(i)
            print(area)
            if area > 40:
                xd, yd, wd, hd = cv2.boundingRect(i)
                # Draw rectangle for defect
                cv2.rectangle(image, (xd, yd), (xd + wd, yd + hd), (0, 0, 255), 2)

                # Label the defect
                if area > 400:
                    # Defect Type: Tearing
                    image = cv2.putText(image, 'Tearing Found', (xd, yd - 5), cv2.FONT_HERSHEY_SIMPLEX,
                                            0.5, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("HSV", hsv_frame)
cv2.imshow("Masking Effect", mask)
cv2.imshow("Eroded", eroded_frame)
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
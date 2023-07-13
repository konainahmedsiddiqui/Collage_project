import cv2
import numpy as np

# Load images
img1 = cv2.imread('C:/Users/Dell/HACKERSPACE/Frame_proj/Examples5/pexels-photo-1066801.jpeg')
img2 = cv2.imread('C:/Users/Dell/HACKERSPACE/Frame_proj/Examples5/istockphoto-1339226443-612x612.jpg')
img3 = cv2.imread('C:/Users/Dell/HACKERSPACE/Frame_proj/Examples5/pexels-photo-4672438.jpeg')
img4 = cv2.imread('C:/Users/Dell/HACKERSPACE/Frame_proj/Examples5/pexels-photo-9584933.jpeg')

# Resize images
img1 = cv2.resize(img1, (200, 200))
img2 = cv2.resize(img2, (200, 200))
img3 = cv2.resize(img3, (200, 200))
img4 = cv2.resize(img4, (200, 200))

# Create circle shape
height, width = 600, 600
circle = np.zeros((height, width, 3), np.uint8)
center = (height//2, width//2)
radius = height//3
color = (255, 255, 255)
cv2.circle(circle, center, radius, color, -1)

# Mask for circle shape
gray_circle = cv2.cvtColor(circle, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_circle, 1, 255, cv2.THRESH_BINARY)

# Place images within circle shape
result = cv2.bitwise_and(circle, circle, mask=mask)
result = cv2.addWeighted(result, 1, img1, 1, 0)
result = cv2.addWeighted(result, 1, img2, 1, 0)
result = cv2.addWeighted(result, 1, img3, 1, 0)
result = cv2.addWeighted(result, 1, img4, 1, 0)

# Display and save final collage
cv2.imshow('Photo Collage', result)
# cv2.imwrite('circle_collage.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

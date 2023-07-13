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

# Create polygon shape
height, width = 200, 200
polygon = np.zeros((height, width, 3), np.uint8)
pts = np.array([[100,100], [500,200], [450,450], [200,500]], np.int32)
cv2.fillPoly(polygon, [pts], (255, 255, 255))
cv2.polylines(polygon, [pts], True, (0, 0, 0), 50)

# Mask for polygon shape
gray_polygon = cv2.cvtColor(polygon, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_polygon, 1, 255, cv2.THRESH_BINARY)

# Place images within polygon shape
result = cv2.bitwise_and(polygon, polygon, mask=mask)
result = cv2.addWeighted(result, 1, img1, 1, 0)
result = cv2.addWeighted(result, 1, img2, 1, 0)
result = cv2.addWeighted(result, 1, img3, 1, 0)
result = cv2.addWeighted(result, 1, img4, 1, 0)

# Display and save final collage
cv2.imshow('Photo Collage', result)
# cv2.imwrite('irregular_collage.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

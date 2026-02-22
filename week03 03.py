import cv2

# Load the image
image = cv2.imread(r'C:\Users\USER\Pictures\download.jpg')
height, width = image.shape[:2]

# Define center, angle, and scale
center = (width // 2, height // 2)
angle = 90  # Counter-clockwise
scale = 1.0

# Get rotation matrix and apply transformation
matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(image, matrix, (width, height))

# Save and display
cv2.imwrite('rotated.jpg', rotated)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()



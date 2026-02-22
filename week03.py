import cv2

# Load image
img = cv2.imread(r'C:\Users\USER\Pictures\download.jpg')

# Option 1: Resize to exact dimensions (Width, Height)
new_dimensions = (500, 300)
resized_exact = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

# Option 2: Resize by scaling factor (e.g., 50% of original size)
# To maintain aspect ratio, set fx and fy to the same value
resized_scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display results
cv2.imshow('Resized Exact', resized_exact)
cv2.imshow('Resized Scaled', resized_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

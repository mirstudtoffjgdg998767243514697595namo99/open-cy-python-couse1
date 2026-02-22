import cv2

# 1. Load image
img = cv2.imread(r'C:\Users\USER\Pictures\download.jpg')

# 2. Transform: Flip -> Rotate -> Resize
img = cv2.flip(img, 1)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img = cv2.resize(img, (400, 400)) # Default interpolation is fine for general use

# 3. Show Result
cv2.imshow('Final Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


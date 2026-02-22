import cv2

# Load the image
image = cv2.imread(r'C:\Users\USER\Pictures\download.jpg')

# Flip options:
# 0  = Flip vertically (around x-axis)
# 1  = Flip horizontally (around y-axis)
# -1 = Flip both vertically and horizontally
flipped_image = cv2.flip(image, 1) # This flips it horizontally

# Show the results
cv2.imshow('Original', image)
cv2.imshow('Flipped', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2


image = cv2.imread(r'C:\Users\USER\Pictures\download.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

save = cv2.imwrite('new2.jpeg', gray)

cv2.imshow('new image', save)
cv2.waitKey(0)
cv2.destroyAllWindow()


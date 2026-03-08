import cv2

img = cv2.imread(r'C:\Users\USER\Downloads\superman.jpg')

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(grayscale, 100, 255, cv2.THRESH_BINARY)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('original', img)
cv2.imshow('Grayscale', grayscale)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)


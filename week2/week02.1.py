import cv2

cap = cv2.VideoCapture(0) 

if not cap.read():
    print("cant cam")

while True:
    res, frame = cap.read()


    if not res:
        print('not found')
        break

    cv2.imshow('My camera', frame)

    # 1 = custom key (press q to make true)
    if cv2.waitKey(1) == ord('q'):
        break
#0 = any key to make true

cv2.waitKey(0)
cv2.destroyAllWindow()
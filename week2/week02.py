import cv2 as opencv

cap = opencv.VideoCapture('imgs\meme2.mp4')

while True:
    res, frame = cap.read()


    if not res:
        print('not found')
        break

    opencv.imshow('Frame', frame)

    if opencv.waitKey(1) == ord('q'):
        break

opencv.waitKey(0)
opencv.destroyAllWindow()
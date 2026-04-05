import cv2

# 1. โหลดไฟล์ Haar Cascade สำหรับตรวจจับใบหน้า (ไฟล์นี้ปกติจะมาพร้อมกับ OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. เปิดกล้อง (0 คือกล้องหลักของเครื่อง)
cap = cv2.VideoCapture(0)

print("กำลังเปิดกล้อง... (กด 'q' เพื่อออกจากโปรแกรม)")

while True:
    # อ่านเฟรมจากกล้อง
    ret, frame = cap.read()
    if not ret:
        break

    # 3. แปลงภาพเป็นสีเทา (Grayscale) เพื่อให้ประมวลผลได้เร็วขึ้น
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 4. ตรวจจับใบหน้า
    # scaleFactor: ปรับขนาดภาพเพื่อให้ตรวจจับหน้าได้หลายระยะ
    # minNeighbors: กำหนดความเข้มงวดในการตรวจจับ (ค่ามากจะตรวจจับแม่นยำขึ้นแต่ยากขึ้น)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 5. วาดกรอบสี่เหลี่ยมรอบใบหน้า
    for (x, y, w, h) in faces:
        # cv2.rectangle(ภาพเนื้อหา, (จุดเริ่มต้น), (จุดสิ้นสุด), (สี BGR), ความหนาเส้น)
        # (0, 255, 0) คือสีเขียวในระบบ BGR
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # แสดงผลลัพธ์ในหน้าต่างใหม่
    cv2.imshow('Face Detection - Press q to exit', frame)

    # กด 'q' เพื่อหยุดการทำงาน
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# คืนทรัพยากรให้ระบบ
cap.release()
cv2.destroyAllWindows()

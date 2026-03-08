import cv2  # นำเข้าไลบรารี OpenCV
import numpy as np  # นำเข้าไลบรารี numpy เพื่อจัดการเรื่องแถวลำดับ (Array)

# อ่านภาพจากตำแหน่งที่ระบุ
img = cv2.imread(r'C:\Users\USER\Downloads\superman.jpg')

# แปลงระบบสีจาก BGR เป็น HSV เพื่อให้ง่ายต่อการคัดแยกสี (สำคัญมาก)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# กำหนดช่วงค่าสีน้ำเงินต่ำสุดและสูงสุดในระบบ HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# สร้าง Mask โดยเลือกเฉพาะพื้นที่ที่มีค่าสีอยู่ในช่วงที่กำหนด (สีน้ำเงิน)
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# นำภาพต้นฉบับมาซ้อนกับ Mask เพื่อดึงเฉพาะส่วนที่เป็นสีน้ำเงินออกมา
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('original', img)    # แสดงภาพต้นฉบับ
cv2.imshow('hsv', hsv)          # แสดงภาพในระบบสี HSV
cv2.imshow('mask', mask)        # แสดงภาพ Mask ที่คัดกรองสีแล้ว
cv2.imshow('result', result)    # แสดงผลลัพธ์เฉพาะส่วนที่เป็นสีน้ำเงิน
cv2.waitKey(0)                  # รอการกดปุ่มเพื่อปิดหน้าต่าง

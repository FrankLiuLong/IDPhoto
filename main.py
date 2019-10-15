#导入需要的模块
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    cv2.namedWindow("1122",0)
    cv2.resizeWindow("1122",1280,1080)
    cv2.imshow("1122",img)

cap.release()
cv2.destroyAllWindows()

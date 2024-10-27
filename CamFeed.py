import cv2
import time

cam = cv2.VideoCapture(0)
time.sleep(1)
_,img = cam.read()
cv2.imwrite("imgfromCam.jpg",img)
cv2.imshow("imgfromCamFeed",img)
        
while True:
    _,img = cam.read()
    cv2.imshow("CamFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

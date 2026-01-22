import cv2

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        print("quitting")
        break
    #cv2.imwrite("phas4/video_cap.jpeg",frame)
cap.release()
cv2.destroyAllWindows()
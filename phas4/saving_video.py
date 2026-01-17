import cv2

cap=cv2.VideoCapture(0)
frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter("phas4/output1.mp4",codec,20.0,(frame_width,frame_height))
while True:
    ret,frame=cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
out.release()
import cv2
image=cv2.imread("phase1/new.jpeg")
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
new_image=cv2.putText(image,"Hello World",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),5)
cv2.imshow("New Image",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

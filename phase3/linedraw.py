import cv2
image=cv2.imread("phase1/new.jpeg")
cv2.imshow("Image",image)
pt1=(100,100)
pt2=(300,300)
cv2.line(image,pt1,pt2,(255,0,0),5)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()  

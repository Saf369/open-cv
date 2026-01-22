import cv2
image=cv2.imread("phase1/new.jpeg")
cv2.imshow("Image",image)
cv2.circle(image,(100,100),10,(255,0,0),5)
cv2.imwrite("phase3/circle_image.jpeg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
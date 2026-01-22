import cv2
image=cv2.imread("phase1/new.jpeg",cv2.IMREAD_GRAYSCALE)
ret,thresh=cv2.threshold(image,120,255,cv2.THRESH_BINARY)
cv2.imshow("Image",image)
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
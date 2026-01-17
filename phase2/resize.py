import cv2
image=cv2.imread("phase1/new.jpeg")
cv2.imshow("Image",image)
resized_image=cv2.resize(image,(300,300))
cv2.imshow("Resized Image",resized_image)
cv2.imwrite("phase2/resized_image.jpeg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

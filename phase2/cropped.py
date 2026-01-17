import cv2
image=cv2.imread("phase1/new.jpeg")
cropped_image=image[100:200,100:200]
cv2.imshow("Image",image)
cv2.imshow("Cropped Image",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("phase2/cropped_image.jpeg",cropped_image)
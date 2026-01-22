import cv2
image=cv2.imread("phase1/new.jpeg")
cv2.imshow("Image",image)
if(image is not None):
    h,w,c=image.shape
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,90,1.0)
    rotated_image=cv2.warpAffine(image,M,(w,h))
    cv2.imshow("Rotated Image",rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("phase2/rotated_image.jpeg",rotated_image)
else:
    print("Image not found")
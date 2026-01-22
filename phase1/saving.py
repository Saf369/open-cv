import cv2
image=cv2.imread("phase1/new.jpeg")
if(image is not None):
    cv2.imwrite("phase1/new.jpeg",image)
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
    
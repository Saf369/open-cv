import cv2
image=cv2.imread("phase1/new.jpeg")
if(image is not None):
    h,w,c=image.shape
    print("Height:",h)
    print("Width:",w)
    print("Channels:",c)
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
    
import cv2

image=cv2.imread("phase1/new.jpeg")
while True:
    shape_type=input("Enter the shape type:")
    match shape_type:
        case "circle":
            newimage=cv2.circle(image,(100,100),10,(255,0,0),5)
            cv2.imshow("Image",newimage)
            print("circle")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        case "rectangle":
            newimage=cv2.rectangle(image,(100,100),(150,150),(255,0,0),5)
            cv2.imshow("Image",newimage)
            print("rectangle")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        case "text":
            newimage=cv2.putText(image,"Hello World",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),5)
            cv2.imshow("Image",newimage)
            print("text")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        case _:
            # Default case
            pass

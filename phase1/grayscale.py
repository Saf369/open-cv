import cv2

image=cv2.imread("phase1/new.jpeg")
if(image is not None):
    print("Options:")
    print("1: Convert to Grayscale and Display")
    print("2: Save Grayscale Image")
    initial_choice = input("Enter your choice (1/2): ").strip()
    
    match initial_choice:
        case '1':
            gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            cv2.imshow("Gray Image",gray_image) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
        case '2':
            gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            cv2.imwrite("phase1/new_gray12.jpeg",gray_image)
            print("Grayscale image saved as 'phase1/new_gray12.jpeg'")
        
else:
    print("Image not found")
import cv2

img=cv2.imread("phase5/pentagon.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(f"Number of contours found: {len(contours)}")

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.drawContours(img, [approx], -1, (0, 0, 255), 2)
    corners=len(approx)
    if(corners==3):
        cv2.putText(img, "Triangle", (contour[0][0][0], contour[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif(corners==4):
        cv2.putText(img, "Rectangle", (contour[0][0][0], contour[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif(corners==5):
        cv2.putText(img, "Pentagon", (contour[0][0][0], contour[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif(corners==6):
        cv2.putText(img, "Hexagon", (contour[0][0][0], contour[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(img, "Circle", (contour[0][0][0], contour[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Thresh", thresh)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

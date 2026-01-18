import cv2
import numpy as np

img1=np.zeros((200,200,3),np.uint8)
cv2.rectangle(img1,(50,50),(150,150),(255,255,255),-1)
img2=np.zeros((200,200,3),np.uint8)
cv2.circle(img2,(100,100),50,(255,255,255),-1)
bitwise_and=cv2.bitwise_and(img1,img2)
bitwise_or=cv2.bitwise_or(img1,img2)
bitwise_xor=cv2.bitwise_xor(img1,img2)
bitwise_not=cv2.bitwise_not(img1)
cv2.imshow("Image 1",img1)
cv2.imshow("Image 2",img2)
cv2.imshow("Bitwise AND",bitwise_and)
cv2.imshow("Bitwise OR",bitwise_or)
cv2.imshow("Bitwise XOR",bitwise_xor)
cv2.imshow("Bitwise NOT",bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
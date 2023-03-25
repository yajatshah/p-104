import cv2
img=cv2.imread("C:/Users/yajat/OneDrive/Desktop/Python classes/Python projects/solar-system.jpg")

cv2.putText(img,"Sun",(100,80),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255)) 
cv2.putText(img,"Mercurary",(110,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255)) 
cv2.putText(img,"Venus",(190,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.putText(img,"Earth",(300,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255)) 
cv2.putText(img,"Mars",(400,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255)) 
cv2.putText(img,"Jupiter",(500,90),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.putText(img,"Saturn",(720,110),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255)) 
cv2.putText(img,"Uranus",(950,113),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))     
cv2.putText(img,"Neptune",(1080,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))           
cv2.imshow("Display Image",img)
cv2.waitKey(0)
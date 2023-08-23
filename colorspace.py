import cv2

img = cv2.imread("insangrubu1.jpg")
cv2.imshow("Orijinal", img)
 
 #conversion to gray color base from blue,green,red color base
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

 #conversion to hsv(hue, saturation,value) from blue green, red color base
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
 
#convesion to lab(lightness, unique colors) from blue green red color base
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
 #conversion to red, green, blue color base from blue green red color base
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)
 
 #conversion from hsv to bgr
hsv_bgr = cv2.cvtColor(lab, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV BGR", hsv_bgr)
 
cv2.waitKey(0)
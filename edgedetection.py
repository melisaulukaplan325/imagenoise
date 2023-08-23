import cv2

img = cv2.imread("house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#gaussian blur is needed for a edge ditaction with less noise
gaussian = cv2.GaussianBlur(gray, (3,3), 0)

cannyedge = cv2.Canny(gaussian, threshold1=25, threshold2=25)

cv2.imshow("canny", cannyedge)

cv2.waitKey(0)
cv2.destroyAllWindows()



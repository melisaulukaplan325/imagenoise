import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("house.jpg")

#gaussian blur wit 7 to 7 kernel
gaussian = cv2.GaussianBlur(img,(7,7), 0)
#median blur with 15 kernel
median = cv2.medianBlur(img, 15)
#bileteral blur can use gaussian disturbition
bilateral = cv2.bilateralFilter(img, 9, 750, 750)
blur= cv2.blur(img,(5,5))

cv2.imshow("Gaussian Blur",gaussian)
cv2.imshow("Median Blur",median)
cv2.imshow("Bilateral blur",bilateral)
cv2.imshow("Normalized blur", blur)

plt.subplot(221),plt.imshow(img,cmap = 'gray')
plt.title('Normal Image'), plt.xticks([]), plt.yticks([])


plt.subplot(222),plt.imshow(gaussian,cmap = 'gray')
plt.title('Gaussian Blur'), plt.xticks([]), plt.yticks([])


plt.subplot(223),plt.imshow(median,cmap = 'gray')
plt.title('Median Blur'), plt.xticks([]), plt.yticks([])


plt.subplot(224),plt.imshow(bilateral,cmap = 'gray')
plt.title('Bilateral Blur'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()
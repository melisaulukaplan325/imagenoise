import cv2
import numpy as np
from matplotlib import pyplot as plt

img0= cv2.imread("insangrubu1.jpg")
img1= cv2.imread("insangrubu1.jpg", 0)
img1 = img1/255.0


row, col = img1.shape
mean = 0
var = 0.01
sigma = np.sqrt(var)
gaussian = np.random.normal(loc = mean,
                    scale = sigma,
                    size = (row, col))

gaussian_img = gaussian + img1

smooth_part = gaussian[:30, :30]

plt.subplot(221),plt.imshow(img0,cmap = 'gray')
plt.title('Normal Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(gaussian_img,cmap = 'gray')
plt.title('Gaussian Noise Image'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.hist(img0.ravel(),256,[0,256])#; plt.show()
plt.title('Original Image Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.hist(gaussian_img.ravel(),256,[0,2])#; plt.show()
plt.title('Noisy Image Histogram'), plt.xticks([]), plt.yticks([])


#plt.subplot(224),plt.hist(img1.ravel(),256,[0,256])#; plt.show()
#plt.title('Estimated Noise Distribution'), plt.xticks([]), plt.yticks([])
plt.show()


#cv2.imshow("Gaussian noise", gaussian_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2
import numpy as np
from matplotlib import pyplot as plt


img0= cv2.imread("insangrubu1.jpg")
img = cv2.imread("insangrubu1.jpg", cv2.IMREAD_GRAYSCALE)

img=img/255.0

gama = np.random.gamma(0.1, 20, (533,800))/255

gama_img = img + gama 

#cv2.imshow("Original Image",img)
#cv2.imshow("Gama Noise",gama_img)


plt.subplot(221),plt.imshow(img0,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(gama_img,cmap = 'gray')
plt.title('Gama Noise Image'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.hist(img0.ravel(),256,[0,256])#; plt.show()
plt.title('Original Image Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.hist(gama_img.ravel(),256,[0,2])#; plt.show()
plt.title('Gama Noisy Image Histogram'), plt.xticks([]), plt.yticks([])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

#salt and papper
def saltandpepper(img):
    [row, colm] = img.shape
    #Random pixel numbers for putting black and white dots
    pixelnumber = random.randint(3000,100000)
    for i in range(pixelnumber):
        y_crd= random.randint(0,row-1)
        x_crd = random.randint(0,colm-1)
        img[y_crd][x_crd] = 255
    for i in range(pixelnumber):
        y_crd= random.randint(0,row-1)
        x_crd = random.randint(0,colm-1)
        img[y_crd][x_crd] = 0
    return img
    
#gaussian
img1= cv2.imread("image.jpg",0)
img1 = img1/255.0

row, col = img1.shape
mean = 0
var = 0.01
sigma = np.sqrt(var)
#creating noise like a gaussian disturbition
gaussian = np.random.normal(loc = mean,
                    scale = sigma,
                    size = (row, col))

gaussian_img = gaussian+ img1


#rayleigh
rayleigh = np.random.rayleigh(0.2, img1.shape)
rayleigh_img = rayleigh + img1

#gama
gama = np.random.gamma(0.1, 20, (3237,5755))
gama_img = img1 + gama 

img =  cv2.imread("image.jpg")
orgimg = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Form",img)



cv2.imwrite("C:\\staj\\saltpaperimg.jpg", saltandpepper(orgimg))
cv2.imshow("Salt-Pepper Noise Form",cv2.imread("C:\\staj\\saltpaperimg.jpg", cv2.IMREAD_COLOR))

cv2.imshow("Gama Noise",gama_img)

cv2.imshow("Rayleigh Image", rayleigh_img)

cv2.imshow("Gaussian noise", gaussian_img)

plt.subplot(221),plt.hist(gaussian_img.ravel(),20,[0,20])
plt.title('Gaussian Noise Image Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.hist(rayleigh_img.ravel(),20,[0,20])
plt.title('Rayleigh Noise Image'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.hist(gama_img.ravel(),20,[0,20])#; plt.show()
plt.title('Gama Noisy Image Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.hist(img.ravel(),20,[0,20])
plt.title('Image Histogram'), plt.xticks([]), plt.yticks([])

#plt.subplot(224),plt.hist(gama_img.ravel(),256,[0,256])#; plt.show()
#plt.title('Gama Noisy Image Histogram'), plt.xticks([]), plt.yticks([])

plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()
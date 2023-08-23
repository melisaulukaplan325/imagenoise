import cv2
import numpy as np
from matplotlib import pyplot as plt

def scretch(img, sigma=2, plot=False):
   #creating an empty array with the same rows and cols as img
    strecthed = np.zeros(img.shape)

    #collecting pixels between 0-255 and putting them inside scretched array
    for i in range(img.shape[2]):
        band = img[:,:,i]
        if np.min(band)<0:
            band = band+ np.abs(np.min(band))
            band = band/np.max(band)
            band = band * 255
        std= np.std(band) #calculating standart derivation for calculating 
        mean = np.mean(band)
        max = mean+(std*sigma)
        min = mean-(std*sigma)
        band = (band-min)/(max-min)*255

        band[band>255]=255
        band[band<0]=0
        strecthed[:,:,i] = band

    strecthed = strecthed.astype('int')
    return strecthed


original = cv2.imread("contrast.jpg")
img = scretch(original, 2, False)


plt.subplot(221),plt.imshow(original, cmap= 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(img, cmap= 'gray')
plt.title('Scretched Image'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.hist(original.ravel(),256,[0,256])#; plt.show()
plt.title('Original Image Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.hist(img.ravel(),256,[0,256])
plt.title('Scretched Image Histogram'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows() 
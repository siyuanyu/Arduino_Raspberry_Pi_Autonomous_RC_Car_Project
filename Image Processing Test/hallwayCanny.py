import cv2
import numpy
from matplotlib import pyplot as plt
import io
#from picamera import PiCamera

#Create a memory stream so photos doesn't need to be saved in a file
#stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)

#camera = PiCamera()
#camera.resolution = (320, 240)
#camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array

width=640
img = cv2.imread('Hallway.jpg', 1)
r = float(width) / img.shape[1]
dim = (width, int(img.shape[0]*r))
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#Now creates an OpenCV image
#img = cv2.imdecode(buff, 1)

edges = cv2.Canny(resized_img,100,200)

plt.subplot(121),plt.imshow(resized_img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

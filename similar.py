
import cv, cv2
import matplotlib.pyplot as pyplot
import numpy as np
import matplotlib.image as mpimg

imgName     = 'shirt-black';
img         = cv2.imread(imgName + '.jpg', 0)
edges       = cv2.Canny(img, 100, 200)
kernel      = np.ones((8, 8), np.uint8)
dilation    = cv2.dilate(edges, kernel, iterations = 1)
closing     = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

#erosion     = cv2.erode(dilation, kernel, iterations = 1)

img = cv2.imwrite(imgName + '-cv.jpg', closing)


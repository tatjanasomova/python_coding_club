import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg')
#image0 = cv2.imread(r'C:\Users\som87475\source\repos\python\coding club 2021\sunset.jpg')
image0 = cv2.imread('sunset.jpg')

image1 = cv2.imread('image1.png')
image2 = cv2.imread('image2.png')
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BAYER_GB2GRAY)
print(image2)

cv2.cvtColor()

output = cv2.inpaint(image1, image2_gray, 10, flags=cv2.INPAINT_TELEA)
cv2.imshow('Image', image1)
cv2.imshow('Mask', image2)
cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

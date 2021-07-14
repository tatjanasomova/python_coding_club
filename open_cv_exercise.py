# To select Interpreter command from the Command Palette (Ctrl+Shift+P)
# Select .venv
import numpy as np
import cv2 as cv

#image0 = cv.imread(r'C:\Users\som87475\source\repos\python\coding club 2021\sunset.jpg')
image0 = cv.imread('sunset.jpg')

image1 = cv.imread('image1.png')
image2 = cv.imread('image2.png')
image2_gray = cv.cvtColor(image2, cv.COLOR_BAYER_GB2GRAY)
print(image2)

cv.cvtColor()

output = cv.inpaint(image1, image2_gray, 10, flags=cv.INPAINT_TELEA)
cv.imshow('Image', image1)
cv.imshow('Mask', image2)
cv.imshow('Output', output)
cv.waitKey(0)
cv.destroyAllWindows()

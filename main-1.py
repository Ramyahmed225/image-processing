
import cv2 as cv
import numpy as np

img = cv.imread('Before.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('After.jpg',res)


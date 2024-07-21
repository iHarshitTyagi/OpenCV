import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img.shape)
# img[200:300] = 255,0,0

cv2.line (img,(0,0),(300,300),(0,255,0),3) # Create a line on image

cv2.imshow('image',img)

cv2.waitKey(0)
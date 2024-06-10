import cv2
import os
from time import sleep

cam= cv2.VideoCapture(0)
directory = r'C:\Users\MegaN\Documents\Fulvous\Fulvous'

# show test shot
while True:
    ret, image = cam.read()
    cv2.imshow('Imagetest' ,image)
    k = cv2.waitKey(1)
    if k != -1:
        break
os.chdir(directory)

# start timelapse
for i in range(3):
    ret, image = cam.read()
    cv2.imwrite('imagetest{0:04d}.jpg'.format(i), image)
    sleep(10)

cam.release()
cv2.destroyAllWindows()
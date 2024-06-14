import cv2
import os
import imageio
from os import system
from time import sleep

cam= cv2.VideoCapture(0)
directory = r'/home/megan/pi'

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

with imageio.get_writer('timelapse.gif', mode='I') as writer:
    

cam.release()

#create animation with ImageMagick goal 600 sleep and 50 photos
# system('convert  -delay 10 -loop 0 image*.jpg animation.gif')

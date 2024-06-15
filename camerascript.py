import cv2
import os
import imageio
from os import system
from time import sleep

cam= cv2.VideoCapture(0)
directory = r'/home/megan/pi'
frames=[]

# show test shot
while True:
    ret, image = cam.read()
    cv2.imshow('Imagetest' ,image)    
    k = cv2.waitKey(1)
    if k != -1:
        break
os.chdir(directory)

# start timelapse
for i in range(4):
    ret, image = cam.read()
    cv2.imwrite('imagetest{0:04d}.png'.format(i), image)
    frames.append(image)
    sleep(10)

with imageio.get_writer('timelapse.gif', mode='I') as writer:
    for idx, frame in enumerate(frames):
        print('adding frame to Gif file'), idx+1
        #change color mode from BGR to RGB to remove blue tint
        rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)

cam.release()

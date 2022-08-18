import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import time

width =GetSystemMetrics(0)
height= GetSystemMetrics(1)


file_name=f"video{str(time.strftime('%d-%m-%Y %H-%M-%S'))}.mp4"
#It is used to show the version of video ie being recorded.
forcc=cv2.VideoWriter_fourcc('m','p','4','v')


#for capturing a photo and then conveqrting it to video "CODEC"
#20 is fps here
capture_video=cv2.VideoWriter(file_name,forcc,20.0,(width,height))

while True:
    #screen_img is used to show how much screen it will capture.
    screen_img=ImageGrab.grab(bbox=(0,0,width,height))
    
    #In array_img it is used to storing width and legth array of
    #screen_img 
    array_img=np.array(screen_img)
    
    #Color_img is used to show correct colors of screen
    color_img=cv2.cvtColor(array_img,cv2.COLOR_BGR2RGB)
    
    capture_video.write(color_img)
    #Upper header of a screen will be describe by this:
    cv2.imshow("Screen Recorder by Shreyas",color_img)
    if cv2.waitKey(1)==ord("q"):
        break


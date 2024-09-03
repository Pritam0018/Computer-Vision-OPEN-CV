import cv2
import pyautogui
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.8,maxHands=1,)
cap=cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))


output_file = 'output_video.mp4'
video_writer = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
while True:
    _,img=cap.read()
    hands,img=detector.findHands(img)
    if hands:
        lmlst=hands[0]['lmList']   
        length1,img,_= detector.findDistance(lmlst[4][0:2],
                                                  lmlst[8][0:2],
                                                  img=img,
                                                  color=(255, 0, 0),
                                                  scale=10)
        length2,img,_= detector.findDistance(lmlst[4][0:2],
                                                  lmlst[20][0:2],
                                                  img=img,
                                                  color=(255, 0, 0),
                                                  scale=10)
        if length1 > 90:
           pyautogui.keyDown('up')
        else:
            pass   
        if length2 > 90:
            pyautogui.keyDown('enter')        
        else:
           pass
    cvzone.putTextRect(img,f'GOOGLE-DINOSAUR-GAME',(100,35),2,2,colorT=(255,255,255),colorR=(0,255,0),border=3,colorB=())    
    cv2.imshow("GOOGLE - DINOSAUR - GAME ",img)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('q'):
        break

cap.release()
video_writer.release()

cv2.destroyAllWindows()

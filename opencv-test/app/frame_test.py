import cv2
from time import sleep

cap = cv2.VideoCapture(0)

while (True):
    print('Reading camera frame using openCV...')
    ret, frame = cap.read()
    print('done.')
    height, width, channels = frame.shape
    print('Frame width: ' + str(width))
    print('Frame height: ' + str(height))
    print('Frame channels: ' + str(channels))
    sleep(60)

cap.release()

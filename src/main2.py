import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\video1.avi')
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

lk_params = dict( winSize  = (20,20),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
for index in range(10):
    ret, frame = cap.read()
ret, frame = cap.read()
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

frame_anterior = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
punto_elegido = cv2.goodFeaturesToTrack(frame_anterior, 7, 0.05, 25)
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    #Se aplica el metodo de Lucas Kanade
    punto_elegido, st, err = cv2.calcOpticalFlowPyrLK(frame_anterior, frame_gray, punto_elegido, punto_elegido, **lk_params)
 
    #Pintamos el centro (lo hacemos con un bucle por si, por alguna razon, decidimos pintar mas puntos)
    for i in punto_elegido:
          cv2.circle(frame,tuple(i[0]), 5, (0,0,255), -1)
          
    #Se guarda el frame de la iteracion anterior del bucle
    frame_anterior = frame_gray.copy()
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
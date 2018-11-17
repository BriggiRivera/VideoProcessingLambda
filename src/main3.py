import numpy as np
import cv2 as cv

def increase_brightness(img, value=10):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv.merge((h, s, v))
    img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
    return (255 - img)

def processVideo(path, output):
    cap = cv.VideoCapture(path, apiPreference=cv.CAP_FFMPEG)
    width = int( cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height =int( cap.get( cv.CAP_PROP_FRAME_HEIGHT))
    fps =  cap.get(cv.CAP_PROP_FPS)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(output, fourcc, 64, (width,height))

    ret, frame = cap.read()
    previous = frame.copy()
    while(ret):
        result = increase_brightness(cv.subtract(frame, previous))
        cv.imshow('Show',result)
        k = cv.waitKey(60) & 0xff
        if k == 27:
            break
        previous = frame.copy()
        ret ,frame = cap.read()
        out.write(result)
    cv.destroyAllWindows()
    cap.release()
    out.release()
    
processVideo('D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\video.mp4',
            'D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\video_processed.mp4')

"""
cap = cv.VideoCapture('D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\splitted.mp4')
# take first frame of the video
ret,frame = cap.read()
# setup initial location of window
r,h,c,w = 460,40,180,80  # simply hardcoded the values
track_window = (c,r,w,h)
# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
height = np.size(frame, 0)
width = np.size(frame, 1)
fourcc = cv.VideoWriter_fourcc(*'DIVX')
path = 'D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\splitted_processed.mp4'
out = cv.VideoWriter(path, fourcc, 1, (width,height), False)

while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        #cv.imshow('img2',img2)
        k = cv.waitKey(60) & 0xff
        if k == 27:
            break
        out.write(img2)
    else:
        break
cv.destroyAllWindows()
cap.release()
out.release()
"""
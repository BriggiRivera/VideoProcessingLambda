import numpy as np
import moviepy

"""def increase_brightness(img, value=30):
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
    out = cv.VideoWriter(output, fourcc, 32, (width,height))

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
    
processVideo('D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\splitted.mp4',
            'D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\processed.mp4')

"""

import moviepy.editor as mpe
video = mpe.VideoFileClip('D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\video.mp4')
np_frame = video.get_frame(2) # get the frame at t=2 seconds
np_frame = video.get_frame(10 * 32) # get frame by index
video.save_frame('my_image.jpeg', t=2) # save frame at t=2 as JPEG
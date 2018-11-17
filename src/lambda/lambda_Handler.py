from __future__ import print_function

import os.path as osp
import os
import boto3
import sys
import uuid
import cv2 as cv
import numpy as np

s3_client = boto3.client('s3')

def handler(event, context):
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        s3_client.download_file(bucket, key, download_path)
        processed_path = '/tmp/{}{}'.format("processed-", key)
        processVideo(download_path, processed_path)
        
        s3_client.upload_file(processed_path, '{}-transformed'.format(bucket), key)

def increase_brightness(img, value=30):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv.merge((h, s, v))
    img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
    return (255 - img)

def processVideo(path, output):
    cap = cv.VideoCapture(path)
    width = int( cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height =int( cap.get( cv.CAP_PROP_FRAME_HEIGHT))
    fps =  cap.get(cv.CAP_PROP_FPS)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(output, fourcc, 32, (width,height))

    ret, frame = cap.read()
    previous = frame.copy()
    while(ret):
        result = increase_brightness(cv.subtract(frame, previous))
        previous = frame.copy()
        ret ,frame = cap.read()
        out.write(result)
    cv.destroyAllWindows()
    cap.release()
    out.release()
    

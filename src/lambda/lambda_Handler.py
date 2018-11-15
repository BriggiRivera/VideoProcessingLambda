from __future__ import print_function

import os.path as osp
import os
import boto3
import sys
import uuid
from skimage import filters
from skimage.io import imread, imsave

s3_client = boto3.client('s3')

def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        s3_client.download_file(bucket, key, download_path)

        image = imread(download_path, flatten=True)
        edges = filters.sobel(image)

        processed_path = '/tmp/{}{}'.format("processed-", key)
        imsave(processed_path, edges)

        s3_client.upload_file(processed_path, '{}-transformed'.format(bucket), key)

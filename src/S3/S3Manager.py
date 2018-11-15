import boto3
import os

from os.path import join

class S3Manager:
    def __init__(self, bucketName):
        self.s3Client = boto3.client('s3')
        self.bucket_name = bucketName
        
    def upload(self, fullPath, fileName):
        self.s3Client.upload_file(join(fullPath, fileName), self.bucket_name, fileName)

    def download(self, path, fileName):
        self.s3Client.download_file(self.bucket_name, fileName, join(path, fileName))
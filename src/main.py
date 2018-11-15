import sys
import boto3
import os

from os import listdir
from os.path import isfile, join
from S3.S3Manager import S3Manager

from PIL import Image, ImageSequence

def main(argv):
    im = Image.open("D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\video.mp4")
    index = 1
    for frame in ImageSequence.Iterator(im):
        frame.save("D:\\Maestria\\Cloud Computing\\VideoProcessing\\VideoProcessingLambda\\videos\\frame%d.png" % index)
        index = index + 1

def main1(argv):

    directory = argv[1]
    print(directory)
    pictures = [picture for picture in listdir(directory) if isfile(join(directory, picture)) and picture.endswith('.mp4')]
    manager_input = S3Manager("briggi-rivera-guillen-videos")
    manager_output = S3Manager("briggi-rivera-guillen-videos-processed")
    
    for picture in pictures:
        manager_input.upload(directory, picture)
    
    output_directory = join(directory, "Procesados")
        
    for picture in pictures:
        print(picture)
        manager_output.download(output_directory, picture)

if __name__ == "__main__":
    main(sys.argv)
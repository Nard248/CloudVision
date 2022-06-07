import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Nard\Desktop\vision\token.json'

client = vision.ImageAnnotatorClient()

with io.open('sign_small.jpg', 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)



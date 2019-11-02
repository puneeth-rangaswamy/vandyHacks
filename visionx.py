import io
import os
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

file_name = os.path.join(
    os.path.dirname(__file__),
    'car.jpg')

with io.open(file_name,'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.web_detection(image=image)

labels = response.web_detection

print(labels.web_entities[0].description)
#for i in labels:
#  if(i.entity_id=="Commercial Street"):
#   print(i);
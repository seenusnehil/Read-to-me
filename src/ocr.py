import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/revanth/Documents/GitHub/Read-to-me/google.json'
from google.cloud import vision
import re
from PIL import Image

def detect_text(path):
    output=[]
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    # with io.open(path, 'rb') as image_file:
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    # content = img

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    output.append(texts[0].description)
    #for text in texts:
     #   print('\n"{}"'.format(text.description))

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
          #          for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return output
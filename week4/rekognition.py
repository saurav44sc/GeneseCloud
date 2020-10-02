import boto3
from PIL import Image, ImageDraw, ImageFont

ACCESS_KEY = 'ASIARXJJI4W2DUNCZPGP'
SECRET_KEY = 'qZ6ADnKNX4iEckzi6zLstAHsp0a2SRTO+bNx3i4H'
SESSION_TOKEN = 'FwoGZXIvYXdzEHkaDMm9rvrdSlr9O3hVsCLbAbd1PVrULqk0uknx2ikV8b29I7D2cb89c2dQvRkvAZ89JTQMu7Lkug6Z9S0nJJ1kawzvy1xSBkzOcPKsFCxC5nN/+SROHvka1IEhVdIimhQj61EWBcMH4D2/oAdvuDmqvuhcuxdj3ozLrqRsFXtMRRK78Ze904TwRQyNcL4s0r6gT3Y6DhmwyzkshzqyzA8fmMtCBZd5yyGE5LrIOnCAVbogcayaXCxvTvV71Sbk1X+JzKZWQeYVqUw9PlOfUPVogERK63I92+RjaiLeckk6S2fnYb9iyylfGoGqRSjdkt37BTItPKfnDC1bGJJ82q1Z2KugGSw/uV7xxYlCA33F1Oro9ju+zK0dmF3J5BzIsE3o'

# Input photo link
photo = 'images/5.jpg'

# Create a rectangular box in the image
def box_image(boxes, photo):
    with Image.open(photo) as im:
        for idx, box in enumerate(boxes):
            draw = ImageDraw.Draw(im)
            top_left = box['Left']*im.size[0], box['Top']*im.size[1]
            bottom_right = (box['Left']+box['Width']) * \
                im.size[0], (box['Top']+box['Height'])*im.size[1]
            top_right = (box['Left']+box['Width']) * \
                im.size[0], (box['Top'])*im.size[1]
            bottom_left = (box['Left']) * \
                im.size[0], (box['Top']+box['Height'])*im.size[1]
            draw.line(top_left + top_right, fill=128, width=20)
            draw.line(top_right + bottom_right, fill=128, width=20)
            draw.line(bottom_right + bottom_left, fill=128, width=20)
            draw.line(bottom_left + top_left, fill=128, width=20)

            fnt = ImageFont.truetype("FreeMono.ttf", 140)
            # draw text, half opacity
            draw.text((top_left[0], top_left[1]*1.15),
                      "Face "+str(idx+1), font=fnt, fill=(255, 255, 255, 255))
        return im

# Sets up the boto3 for rekognition
client = boto3.client('rekognition',
                      region_name='us-east-1',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      aws_session_token=SESSION_TOKEN
                      )

# Reads the input image and request the rekognition and receive the response
with open(photo, 'rb') as image:
    response = client.detect_faces(
        Image={'Bytes': image.read()}, Attributes=['ALL'])
    faces = response['FaceDetails']

# Iterate through every face and gather the output
all_faces_data = []
for face in faces:
    face_data = {}
    face_data['age_range'] = face['AgeRange']['Low'], face['AgeRange']['High']
    face_data['Sunglasses'] = face['Sunglasses']['Value']
    face_data['Beard'] = face['Beard']['Value']
    face_data['Mustache'] = face['Mustache']['Value']
    face_data['Emotions'] = [emotion['Type'] for emotion in face['Emotions'] if emotion['Confidence'] > 70]
    face_data['BoundingBox'] = face['BoundingBox']
    all_faces_data.append(face_data)

# Create a box in the input photo for faces and saves the resultant image
boxes = [face['BoundingBox'] for face in all_faces_data]
im = box_image(boxes, photo)
im.save(photo+'box.png', "PNG")

# Total number of faces detected
total_faces = len(all_faces_data)

# Print the results
print('No. of faces detected: {}'.format(total_faces))
for n,face in enumerate(all_faces_data):
    print()
    if total_faces > 1:
        print('Face {}'.format(n+1))
    print('Age Range: {} to {} years'.format(*face_data['age_range']))
    if face['Emotions']:
        print('Emotion of face: ', ' '.join(face['Emotions']))
    if face['Sunglasses']:
         print('This person seems to be wearing Sunglasses')
    if face['Beard']:
        print('This person seems to have Beard')
import face_recognition as fr
import cv2
import numpy as np
import os
import json
from django.urls import reverse
# from google_drive_api import *
import ast
import requests
import face_recognition
import gdown
import re
from PIL import Image
from io import BytesIO
import base64

# from image_data import image_url

def get_encoded_face_content(request):
    encodedfaces_url = request.build_absolute_uri(reverse('encodedfaces-list'))
    
    encoded_faces = requests.get(f"{encodedfaces_url}1").json()
    return encoded_faces

def update_encoded_face_content(employee_id,encoded_data,request):
    encodedfaces_url = request.build_absolute_uri(reverse('encodedfaces-list'))
   
    encoded_faces = get_encoded_face_content(request)
    # print(encoded_faces)
    encoded_faces['encoded_faces'][employee_id] = encoded_data
    data = {"encoded_faces":json.dumps(encoded_faces["encoded_faces"])}
    # print(data)
    
    response = requests.patch(f"{encodedfaces_url}1/",data = data)
    return response.status_code

def generate_face_encodings(data_url):
    image = load_image_from_data_url(data_url)
    image_np = np.array(image)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
    
    face_locations = face_recognition.face_locations(image_np)
    face_encodings = face_recognition.face_encodings(image_np)[0]
    
    return face_encodings.tolist()

def create_encoded_face_json_file(data_url,employee_id,request):
    face_encodings = generate_face_encodings(data_url)
    
    status = update_encoded_face_content(employee_id,face_encodings,request)
    if status == 200:
        return True
    else:
        return False


    
    


   
def load_image_from_data_url(data_url):
    format, encoded_data = data_url.split(';base64,')
    image_type = format.split('/')[-1]
    image_data = base64.b64decode(encoded_data)
    image = Image.open(BytesIO(image_data))
    return image

def face_recognizer(data_url,request):
    encoded_images = get_encoded_face_content(request)['encoded_faces']

    live_image = load_image_from_data_url(data_url)
    print(live_image)
    live_image = np.array(live_image)
    # print(live_image)
    rbg_image = cv2.cvtColor(live_image,cv2.COLOR_BGR2RGB)
            
    face_cur_locations = fr.face_locations(rbg_image)
    encoded_live_faces = fr.face_encodings(rbg_image, face_cur_locations)

    
    new_known_faces = {}

    for key, val in encoded_images.items():
       
        new_known_faces[key] = [np.array(val)]

    for encoded_face in encoded_live_faces:

        best_match_distance = 1  
        best_match_name = "Unknown"

        for name,face in new_known_faces.items():
            matches = fr.compare_faces(face,encoded_face)
            face_distance = fr.face_distance(face,encoded_face)
            
            min_distance_index = np.argmin(face_distance)
        

            
            if matches[min_distance_index] and face_distance[min_distance_index] < best_match_distance:
                best_match_distance = face_distance[min_distance_index]
                best_match_name = name
                return best_match_name

        return best_match_name
       

        

    
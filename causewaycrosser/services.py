import json
import os
import requests

def get_all_images():
    
    lta_api_key = os.environ.get('LTA_API_KEY')
    
    url = 'http://datamall2.mytransport.sg/ltaodataservice/Traffic-Images'
    
    headers = {'AccountKey' : lta_api_key, 'accept' : 'application/json'} 
    
    r = requests.get(url, headers=headers)
    
    all_images = json.loads(r.text)
    
    return all_images

def get_some_images(all_images):

    some_images = []
    i=0

    while i < 50:
        if all_images['value'][i]['CameraID'] == '2701':
            some_images.append(all_images['value'][i]['ImageLink'])
        if all_images['value'][i]['CameraID'] == '2702':
            some_images.append(all_images['value'][i]['ImageLink'])
        if all_images['value'][i]['CameraID'] == '2704':
            some_images.append(all_images['value'][i]['ImageLink'])
        i = i + 1
        
    return some_images

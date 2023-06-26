import requests
from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = 'acc_dd700ee8152491f'
api_secret = '0a494150eda85de6bacd6cc0df281f82'
script_dir = os.path.dirname(__file__)
rel_path = "out.jpg"
image_path = os.path.join(script_dir, rel_path)
api_url = 'https://api.imagga.com/v2/tags?language=ru'


async def scaning_photo(): 
    response = requests.post(
        api_url,
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    print(response)
    obj = str(response.json()['result']['tags']
              [0]['tag']['ru']).capitalize()
    probability = str(response.json()['result']
                      ['tags'][0]['confidence']).capitalize()
    print(probability, obj)
    os.remove(image_path)

    return f'С вероятностью {probability}% это {obj} '


@app.post("/files/")
async def get_photos(file: UploadFile):
    try:
        img = Image.open(file.file)
        img.save('out.jpg')
    finally:
        width = img.width
        height = img.height
        file.file.close()
        img.close()
        res = await scaning_photo()
        print(res)
        return {'res': res, 'height': height, 'width': width}

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

api_key = os.getenv('API_KEY3')
api_secret = os.getenv('API_SECRET3')
image_path = os.getenv('IMAGE_PATH')
api_url = os.getenv('API_URL')


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

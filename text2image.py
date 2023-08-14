import argparse 
import json
import requests
import io
from PIL import Image
import os

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}

def get_predictions(word) -> io.BytesIO:
	response = requests.post(API_URL, headers=headers, json={"inputs": word})
	return io.BytesIO(response.content)


parser = argparse.ArgumentParser(
    prog="text2image"
)

parser.add_argument("-f", "--file", help="JSON file path", required=True)
args = parser.parse_args()
file_path = args.file

with open(file_path) as file:
    words = json.load(file)



from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()        
gauth.LocalWebserverAuth()   
drive = GoogleDrive(gauth)  


for prof_level in words.keys():
    for word_dict in words[prof_level]:
        word = word_dict["word"]
        image = Image.open(get_predictions(word))

        img_path = f"images/{word}.png"
        image.save(img_path)
        gd_file = drive.CreateFile({'title': f"{word}.png"})
        gd_file.SetContentFile(img_path)
        gd_file.Upload()

        gd_file = None
        os.system(f"rm {img_path}")
